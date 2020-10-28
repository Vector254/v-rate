# V-rate  
## Author  
  
[Victor Nduati](https://github.com/Vector254)  
  
# Description  
This is a Django application that allows a user to post a project he/she has created and get it reviewed by his/her peers with regards to design, usability and content.

# User stories
1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects 
5. View projects overall score
6. View my profile page
  
##  Live Link  
click [here](https://v_rate.herokuapp.com/)  to visit the live site
    
  
## Setup and Installation  
   
##### Cloning the repository:  
 ```bash
 https://github.com/Vector254/v-rate.git
```
##### Navigate into the project folder and install dependencies  
 ```bash 
 pip install -r requirements.txt 
```
##### Install and activate Virtual environment
 ```bash 
 virtualenv virtual && source virtual/bin/activate  
```  

 ##### Setup Database  
  SetUp your database User and Password, then makemigrations 
 ```bash 
 python manage.py makemigrations 
 ``` 
 Then Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 

##### Testing the application  
 ```bash 
 python manage.py test 
```
#### API endpoints
##### get requests(for post requests add a trailing slash)
```bash
 http://localhost:8000/api/projects
 http://localhost:8000/api/profiles
```

 
  
  
## Technologies used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.1.2](https://www.djangoproject.com/download/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* None, reach out below incase of any.
  
## Contact Information   
In case of any question or complaints, please [email](ochrist7@gmail.com) me
  
## License 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 
 Copyright (c) 2019 **Vector**