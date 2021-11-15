from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.urls import reverse
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json
from .models import *
from .forms import *
from removals.helper_functions import *


def index(request):

    if request.user.is_authenticated:
        # Get all jobs from db
        today = datetime.today().strftime('%Y-%m-%d')
        if request.user.role == 'admin' or request.user.role == 'master':
            results = Jobs.objects.filter(date=today).order_by('date', 'time')
        else:
            results = Jobs.objects.filter(date=today, mover=request.user.username).order_by('date', 'time')

        # Create Paginator
        paginator = Paginator(results, 10)

        if request.GET.get('page'):
            page_number = request.GET.get('page')
        else:
            page_number = 1

        jobs = paginator.get_page(page_number)

        period = today

        movers = Jobs.objects.values('mover').distinct()
        emails = User.objects.values('email').exclude(id=request.user.id)

        return render(request, "removals/index.html", {"jobs": jobs, "period": period, "movers": movers, "emails": emails})
    else:
        return render(request, "removals/index.html")


@login_required(login_url="login")
def profile(request):

    if request.method == "POST":
        pass
    else:
        user = request.user
        return render(request, "removals/profile.html", {"user": user})


@login_required(login_url="login")
def search(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]

        results = None

        if name != '' and phone != '' and email != '':
            results = Jobs.objects.filter(name__icontains=name, phone=phone, email=email)
        elif name:
            results = Jobs.objects.filter(name__icontains=name)
        elif phone:
            results = Jobs.objects.filter(phone=phone)
        elif email:
            results = Jobs.objects.filter(email=email)

        return render(request, "removals/search.html", {"jobs": results})

    elif request.method == "GET":
        return render(request, "removals/search.html")

@login_required(login_url="login")
def report_by_date(request):

    role = request.user.role
    username = request.user.username
    startDate = request.GET.get('date1')
    endDate = request.GET.get('date2')
    mover = request.GET.get('movers')


    # Check if there is any period provided by the user
    if (startDate and endDate) or mover:

        if role == 'master' or role == 'admin':
            if mover and mover != 'all':
                results = Jobs.objects.filter(date__range=[startDate, endDate], mover=mover).order_by('date', 'time')
            else:
                results = Jobs.objects.filter(date__range=[startDate, endDate]).order_by('date', 'time')
        else:
            results = Jobs.objects.filter(mover=username,date__range=[startDate, endDate]).order_by('date', 'time')

        # Create Paginator
        paginator = Paginator(results, 10)

        if request.GET.get('page'):
           page_number = request.GET.get('page')
        else:
           page_number = 1

        jobs = paginator.get_page(page_number)

        period = startDate + ' - ' + endDate

        # Get the list of movers
        movers = Jobs.objects.values('mover').distinct()
        emails = User.objects.values('email').exclude(id=request.user.id)

        return render(request, "removals/index.html", {"jobs": jobs, "period": period, "startDate": startDate, "endDate": endDate, "movers": movers, "mover": mover, "emails": emails})
    else:
        # Else redirect to the today`s report
        return HttpResponseRedirect(reverse('index'))


@login_required(login_url="login")
def create_user(request):

    # If request method is POST
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]

        # Try to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            user.role = role
            user.save()
        except IntegrityError:
            return render(request, "removals/create-user.html",
            {"message":"Username already taken."})

        message = "User created successfully!"
        return render(request, "removals/create-user.html", {"message": message})

    # If request method is GET
    elif request.method == "GET":
        return render(request, "removals/create-user.html")


@csrf_exempt
@login_required(login_url="login")
def update_profile(request):

    userId = request.user.id
    data = json.loads(request.body)
    password = data["password"]
    email = data["email"]

    user = User.objects.get(id=userId)
    user.email = email
    user.set_password(password)
    user.save()

    return HttpResponse(status=204)


