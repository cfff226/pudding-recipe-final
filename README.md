# The Pudding Menu:

As someone who loves a dessert, I am always on the look out for new recipes and ingredients ideas. This website is designed to enable users to add their own recipes and take inspiration from others.
The aim is to eventually showcase a catalogue of desserts which can be used for making at home or for commercial use.

# Wireframes

[Wireframes] (https://drive.google.com/file/d/18EdVVXQWrYRqrylLX6Nof3PVaW27khJJ/view?usp=sharing)

[Balsamiq] (https://balsamiq.com/) 
* All wireframes were created using Balsamiq software, since creating the wireframes, the design of the whole website had changed a lot.

* Desktop/large screen 
* Tablet screen 
* Mobile device 

## A first time user/casual user:
* I want to have access to recipes without having to create an account.
* I want to be able to quickly search for recipes without creating an account.
* I want to see a varied range of recipes.
* I want to see ingredients and methods clearly laid out and easy to follow.
* I want to be able to register with an account if I want to share my own recipes.

## As a returning user:
* I want to be able to log into my account.
* I want to be able to upload a recipe.
* I want to be able to view my profile where I can edit any existing recipes I’ve previously uploaded.

## As the site administrator:
* I want to be able to add new recipes to the site.
* I want to be able to edit the existing recipes.
* I want to be able to delete any existing recipes.

## First time/casual user goals:
* The user sees a simple explanation of the website on the home page, which will include the name and the purpose of the website.
* The home page will give the user the option to either log in, register or view recipes as a visitor.
* The user has the ability to view existing dessert recipes by searching in the search bar.
* The user has the option to contact the administrator/owner of the website if necessary.

## Returning visitor goals:
* The user can either log in or choose to view recipes as a visitor.
* The user can easily navigate to the ‘Add a recipe’ feature which is only available for logged in users.
* The user can view all recipes previously uploaded and the ability to edit, delete or add more.
* The user can log out.
* The user can contact the administrator/owner of the website if necessary.

## Developer goals:
* Demonstrate a solid understanding of MongoDB, Heroku, Python, CSS, HTML and Javascript and how they work simultaneously. 
* Build a clean, easy to navigate dessert recipe website.
* Provide users with the ability to use the CRUD functionality to create, read, update and delete recipes.
* Build an overall functional website to add to portfolio.

## Administrator goals:
* Provide a clean, easy to navigate website which will showcase a recipe catalogue.
* Offer the option for users to contact the Administrator if necessary.
* Provide a responsive website across all screen sizes.
* Offer a clear option for users to upload their own recipes to build up the catalogue.

## Design:

### Colour Scheme:

* The colour scheme chosen is a combination of four:

* Black - #000000

* White - #ffffff

* Light Pink - #f7c1f7

* Light Blue - #bbc6f0

### Typography:

The font used are default font families which are part of the Bootstrap template used. These are as follows:

* Sans Serif

* Monospace

* I'd kept these as they are similar and want to go for an easily readable font as there will be a lot of written content on the recipe pages.

### Imagery:

All images used were from Unsplash, these are images that the website will begin showing, before the website builds up a larger catalogue.

[The background image] ("https://images.unsplash.com/photo-1486427944299-d1955d23e34d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80")


### Features:

### Adding a recipe:

* The Add A Recipe feature is available for all registered users, after navigating to the Add A Recipe page there will be a form displayed.
This form requires all fields to be completed, these are inclusive of Dessert Name, Dessert Indredients, Dessert Method and an Image URL of the dessert.

* Initially the form input was a text box, although I decided to change this to a list input which I needed to incorporate some JQuery in order to get working.
I looked on Stack Overflow for more information and was advised a website by one of the tutors to look into.
[Form functions using JQuery] (https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery).

### Database:

* Mongodb is where the database is located. All information including, registration, log in, all form inputs are stored in Mongodb which
only the website administrator will have full access to.

* User access is limited to their own input, this enables users to use the CRUD - Create, Read, Update and Delete - on any of their own recipes.

## Testing

### Google Chrome Lighthouse

* I used this testing method towards the end of my project and the score was very high at 97%:
.
* [Lighthouse overall score] (https://drive.google.com/file/d/1ju1C8xFnCoiSscz_G4W2pNdRtHq_pmGu/view?usp=sharing).

* 87% score on best practices (https://drive.google.com/file/d/1Sz6TXAklMFRu2QLT7uVvw2xnaJZ4Os1P/view?usp=sharing).

* There weren't any major errors to fix after this feedback, but I did make changes to the following:

* Removed inactive css, although when I attempted to remove all inactive css shown in Lighthouse, there were significant differences
made to my project, so I went through and removed only some of what it showed.

### Powermapper repository

* [Powermapper initial score] (https://drive.google.com/file/d/19CSqyi90B2Q6bmFjjME6Q0u1tJhmxgFZ/view?usp=sharing)

* I used this testing method towards the end of my project and the score wasn't very good so there were some small changes to make.

* I was using the same title for multiple pages - I corrected this.

* There was a name missed out on a form - This was corrected.

* A lot of CSS was showing as being inactive, however when I removed some in attempt to clear, it was showing as active css and making changes.


## User stories testing:

## A first time user/casual user:

* I want to have access to recipes without having to create an account.

* This is possible. (https://drive.google.com/file/d/1Pe5UyXWIgNOI6RrfpZpELx2bDwNjAtQQ/view?usp=sharing)

* I want to be able to quickly search for recipes without creating an account.

* This is possible (https://drive.google.com/file/d/1lgy0V5mBjkC8SpcTsF2ROZFd2vaQ9VYF/view?usp=sharing)

* I want to see a varied range of recipes. - Overtime the catalogue will build up and there will be more of a variation of recipes.

* I want to see ingredients and methods clearly laid out and easy to follow. - Each recipe is displayed on a card, the image
is shown at the front all other information is listed on the back of the card, this is scrollable. All form input is limited to list style,
this is so there is a consistent layout across all recipes.

* I want to be able to register with an account if I want to share my own recipes. - Registered users have a profile where they will see all of
their own recipes displayed. They will be able to edit or delete their own recipes from the profile page and recipes page.


## As a returning user:

* I want to be able to log into my account.

* The user will have the opportunity to log into their account after they've registered. The website will keep them logged in until they log out.
They will have the option to autofill their credentials if they've enabled that feature.

* I want to be able to upload a recipe.

* The user will be able to add a new recipe by navigating to the 'Add A Recipe' tab in the nav bar, this will take them to a form input which will require
an image of the dessert, a name, method and ingredients. 

* I want to be able to view my profile where I can edit any existing recipes I’ve previously uploaded.

## As the site administrator:

* I want to be able to edit the existing recipes.

* I want to be able to delete any existing recipes.

* I want to be able to add new recipes to the site. - Once the user has registered, the user will be able to add, edit and delete any
of their own recipes on the website. This is implicated using CRUD method.

## Bugs

* I kept finding a bug which stopped the nav bar from working after 3 clicks, this was due to where I was using a combination of Bootstrap 4.5
and Materialize quite early on. I decided to go with Bootstrap and removed Materialize entirely. This corrected the issue.

## Deployment

### Heroku Deployment

This project was deployed through Heroku using the following steps:

### Requirements and Procfile

* It is necessary to let Heroku know of all requirements that were needed for the project. The following steps were made
in order to do this:

* In the Gitpod Terminal type pip3 freeze --local > requirements.txt.
* In the GitPod terminal, type echo web: python run.py > Procfile to create your procfile.
* The Procfile needs to contain the following line: web: python app.py
* Push these files to your repository.

### Enviroment file

* Create an env.py file and include the following information:

import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", -This is a unique secret key-)
os.environ.setdefault("MONGO_URI",  -unique uri from mongo.db- )
os.environ.setdefault("MONGO_DB", -name of mongodb- )
This information must be stored in the gitignore file, as this contains sensitive information and isn't to be visible to others.

### Creating Heroku App

* Log into Heroku
* Select 'Create New App' from your dashboard
* Choose an app name
* Select the relevant region based on your location
* Select 'Create App'
* 'Connecting to GitHub' Will show
*  Click the 'Deploy' tab towards the top of the screen
* Locate 'Deployment Method' and select 'GitHub'
* Locate your repository name by using the search bar
* Connect to the repository of choice
* Click the 'Settings' tab at the top of the page
* Locate 'Config Vars' and click 'Reveal Config Vars'
* Enter the relevant keys and values which must match the key/value pairs in your env.py file
* Go back to the 'Deploy' tab and select 'Enable Automatic Deployment'
* Locate 'Manual Deploy', choose the master branch and then select 'Deploy Branch'
* Please allow a few moments for it to load and then select 'Open App'


### Forking the GitHub Repository

This method will make a copy of the original repository to the Github account. This will be used in the event of the User wanting to make changes to the repository,
without affecting the original. 
Instructions for this are as follows:
* Log on to Github and locate the GitHub Repository
* Find the ‘Settings’ button on the menu and locate the ‘Fork’ button.
* This will create a copy of the original repository that you should now see in your GitHub account.
* Making a Local Clone
* Log in to Github and locate the GitHub Repository
* Click ‘Clone or download’.
* If you’re using HTTPS, locate ‘Clone with HTTPS’, then copy the link provided.
* Open Git Bash.
* Change the location of the current directory to your location of choice.
* Type git clone and then paste the URL which you copied in Step 3.

## Languages used:
* Python3
* HTML5
* CSS3
* JavaScript

## Frameworks and libraries used:
* Flask
* Flask-PyMongo
* Pip3
* dnspython
* jQuery
* Jinja
* Werkzeug
* Materialize
* [Bootstrap template] (https://startbootstrap.com/template/blog-home) 

## Other external sources used:
* Heroku used to deploy the live site.
* MongoDB used to host the database and its information.
* GitHub used to host repository.
* GitPod used to develop the project.
* Balsamiq used to create wireframes.
* RandomKeygen used to create a password for required <SECRET_KEY>.
* Responsinator used to check site was responsive on different screen sizes.
* Unsplash for images used.

### Code

* The flip cards I ended up changing towards the end of my project for aesthetic reasons.
I took a template from [W3Schools] (https://www.w3schools.com/howto/howto_css_flip_card.asp) and tweaked this for my projects purpose.
* CSS code for link styling from [W3Schools] (https://www.w3schools.com/css/css_link.asp)
* Javascript code which was taken from [sanwebe] (https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery)
This was useful for adding additional input fields onto forms, as I intended for the forms to be list inputs.

## Content

### Images [Unsplash]
* Background across all pages [The background image] ("https://images.unsplash.com/photo-1486427944299-d1955d23e34d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80")
* Recipe images

### Recipes used
* Most recipes were collected from [BBC Good Food Website] (https://www.bbcgoodfood.com/) and some were from own knowledge.
These are as follows:
* Carrot Cake
* Chocolate Cake
* Victoria Sponge
* Tiramisu
* No Bake Cheesecake
* Apple Pie 
* Chocolate Chip Cookies
* Chocolate Brownies
* Muffins 

## Acknowledgements 
* Code Institute Tutor's and Mentor for continued help and support.
* Other Students using Slack.
* Help from Stack Overflow and external sources.





