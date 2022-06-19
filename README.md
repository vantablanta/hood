# Rater
>Developed by [Michelle-Njeri](https://github.com/vantablanta)  
  
## Description  
>A web application that allows you to be in the loop about everything happening in your neighborhood. 
From contact information of different handyman to meeting announcements or even alerts.

##  Live Link  
>[View Site](https://hood-mn.herokuapp.com)  to visit the site
  

## User Story  
  
* Sign in to the application to start using.
* Check out available hoods and join one.
* Create a hood if you dont find any suitable ones for you.
* See news alerts posted
* See amenitites listed in the hood
* See businesses within the hood 
* Interact woh your hood mates by commenitng in the comments section
    
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
```bash 
 https://github.com/vantablanta/hood.git
```
##### Navigate into the folder
 ```bash 
cd project-gram
```
##### Install and activate Virtual  
 ```bash 
pipenv shell 
```  
##### Install Dependencies  
 ```bash 
 pipenv sync
```  
##### Setup Database  
  SetUp your database User,Password, Host then make migrations 
 ```bash 
python manage.py makemigrations app
 ``` 
 Now Migrate  
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
Open the application on your browser `127.0.0.1:8000`.  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 4.0](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [vantablanta@gmail.com]  
  
## License 

[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/vantablanta/hood/blob/master/LICENSE)  
>Copyright (c) 2022 **Michelle Njeri**