@login_required(login_url="login")
def create_job(request):
    if request.method == "POST":
        user = request.user
        form = CreateJob(request.POST)
        if form.is_valid():
            # Get the form inputs if valid
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            cost = form.cleaned_data["cost"]
            commission = form.cleaned_data["commission"]
            pickup = form.cleaned_data["pickup"]
            pickup_code = form.cleaned_data["pickup_code"]
            mover = form.cleaned_data["mover"]
            delivery = form.cleaned_data["delivery"]
            delivery_code = form.cleaned_data["delivery_code"]
            details = form.cleaned_data["details"]

            # Insert job in db
            job = Jobs(user=user, name=name, phone=phone, email=email, pickup=pickup,
            delivery=delivery, final_cost=cost, commission=commission, date=date, time=time, pick_code=pickup_code, deliv_code=delivery_code, comment=details, mover=mover)

            job.save()

            # Create new empty form and show success message
            form = CreateJob()
            return render(request, "removals/create-job.html", {"message":"Job added successfully!", "form": form})


    elif request.method == "GET":

        # Create empty form and render it
        form = CreateJob()
        return render(request, "removals/create-job.html", {"form": form})


@login_required(login_url="login")
def edit_job(request, jobId):
    if request.method == "GET":
        job = Jobs.objects.get(id=jobId)
        return render(request, "removals/edit-job.html", {"job": job})
    else:
        newName = request.POST["name"]
        newPhone = request.POST["phone"]
        newEmail = request.POST["email"]
        newPickup = request.POST["pickup"]
        newDelivery = request.POST["delivery"]
        newCost = request.POST["cost"]
        newDate = request.POST["date"]
        newTime = request.POST["time"]
        newPickCode = request.POST["pickup-code"]
        newDelivCode = request.POST["delivery-code"]
        newComment = request.POST["details"]
        newMover = request.POST["mover"]

        job = Jobs.objects.get(id=jobId)
        job.name = newName
        job.phone = newPhone
        job.email = newEmail
        job.pickup = newPickup
        job.delivery = newDelivery
        job.final_cost = newCost
        job.date = newDate
        job.time = newTime
        job.pick_code = newPickCode
        job.deliv_code = newDelivCode
        job.comment = newComment
        job.mover = newMover
        job.save()

        form = CreateJob()
        return render(request, "removals/create-job.html", {"message":"Job was updated successfully!", "form": form})


@csrf_exempt
@login_required(login_url="login")
def send_еmail(request):

    data = json.loads(request.body)
    startDate = data["startDate"]
    endDate = data["endDate"]
    mover = data["mover"]
    receiverEmail = data["userEmail"]
    date = startDate + ' - ' + endDate
    userName = request.user.username

    if startDate and endDate:
        if mover:
            if mover == "all":
                results = Jobs.objects.filter(date__range=[startDate, endDate]).order_by('date','time')
            else:
                results = Jobs.objects.filter(mover=mover, date__range=[startDate, endDate]).order_by('date', 'time')
        else:
            if request.user.role != "master":
                results = Jobs.objects.filter(mover=userName, date__range=[startDate, endDate]).order_by('date', 'time')
            else:
                results = Jobs.objects.filter(date__range=[startDate, endDate]).order_by('date', 'time')

    else:
        today = datetime.today().strftime('%Y-%m-%d')
        results = Jobs.objects.filter(date=today)

    # convert results from db to html table
    html_body = convert_query_to_html(results)

    # send the html table to the specified receiver email
    send_mail(
        f"Removals for {date}",
        'Here is the message',
        'noreplytothis377@gmail.com',
        [f"{receiverEmail}"],
        fail_silently=False,
        html_message=html_body,
        )


@csrf_exempt
@login_required(login_url="login")
def delete_job(request):

    data = json.loads(request.body)
    jobId = data["jobId"]

    job = Jobs.objects.get(id=jobId).delete()

    return HttpResponse(status=204)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        # Check if authentication is successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "removals/login.html",
            {"message":"Invalid username and/or password."})
    else:
        return render(request, "removals/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))