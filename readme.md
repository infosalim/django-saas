# Run venv
python3 -m venv venv


# Activate venv Linux
source venv/bin/activate
# Activate venv Windows
.\venv/Scripts\activate


# Installation
pip install -r requirements.txt

# Upgrade packages
pip install pip --upgrade


# pip freeze
The pip freeze command outputs a list of installed Python packages along with their versions. It is often used to generate a requirements.txt file, which can then be shared to ensure others use the same package versions.

pip freeze > requirements.txt


# Available subcommands
django-admin

# Run the project
django-admin startproject cfehome .

The command django-admin startproject cfehome . is used to create a new Django project named cfehome in the current directory. The dot (.) at the end indicates that Django should set up the project files within the current directory rather than creating a new subdirectory for the project.
