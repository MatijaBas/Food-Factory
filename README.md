# [Food Factory Cookbook](https://food-factory-recipes-ms3.herokuapp.com/) - Milestone Project Three

## Table of Contents

- [**About**](#About)
  - [Why This Project?](#Why-This-Project)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Style Rationale](#Style-Rationale)
  - [Mockups](#Mockups)
  - [Database Schema](#Database-Schema)
- [**Features**](#Features)
  - [Functionality](#Functionality)
  - [Existing Features](#Existing-Features)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [Version Control](#Version-Control)
  - [Hosting](#Hosting)
- [**Testing**](#Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Responsive and Functional Testing](#Responsive-and-Functional-Testing)
  - [Additional Testing](#Additional-Testing)
  - [Code Validation](#Code-Validation)
  - [Bugs Or Problems](#Bugs-Or-Problems)
- [**Deployment**](#Deployment)
  - [Live App Link](#Live-App-Link)
  - [Repository Link](#Repository-Link)
  - [Running Code Locally](#Running-Code-Locally)
- [**Credits**](#Credits)
  - [Content](#Content)
  - [Acknowledgements](#Acknowledgements)
  - [Disclaimer](#Disclaimer)

## About

I have created online cookbook containing recipes in different categories. My intention was to create a place where user can find an inspiration to create their everyday but also recipes for special occasions. In addition, user can register and login to be able to add, edit and delete their own recipes. For easier and quicker experience, user can browse recipes, searching by category or cooking time. 

### Why This Project?

This project was created for the Data Centric Development  project of [**_Code Institute's_**](https://codeinstitute.net/) Full Stack Software Development course. The project scope was to create a web app using Python and a no-SQL database (MongoDB), which uses CRUD operations to allow users to easily create, read, update and delete food recipes.
The front-end display and functionality uses HTML, CSS and JavaScript. The back-end functionality uses Python, Flask and MongoDB.


## UX

### User Stories

-	As user, I would like to check out different recipes
-	As user, I would like to browse recipes by different categories
-	As user, I would like to add my recipes
-	As user, I would like to edit existing recipes on webpage
-	As user, I would like to delete existing receipt on webpage
-	As user, I would like to register on the webpage
-	As user, I would like to login to the webpage
-	My goal was to create user friendly , easily accessible, data driven web application


### Style Rationale

When doing research for this project, I was browsing through google.com for different webpages with similar theme.  I drew the layout for this webpage using pen and paper. Then tried on different colours and background images I found on google.com to find a best match to the idea I had in my head.

### Mockups

I drew my Mockups using paper and pen, there is few of them such as the home page, recipe page, add recipe page, login and register.

- [Homepage](https://github.com/MatijaBas/Food-Factory/blob/master/Mockups/Homepage.pdf)
- [Search](https://github.com/MatijaBas/Food-Factory/blob/master/Mockups/Search.pdf)
- [All Recipes](https://github.com/MatijaBas/Food-Factory/blob/master/Mockups/All_recipes.pdf)
- [Add recipe](https://github.com/MatijaBas/Food-Factory/blob/master/Mockups/Add_recipe.pdf)
- [Login](https://github.com/MatijaBas/Food-Factory/blob/master/Mockups/Login.pdf)
- [Register](https://github.com/MatijaBas/Food-Factory/blob/master/Mockups/Register.pdf)

### Database Schema

To help me build my project I have created different databases for the collections I would use;
-	[Recipe Schema](https://github.com/MatijaBas/Food-Factory/blob/master/database_schema/dataschema.pdf)
-	Category Schema
-	UserLogin Schema


## Features

### Functionality

This website uses Python logic to allow users to login, or register for a free account. The app offers CRUD operations to allow users to create, edit and delete food recipes. Users can search for a recipe by name, or they can filter recipes based on various categories.

### Existing Features

- **Login** - Allows existing users to login to their account. The form's username field only accepts alphanumeric values. I've included authorization checks to verify the username and password
-**Register** - Allows new users to register for a free account. The form's username field only accepts alphanumeric values. I've included checks to ensure that the username doesn't already exist in the database before users are successfully registered
-	**Add Recipe** - Create operation. Allows the user to add a new recipe to the site and database. All form fields are required. There is no add image field so image is added by default(same picture for all recipes) Additionally, the new recipe's ObjectID is added to the  database.
-**Edit Recipe** - Update operation. All existing recipe values are pre-populated in the relevant form fields, which the user is able to edit if required. Upon form submission, the recipe database record is updated with the new values. Additionally, the last edited date field in the recipe record is at the end of the list.
-**Delete Recipe** - The Delete button is available for all users. Clicking the button triggers the Delete modal, which asks the user to confirm the deletion request. If the user presses 'YES', the 'deleted' field in the recipe's database record is updated to 'True', which ensures that the recipe is no longer displayed on the app, although the record is removed from the database.

### Features Left to Implement

With more time on disposal, I would like to finish functionality for login, register and search-browse engine. This is in the app butt it's not working at the moment.

## Technologies Used

- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.
- [**SCSS**](https://sass-lang.com/documentation/syntax)
    - The project uses **SCSS** to add custom styles to the elements and content of my app. I used **SCSS** instead of **CSS**, as it is more powerful and I used the logic to write some variables, mixins and media queries, which I called for various features.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles created with **SCSS** to my app. The base.html file is linked directly to the main.min.css stylesheet.
- [**Bootstrap**](https://getbootstrap.com/)
    - The project uses the **Bootstrap** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Bootstrap styles to my app, before adding my custom styles.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**PyMongo**](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.
- [**Flask**](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses **Flask**, which is a Python microframework.
- [**Flask Blueprint**](https://flask.palletsprojects.com/en/1.0.x/blueprints/)
    - The project user **Flask Blueprint** to compartmentalise my Python code and make it more modular and easier to navigate.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**MongoDB**](https://cloud.mongodb.com/)
    - The project uses **MongoDB** to store the database in the cloud. The information displayed in the front-end app is pulled from the database store.
- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text and suit my chosen theme. The brand logo uses the *_Dancing Script_* font and the rest of the site uses the *_Roboto_* font.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.
- [**Gitpod**](https://www.gitpod.io/)
    - I've used **Gitpod** as the development environment to write the code for my website.

### Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project in Gitpod, before pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

### Hosting

- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

## Testing

I used Google Chrome's Development tools to constantly test each change that I made to my project and to ensure that it appeared in the desired way on different screen sizes. I also tested my app on different screen sizes (mobile, tablet and desktop) to ensure it appeared in the desired way on different devices.

### Additional Testing

In addition to my own testing, I also asked family members, friends and the Slack community to test my app and provide any feedback.

### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) to validate my JavaScript syntax.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

### Bugs Or Problems

- There is few Unresolved problems that I'am aware of but didn't have a time to fix it. 
 - **Delete Button** So if you decide to delete a recipe, you are gonna be asked are you sure?, and if you decide to click cancel, recipe will be deleted any way.
 - **image upload** it's default image for all recipes add by user, only I can add real images of recipes.
- **Edit categories** If you decide to edit recipe and click on edit button, on new open page you can't change the categorie.

## Deployment


                                        
                       
                        deployment of project through github 
                
    1. Go to the terminal 
    2. Typed in git add "filename of what you want to push" and press enter key
    3. Typed in commit -m "type in the message that I would explain about the commit in quotations"
    4. Repeat if neccessary for more files 
    5. Typed in  git push 
    6. files are now pushed to github


                        
                       
                       deployment of page through github pages
                       
                        
                
    1.Go to the github repository of happy cooking
    2. Then click on settings up on the right handside of the screen under the watch button
    3. Scroll down to the Github Pages
    4. In the container there is a source heading and a option button that has the word "none" with a little arrow pointing down the right
    5. Click on this and it will give you three options master branch, master branch/docs folder or none.
    6. click the master branch.
                      
                      
                      
                      
                      
                        creating up herokua app
                
    1. Log in using username and password
    2. In the personal page click the "NEW" button
    3. Click "Create new app"
    4. This brought me to Create new app page
    5. Type in an app name you want to call the app i called mine food-factory-recipes-ms3
    6. Choose a region united states or europe, i choose europe
    7. Press "create app" button.
    8. The app is now created.
    
    
    
    
                        Create a new Git repository
                        
    1. Type in "cd my-project/" in the terminal
    2. Next type in "git init"
    3. After that I typed in "heroku git:remote -a food-factory-recipes-ms3"                    
                        
            set up Deployment to Heroku in terminal of gitpod
                
    1. Go to the "deploy" page in heroku app
    2. To set up heroku deployment from github to heroku scroll down to "Deploy using Heroku Git" section
    3. Typed in "heroku login" to the terminal of gitpod
    4. Open url of login and click login to connect heroku with gitpod
    
    5.Created a requirements.txt file using the following command in the terminal window:

    ```sudo pip3 freeze --local > requirements.txt```

    6. Created a Procfile using the following command in the terminal window:

    ```echo web: python <fileName.py> > Procfile```

    7. Ran the `git push heroku master` command in the terminal window to push the app to Heroku.
    8. Ran the `heroku: ps:scale web=1` command in the terminal window to run the app in Heroku.
    9. Entered the following Config Var in Heroku:

    ```MONGO_URI : <link to MongoDB>```
    
                     set up Deployment to Heroku app
                
    1. Go to the "settings" page in heroku app
    2. To set up heroku config vars from cloud9 to heroku scroll down  and click on "Reveal Config Vars" section:
    3. Typed in "IP" to KEY and "0.0.0.0" to value 
    4. Typed in "PORT" to KEY and "5000" to value 
    5. Typed in "MONGO_URI" to KEY and "mongodb+srv://MatijaBas:<password>@myfirstcluster-y6kfn.mongodb.net/food_factory?retryWrites=true&w=majority" to value 
    6. Typed in "SECRET_KEY" to KEY and "<secret_key>"" to value 
     
    
                Commit my code to the repository and deploy it to Heroku using cloud9 terminal 
                
    1. Open terminal
    2. Typed in git add .
    3. Typed in git commit -am "message to explain about the commit you are commiting"
    4. Typed in git push heroku master
    5. Its pushed now.
    
    
    
                         
                setting up mongodb database for collection to connect to deploy to database
                          
    1.Sign up using first name,last name and email address.
    2. Choose M0, the free forever tier.
    3. Scroll right down to the bottom of the page, click on the little arrow, and type cluster name.
    4.Then click on the create cluster button.
    5.Click on the security tab 
    6.Create a username
    7.Create a password
    8. select allow access from anywhere
    

                Create a collection for data to deploy when recipes are added in web application
                            
    1. click on the collections button
    2. click Create Database button
    3. enter "DATABASE NAME"
    4. enter "COLLECTION NAME"
    5.click "create" button
    6. click insert document and enter in data of choice to database


### Live App Link

Click the link below to run my project in the live environment:

[Food Factory](https://food-factory-recipes-ms3.herokuapp.com/)

### Repository Link

Click the link below to visit my project's GitHub repository:

[Food Factory GitHub Repository](https://github.com/MatijaBas/Food-Factory)

### Running Code Locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to [my GitHub repository](https://github.com/MatijaBas/Food-Factory)
2. Click on 'Clone or download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Git Bash' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. In the terminal, run the `pip3 install -r requirements.txt` command to install the requirements.txt file.
9. You should now be able to run the app locally using the `python3 run.py` command.

## Credits

### Content

-Every single line of the code in my project was written by myself.
- I researched how to upload images to my local directory by reading this [Flask-Uploads](https://pythonhosted.org/Flask-Uploads/) article.
- I got a general idea of how to create a register and login system by watching this [Login Video](https://www.youtube.com/watch?v=UIJKdCIEXUQ&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3)
- I read this [Error Handlers Article](https://flask.palletsprojects.com/en/1.0.x/errorhandling/) to learn how to implement error handlers in my Python code.
- I read this [Jinja Template Inheritance Article](https://jinja.palletsprojects.com/en/2.10.x/templates/) to learn how to import my partials HTML files to the main HTML files using Jinja Templating.
- I read this [SASS Output Styles Article](https://web-design-weekly.com/2014/06/15/different-sass-output-styles/) to learn how to create different styles of CSS files using SCSS.
-And many other video and tutorials that I get from my menthor.

### Media

- I found the Favicon image on Google, and I used the [Favicon Converter](https://favicon.io/favicon-converter/) to convert the image to a Favicon.
- I found all the recipe pictures used in my site on [BBC Food Website](https://www.bbc.co.uk/food).
- I found all the recipe pictures used in my site on [Crazy for crust](https://www.crazyforcrust.com/)
- I found all the recipe pictures used in my site on [Coolinarika](https://www.coolinarika.com/)

### Acknowledgements

- I received inspiration for the style of my project from [Coolinarka](https://www.coolinarika.com/)
- Thanks to everybody on SLACK that help me when I was stuck and needed assistance. Thanks Tutors aswell. They help me to debug my Python code.
- Big thanks to my mentor Antonija Simic, for her feedback on my project's scope, design and so many useful information shared. It's so inspiring to work with her and everything looks so easy.
- And at the end thanks to my wife and my Family,to gave me precious time so I can work on my project, they are biges support I can imagine.

### Disclaimer

This project is for educational purposes only.