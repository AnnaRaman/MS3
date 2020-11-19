# Anna Raman – in the mix.
**Milestone Project 3: Data-CentricFrontend Development – Code Institute**

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

* Images / Animation




#### Wireframes

These can be found in the folder wireframes. 
(assets/wireframes)
 <a href="https://github.com/AnnaRaman/Cocktaill-api-milestone2/blob/be656a1f1dd5e6eb61281307e95d1f358cdc47ad/assets/wireframes/Drinks%20Page.jpeg">Drinks</a>

### FEATURES

-	Responsive on all device sizes


-   User registration


-   Form


Features Left to Implement
In order to improve the site’s potential, I would like to add an API and fetch data that corresponds to the calories/abv of the cocktails. However, I could not find an API that would do so.

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

The only errors airsing from the JS tetsing indicate that i am using ES6, however i have chosen es6 as it improves my code.

My version control relied on creating duplicates locally on my hard-drive. Unfortunately, I was unable to use git. I thought the only way to control my versions was by using GitPod. However, was unable to access GitPod so I relied Visual Studio Code. In my attempt to use version control via Visual Studio Code the terminal returned an error stating that an origin already exists for this repository. Despite numerous searching around the internet to fix this bug, I was unable to do so. Therefore, I had no choice but to create duplicates locally whenever significant changes where made.

1.	As someone who is looking to explore more recipes, I’d like to be able to browse a catalogue of different recipes and obtain information about the recipe such as the ingredients, difficulty and serving.
    - The layout of the cocktails on the cards allows the user to dynamically interact with the drinks that are presented on the cards. Due to the number of cocktails on the page, there is an overlay on the drinks section, to ***


2.	As someone looking to organise my recipes, I would like to be able to store my recipes in one place so that I can view, edit and delete them easily in my own account.
    - The hover-over effect allows the user to learn more about the cocktail that they choose, rather than being overwhelmed with information about every cocktail on the site. The front of each card provides the name and picture of the drink, while the back details the ingredients, method and rating. 

3.	As an inexperienced cook I’d like to be able to search for different recipes.
     - The search function allows the user to search in-depth to discover a cocktail that they like. If there nothing matches their search, they will be notified. If for example the user wanted to search for a cocktail by name but wasn’t sure of the spelling, the X function, makes the search easier and makes it more likely for them to find the cocktail that they are looking for. If the user doesn’t know what they are looking for, the lucky dip function randomly selects a cocktail from the array to provide some inspiration for the user.  


The testing process intended to ensure that website was fulfilling the needs of the user. After running through the entire website checking links, anchors, the search bar (for positive and negative results), the random generator, website compatibility and responsiveness, it is deducible that it functions as intended. The user stories mentioned in the UX section have been tested and proven success. All data fetched from the data has been received and presented as intended.

1.	Search bar
     2. Type in a search that does not match an item in the array, you are presented with a message informing that there were no results matching the values entered. 
     3. Start typing some letters into the search bar, and every matching result with the same values will be presented, as well of the number of matches that are returned. 

All links provided on the website have been coded with 'target="_blank"' so that the user can maintain their position on the website, whilst exploring the link's destination in a new tab. These have been tested and proven to work efficiently. The anchor tags surrounding the 'home', 'drinks', ‘lucky dip' and ‘links’, are fully functioning and allow the user to skip to their desired section. 

With thanks to Flexbox’s framework, the website has been tested and is successfully responsive to different screen sizes, and the elements on the page wrap accordingly and appropriately. The tested mobile devices were iPhone model 5 through to iPhone 8, Galaxy S5, pixel and pixel XL. 


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
- The random generator card was inspired by this <a href="https://codepen.io/jorchie/pen/PLxaXK">codepen</a>
- The button for the random generator was initially inspired by this <a href="https://codepen.io/JoeHastings/pen/MwoOeW">codepen</a>
- The useful links page design was inspired by this <a href="https://codepen.io/sincamons/pen/BNZZbg?editors=0110">codepen</a>
#### Content

The content on all of the cards is data fetched from this <a href="">API</a>

#### Media
- The animations used on the name 'in the mix.' was taken from <a href="https://animate.style/">animate.css</a>
- The GIF on the intial card of the random cocktial generator is from  a <a href="https://in.pinterest.com/pin/129408189279318218/">pintrest pin</a>
- The balls animation in the background was inspired by 
a <a href="https://codepen.io/nashvail/details/wpGgXO">Codepen</a>