# Url Shortener - Flask - Python
It is a technique on the World Wide Web in which a Uniform Resource Locator (URL) may be made substantially shorter and still direct to the required page. This is achieved by using a redirect which links to the web page that has a long URL

## Build Requirments
The following programming language should be installed like below

````
Language : Python
Version  : 3.6.9 { Minimum }
Package  : PIP - Python
Version  : 20.0.0 { Minimum }
````
The following packages need to installed, In-order to run the program
| Package Name | Version |
|--------------|---------|
| Flask        | 2.0.2   |
| Flask-MySQLdb        | 0.2.0   |
| Flask-Session        | 0.4.0   |
| Flask-ShortUrl       | 0.2.0   |


## After Setup the packages, Next DB
The following command are used to create the database.

[1]. Create a database 
````
Use the following command in the MySQL database, create database urlshortner
````
[2]. Create a table
````
create table users(
    pid int auto_increment primary key,
    username varchar(9) not null,
    password varchar(255) not null
);
````

[3]. Insert Some values in table
````
INSERT INTO users (userame,password) VALUES ('test@test.com','Test@1234');
````

[4]. Create a table for storing the URL Shortner records
````
create table urls(
    pid int auto_increment primary key,
    uid varchar(255) not null,
    previousurl varchar(5000) not null,
    orginalurl varchar(255) not null,
    date varchar(255) not null
);

````
## After DB Setup, Run the program
After successfully setting up the base package and DB setup, Use the following command to run the program.
### Linux Env
[1]. Export the flask env in debug mode to check the backend operations

````
Command 1:
export FLASK_APP = app.py
Command 2:
export FLASK_DEBUG = 1
````
After successfully exporting the flask, Then run with following command
````
flask run
````
### Windows Env
Running the flask along with exporting the file
````
Command 1:
setx FLASK_APP "app.py"
````
After successfully exporting the flask, Then run with following command
````
flask run
````

## Outputs
[1]. Login Page
![Login](https://user-images.githubusercontent.com/86065440/148672248-eca7b788-65e4-4e6b-a77c-a760660d37e7.png)

[2]. Register Page
![Register](https://user-images.githubusercontent.com/86065440/148672278-30d485d2-a326-41c5-ade9-0cf430b1a408.png)

[3]. Home Page
![Home](https://user-images.githubusercontent.com/86065440/148672258-2a3a4355-acfb-4e76-85f0-0069792b7a74.png)

[4]. URL Shortner
![URLShorten](https://user-images.githubusercontent.com/86065440/148672302-213a343c-b42a-4330-b226-179b6ff23fba.png)

[5]. Copy the trimmed / Shortned URL
![Copy](https://user-images.githubusercontent.com/86065440/148672329-d1ebc502-1070-4b82-913c-c9625f7a1611.png)

[6]. Stored records
![History](https://user-images.githubusercontent.com/86065440/148672346-e814795a-5be8-4da1-bf58-7d4fe064b54f.png)

[7]. Before redirected Page
![BeforeRedirect](https://user-images.githubusercontent.com/86065440/148672357-54e53773-0497-4e06-9058-069e9804b7ae.png)

[8]. After redirect
![AfterRedirect](https://user-images.githubusercontent.com/86065440/148672371-d7cd30be-b8e5-4872-9150-16153975c5c7.png)
     
      

  
