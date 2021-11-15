#  🚚 Removals company system
Removals Company **Jobs Schedule System** : This is a system developed for a removals company in order to keep record of all its removal jobs.\
\
See how it works in the **video**:\
\
\
[![IMAGE ALT TEXT](http://img.youtube.com/vi/2KKx6ePu0_s/0.jpg)](https://youtube.com/watch?v=2KKx6ePu0_s&feature=share "Video Title")
\

## For Project`s details see below 👇 👇 👇

# Project Description
The project is a web site for a removal company to keep track of its removal jobs. The site has three types of user roles: master, administrator and user. According to the role of the users they are authorized to access different features.
Depending on the role of the user the manu after login shows the following features:
1. for master
    * Profile - They can change their password and email
    * Jobs - Filters jobs for certain period and mover
    * Search - Can search clients by name, phone or email
    * Create User - The master can create users
    * Create Job - Inputs a new job
    * Log Out
2. for admin
    * Profile
    * Jobs
    * Search
    * Create Job
    * Log Out
3. for user
    * Profile
    * Jobs - Filters jobs for a certain period
    * Log Out
All of the roles have the ability to see the removal jobs for a certain period. The user role can only view jobs for which the user is the mover as well. Depending on the role of the user a removal jobs table shows the following information:
1. for master and admin
    * Customer Name
    * Phone
    * Email
    * Pickup Address
    * Delivery Address
    * Date
    * Time
    * Cost
    * Profit
    * Details
    * Mover (Person in charge of the move)
    * Edit and Delete buttons for every job in the table
2. for user
    * Customer Name
    * Phone
    * Pickup Address
    * Delivery Address
    * Date
    * Time
    * Details
All of the users are able to send the generated table as an html to an email address.

# Files content
1. views.py - contains the functions for all the paths in the project
    * index - prompts the user to log in. If user is logged in shows the removal jobs for today if any.
    * profile - shows user name, user role, user email and offers the option to change password and email
    * search  - use rcan search clients by name, phone and email
    * report_by_date - shows removal jobs for certain period. Master and admin can filter results by mover as well
    * create_user - the master can create users and determine their roles
    * update_profile - users can change their password and email
    * create_job - master and admin can input new removal jobs in the database
    * edit_job - master and admin can edit existing jobs
    * send_email - users can email tables with removal jobs as html
    * delete_job - master and admin can delete jobs from database
    * login_view - logs user in
    * logout_view - logs user out
2. models.py - contains the classes for the database
    * User class
    * Jobs class
3. forms.py - contains one form
    * CreateJob class is used to create form in order to input a removal job in the database
4. layout.html - this is the basic html file
5. login.html - visualizes the login page. It requires username and password
6. index.html - after login shows the removal jobs for today and gives the opportunity to filter results or send them to and email address
7. profile.html - shows the profile of the user with their role, username, email
8. search.html - gives the option to search client by name, phone and email
9. create_job - visualizes a form to create a removal job in the database
10. edit_job - shows a pre-filled form in which one can edit an existing removal job
11. create_user - shows a form by wich a user can be created with a certain username, password and role
12. javascript.js - contains all the javascript functions
    * delete_job - deletes a job without reloading the page
    * show_edit_profile - on a button click shows a form which allows the user to edit their email and password
    * cancel_edit_profile - on a button click hides the form which edits the profile
    * save_profile - saves the new email and password the user gave
    * send_email - emails the table with removal jobs
13. style.css - contains the css code for the whole project
14. helper_functions - contains functions used in the views for specific tasks
    * convert_query_to_html - converts QuerySet from db to html table
