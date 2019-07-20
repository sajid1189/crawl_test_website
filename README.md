# A django powered website to test your crawling strategy

## How to use:

- Install the requirements from the requirements.txt
- Run the management command with tow positional arguments. The first argument is the number of pages on the site and the second argument is the number of maximum links per page.
 python manage.py create_new_site 10000, 50
 
 ## Complete installation instructions (on Ubuntu)
 ### The project uses Django 2.1 which is compatible with only Python 3
 
 - Install PostgresQL server
   `sudo apt-get install postgresql postgresql-contrib`
 
 - Install  PIP
   `sudo apt install python3-pip`
 
 - Install virtual environment
   `pip3 install virtualenv`
 
 - Create a virtual env
  `virtualenv venv`
 
 - Activate the virtual environment
  `source venv/bin/activate`
  
 - Install the requirements
   `pip3 install -r requirements.txt`
  