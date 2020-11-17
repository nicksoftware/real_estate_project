# Real Estate Project

---
## Getting Started.
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites.
What things you need to install the software and how to install them
```
Python3.7
Pip
Virtulenv(virtualenvwrapper preferably)
```
[Optional]
```
Virtulenvwrapper
```
### Installing.

A step by step series of examples that tell you how to get a development env running
##### Python3.7
_You’ll need to be logged in as a user with sudo access to be able to install packages on your Ubuntu system._

1. Start by updating the packages list and installing the prerequisites:
```
sudo apt update
sudo apt install software-properties-common
```
2. Next, add the deadsnakes PPA to your sources list:
```
sudo add-apt-repository ppa:deadsnakes/ppa
```
* When prompted press Enter to continue:
* Press [ENTER] to continue or Ctrl-c to cancel adding it.

3. Once the repository is enabled, install Python 3.7 with:
```
sudo apt install python3.7
```
4. At this point, Python 3.7 is installed on your Ubuntu system and ready to be used. You can verify it by typing:
```
python3.7 --version
```
#####  PIP3
Install PIP3 on Ubuntu with Apt.
```
sudo apt install python3-pip
```
##### Virtulenv
Install the virtualenv using PIP3.
```
pip3 install virtualenv
```
##### Virtualenvwrapper
Read the virtualenvwrapper installation guide here [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
*NOTE:* Follow *all* the steps in the guide.


---
## Setup enviroment.
---
### Create Virtualenv
Create a virtual to install all the packages you'll need for the project.
*NOTE:* It's better to use virtualenvwrapper to create your virtualenv.
#### Using Virtualenvwrapper.

1. Create your virtual envinment.
```
mkvirtualenv -p $(which python3.7) realEstate
```
- We use the p flag to specify which version of Python we want to use in our virtualenv.
2. Activate your environment.
```
workon realEstate
```
#### Using Virtualenv.
Virtualenv needs a directory to store the virtualenv files in, and the project is not the best place to place them, create the virtualenv in desired directory.
1. Navigate to desired directory/folder.
```
cd navigate/some/where/desired/
```
2. Create your environment
```
virtualenv -p $(which python3.7) realEstate
```
3. Activate your environment.
```
source /path/to/venv/bin/activate
```
Find out more about virtual environments in the [Virtualens docs](https://virtualenv.pypa.io/)
#### Test virtualenv activity.
1. Virtualenv name in brackets.
Before doing anything to test if your virtualenv is active, your virtualenv name should be visible in brackets inside your cli, like so:
```
(realEstate)~ 
```
or 
```
(realEstate)whatever-Your-cli-shows~
```
2. pip3 freeze
running:
```
Pip3 freeze
```
should return an empty list or nothing.
3. Python
When you type in ```python```  inside your cli then Python3.7 should be launched, close Python by typing in ```quit()```. If you type in ```which python``` the path that gets printed out will be for a python executable within your virtualenvironment. like so:
```
/path/to/your/realEstate/venv/bin/python
```
### Install Packages
1. Navigate to your github project clone using ```cd```.
2. Inside your project navigate to your app, realEstate.
3. install all the packages like so:
```
pip3 install -r requirements.txt
```

### Start development server.
Now that you have a running database service, start your development server by navigating to your application folder, inside your preoject folder:
```
cd ~/path/to/project/folder/realEstate/
```
Start the server using the `manage.py` file created automatically by creating a django-application.
```
python3.7 manage.py runserver
```
Read more about the manage.py and runserver command here: [runserver](https://docs.djangoproject.com/en/2.2/ref/django-admin/#runserver)

*NB:*
- Make sure your virtualenv is running.
- Make sure you installed all packages in the requirements.txt file

The cli should return information about the server and the port, now check out the application on the active port. Go to a browser and view your application.
### Creating superuser.
To have all the permission create a super user account for yourself, like so:
```
Python3.7 manage.py createsuperuser
```
Fill in all requested information.
Find out more about the [createsuperuser command](https://docs.djangoproject.com/en/2.2/ref/django-admin/#createsuperuser).


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used.

## Contributing

Please read [CONTRIBUTING.md](#) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [git](https://git-scm.com/) for versioning. 

## Authors
Hlulani Nicolas Maluleke

## Acknowledgments

* Hat tip to anyone whose code was used
