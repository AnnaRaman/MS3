# Anna Raman – RecipeBook

live: https://github.com/AnnaRaman/MS3.git

My web application presents a library of recipes, which can be viewed by all users, whether they have made an account or not. The user has the option to make an account and if they do, they are able to create, read, update and delete recipes on the website that they have control over. These recipes can be viewed in the ‘my recipes’ page. The user can search for recipes to view, but will not be able to edit or delete another users recipe. 

### USER EXPERIENCE (UX)
#### User Stories


1.	As someone who is looking to explore more recipes, I’d like to be able to browse a catalogue of different recipes and obtain information about the recipe such as the ingredients, difficulty and serving.

2.	As someone looking to organise my recipes, I would like to be able to make an account.

3.  As a user i would like to store my recipes in one place so that I can view, edit and delete them easily in my own account.

3.	As an inexperienced cook I’d like to be able to search for different recipes.


#### Design
* Layout Design

My focus with the design was to facilitate the users search for what they are looking for; a simplistic layout with clear navigation. The search function allows the user to find a recipe which best suits their preferences from the . The inspiration for the layout design was inspired by the Code Institute mini project, aided by the materialize framework, which also ensures that the website is responsive on different screen sizes. I used REM rather than pixels to further promote responsiveness.


* Colour scheme / Typography

I chose a yellow colour scheme as it known to represent food attributes, and seem appealing to the user. I chose the particular shades of colour from Materialize's colours.






#### Wireframes

https://wireframe.cc/pro/pp/6c55400ea393562 - home not logged in

https://wireframe.cc/pro/pp/7d116f633393557 - home logged in

https://wireframe.cc/pro/pp/5b9429d2f393609 - my receipes

### FEATURES

-	Responsive on all device sizes


-   User registration


-   Forms


Features Left to Implement
In order to improve the site’s potential, I would like to add an API and fetch data so that theres already is a substantial amount of data to faciliate the demonstration of the apps features.

### TECHNOLOGIES

- Languages
1.	HTML5
2.	CSS
3.	JavaScript
4.	Python


- Frameworks/libraries
4.	Flask 1.1.2
5.	Materialize CSS 1.0.0
6.	jQuery 3.5.1
7.  Jinja2
8.	Google fonts
9.	Font awesome



### TESTING

#####Validation

- HTML validator <a href="https://validator.w3.org/">W3 Markup validator</a>

- CSS Validator:  <a href="https://jigsaw.w3.org/css-validator/">jigsaw W3</a>

- Python validator: <a>PEP8</a>

- Responsive



1.	As someone who is looking to explore more recipes, I’d like to be able to browse a catalogue of different recipes and obtain information about the recipe such as the ingredients, difficulty and serving.
    -  The list of recipes is viewable to all users whether they have an account or not

2.	As someone looking to organise my recipes, I would like to be able to store my recipes in one place so that I can view, edit and delete them easily in my own account.
    - The adding recipe operator is fully functioning. Th edit and delete funcions are partly functioning. It is possible to make edits in the input fields however the submit button is not working, like with the function of deleting a recipe.

3.	As an inexperienced cook I’d like to be able to search for different recipes.


The testing process intended to ensure that website was fulfilling the needs of the user. After running through the entire website checking links, anchors, the search bar (for positive and negative results), the random generator, website compatibility and responsiveness, it is deducible that it functions as intended. The user stories mentioned in the UX section have been tested and proven success. All data fetched from the data has been received and presented as intended.

The elements on the page wrap accordingly and appropriately. The tested mobile devices were iPhone model 5 through to iPhone 8, Galaxy S5, pixel and pixel XL. 


### DEPLOYMENT
This project has been deployed from the master branch to the hosting platform, Heroku. To run locally, copy the following link into an editor: https://github.com/AnnaRaman/MS3.git The project was deployed to Heroku using the following steps:Deployment
GitHub Pages
The project was deployed to Heroku Pages using the following steps:

1.	Log into Heroku, and once logged in on your dashboard, create a new app 
2.	Make sure your github profile is displayed then add your repository name.
3.	Click search and once it finds your repository, click to connect the app.
4.	Click on the settings tab for your app and click on ‘reveal config vars’ where you can securely tell Heroku which variables are required to run the app. 
5.	The env.py file contains a different variables in our app. The first variable is IP, with the value “0.0.0.0”. Next the PORT which is “5000” copy these into Heroku config vars. For the secret key, copy that from the env.py file then past it into Heroku. 
6.	Enter the MONGO_DBNAME which is the name of our database.
7.	Go back to the Deploy tab, but before connecting, make sure to push all new files to the repository.
8.	Back within the terminal type Git status just confirm that those are our only pending changes, then add, commit and push these files to send them to GitHub.
9.	Go back to Heroku and select ‘Enable automatic deployment’
10.	Click ‘deploy branch’ 
11.	Heroku will now receive the code from GitHub, and start building the app using our required packages.
12.	Click ‘view’ to launch the app.



Cloning the Repo

1.	Log in to GitHub and locate the GitHub Repository
2.	Under the repository name, click "Clone or download".
3.	To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4.	Open Git Bash
5.	Change the current working directory to the location where you want the cloned directory to be made.
6.	Type git clone, and then paste the URL you copied in Step 3.
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
7.	Press Enter. Your local clone will be created.



### CREDITS

#### Code
- The structure and layout of the code was inspired by that of the code institute mini project.
- The forms and buttons used were templates supplied by Materialize CSS
