# MyProject

**Django Polls App**

This is a polls application that allows users to create, manage, and participate in polls and surveys. It can provide a user-friendly interface for both poll creators and participants, making it easy to gather opinions and insights on various topics. This app allows users to create custom polls, add multiple-choice questions, and invite participants to vote. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
Step 1:  Clone the repository:
terminal:
eg. git clone https://github.com/your-username/your-django-polls-app.git
cd your-django-polls-app

step 2: Create a virtual environment and activate it:
vscode terminal:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Step 3: Perform database migrations:
terminal:
python manage.py migrate

Step 4: Create a superuser (admin) account:
terminal:
python manage.py createsuperuser

Step 5: Run server:
terminal:
Python manage.py run server

Step 6: Navigate to the link
web browser:
http://127.0.0.1:8000/polls/

## Usage
The Django Polls app provides a straightforward and intuitive way to create, manage, and participate in polls and surveys. Follow these steps to effectively use the app:

- Creating a Poll:
To create a new poll, follow these steps:

Access the admin panel by visiting http://127.0.0.1:8000/admin/.
Log in with the superuser (admin) credentials you previously created during installation.
In the admin dashboard, navigate to the "Polls" section and click on "Add".
Fill in the poll question and any relevant information.
Add multiple-choice answers by clicking the "Add another Choice" button and entering the choices.
Save the poll.

- Participating in a Poll:

Participants can visit the homepage (http://127.0.0.1:8000/) to view the list of available polls. They can click on a poll to access the details and vote for their preferred option.

- Viewing Poll Results:

After participants have voted, the poll results will be displayed. The results show the distribution of votes for each choice in a visually appealing graph.

- Admin Features:

As an admin, you can:
Manage existing polls by editing or deleting them.
View vote counts and participant details for each poll.
Analyze poll results to gain insights.

## Credits
Author: Nombulelo Mudzwiri

## Repository URL
[https://github.com/Nombulie/MyProject](https://github.com/Nombulie/MyProject)

