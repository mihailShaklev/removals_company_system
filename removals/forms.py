from django import forms

class CreateJob(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    date = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    time = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'time','placeholder':'Time HH:MM'}))
    cost = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Cost'}))
    commission = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Commission'}))
    pickup = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Pickup address'}))
    pickup_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Code'}))
    mover = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mover'}))
    delivery = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Delivery address'}))
    delivery_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Code'}))
    details = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Details'}))


