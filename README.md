
# TaskBuddy

TaskBuddy is a task management tool that helps individuals and teams organize, track, and prioritize tasks and projects. It provides a user-friendly interface to efficiently manage your tasks and stay productive.

## Features

- Create and manage tasks
- Assign tasks to team members
- Set due dates and priorities for tasks
- Track task progress and completion status
- Receive task notifications and reminders
- Collaborate and communicate with team members
- Generate task reports and analytics

## Installation

1. Clone the repository:
   
   git clone https://github.com/vishwanathdas/taskbuddy.git
   
2.Install the dependencies:

    
    pip install -r requirements.txt
    
asgiref==3.5.2
attrs==22.1.0
backports.zoneinfo==0.2.1
black==22.6.0
click==8.1.3
coverage==6.4.3
Django==4.0.5
factory-boy==3.2.1
Faker==13.15.1
flake8==5.0.4
iniconfig==1.1.1
mccabe==0.7.0
mypy-extensions==0.4.3
packaging==21.3
pathspec==0.9.0
platformdirs==2.5.2
pluggy==1.0.0
py==1.11.0
pycodestyle==2.9.1
pyflakes==2.5.0
pyparsing==3.0.9
pytest==7.1.2
pytest-django==4.5.2
python-dateutil==2.8.2
pytz==2022.1
six==1.16.0
sqlparse==0.4.2
tomli==2.0.1
typing-extensions==4.3.0
uWSGI==2.0.18,<2.1

3.Migration & Migrate Application:

    
    python manage.py makemigrations
    python manage.py migrate

4.Run Application:

    
    python manage.py runserver
    
 ## Configure the environment:

Copy the .env.example file and rename it to .env.
Modify the necessary environment variables in the .env file to match your setup


## Usage

Sign up for a new account or log in with your existing credentials.
Create a new task by clicking on the "New Task" button.
Fill in the task details such as title, description, due date, and assignee.
Set the priority level for the task (high, medium, low).
Save the task, and it will appear in your task list.
Update the task status as you progress.
Collaborate with team members by adding comments or attachments to the task.
Explore the other features and functionalities of TaskBuddy to manage your tasks efficiently.

## Contributing
Contributions are welcome! If you'd like to contribute to TaskBuddy, please follow these steps:

-Fork the repository.
-Create a new branch for your feature or bug fix.
-Make your changes and commit them with descriptive commit messages.
-Push your changes to your forked repository.
-Submit a pull request to the main repository, explaining the changes you've made.
-Please ensure that your code follows the project's coding style and conventions.

## License
TaskBuddy is released under the MIT License.

## Acknowledgments
TaskBuddy was inspired by the need for an efficient task management tool to boost productivity. We would like to thank the following individuals for their contributions and support:

Vishwanath Das
TaskBuddy 
