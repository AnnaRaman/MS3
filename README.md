# Anna Raman – in the mix.
**Milestone Project 2: Interactive Frontend Development – Code Institute**

live: 

My web application presents a library of recipes, which can be viewed by all users, whether they have made an account or not. The user has the option to make an account, and if they do they are able to create, read, update and delete recipes on the website that they have control over. These recipes can be viewed in the ‘my recipes’ page. The user can search for recipes to view, but will not be able to edit or delete another users recipe. 

### USER EXPERIENCE (UX)
#### User Stories


1.	As someone who is looking to explore more recipes, I’d like to be able to browse a catalogue of different recipes and obtain information about the recipe such as the ingredients, difficulty and serving.

2.	As someone looking to organise my recipes, I would like to be able to store my recipes in one place so that I can view, edit and delete them easily in my own account.

3.	As an inexperienced cook I’d like to be able to search for different recipes.


#### Design
* Layout Design

My focus with the design was to facilitate the users search for what they are looking for; hence, the option to search by name, ingredient, or type of cocktail. The range of possible search queries allows the user not only to find a particular cocktail that they desire, but it also allows them to find a cocktail based on their individual preferences. 
The overall design layout was inspired by <a href="https://www.mikiyakobayashi.com/">Mikiya Kobayashi</a>’s website as I found it most appealing to visit, due to the minimalist yet engaging design. I used flex throughout the code to maintain responsiveness. I used REM and EM rather than pixels to further promote responsiveness.


* Colour scheme / Typography

I chose a Triadic colour scheme in the hope of creating bright bold appearance, whilst choosing pastel colours to balance the dramatic effect, “to create a diverse yet balanced scheme” as described by <a href="https://webflow.com/blog/web-design-101-color-theory">Webflow</a>. I chose the particular shades of colours with the help of <a href="https://coolors.co/">Coolors</a>. Typography

* Images / Animation

Rather than changing the API images, I thought it best to minimise the code, and make it as clean and readable as possible. So, I chose to use animations, and GIFs as I felt they are more in line with the friendly, fun theme that is running throughout the site. I chose to use the moving balls animation, as I felt they appropriately signified the bubbles in many drinks and cocktails, drawing the user in. 



#### Wireframes

These can be found in the folder wireframes. 
(assets/wireframes)
 <a href="https://github.com/AnnaRaman/Cocktaill-api-milestone2/blob/be656a1f1dd5e6eb61281307e95d1f358cdc47ad/assets/wireframes/Drinks%20Page.jpeg">Drinks</a>

### FEATURES
•	Responsive on all device sizes


•	Interactive elements

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
7.	Google fonts
8.	Font awesome



### TESTING
- HTML validator <a href="https://validator.w3.org/">W3 Markup validator</a>

- CSS Validator:  <a href="https://jigsaw.w3.org/css-validator/">jigsaw W3</a>

- JS validator: <a href="http://beautifytools.com/javascript-validator.php">beautify tools</a>

The only errors airsing from the JS tetsing indicate that i am using ES6, however i have chosen to es6 as it improves my code.

My version control relied on creating duplicates locally on my hard-drive. Unfortunately, I was unable to use git. I thought the only way to control my versions was by using GitPod. However, was unable to access GitPod so I relied Visual Studio Code. In my attempt to use version control via Visual Studio Code the terminal returned an error stating that an origin already exists for this repository. Despite numerous searching around the internet to fix this bug, I was unable to do so. Therefore, I had no choice but to create duplicates locally whenever significant changes where made.

1.	As someone who regularly enjoys making cocktails, I’d like to broaden my scope of drinks to make. So, I would like there to be a well -presented range of drinks, easily viewable and navigable.
    - The layout of the cocktails on the cards allows the user to dynamically interact with the drinks that are presented on the cards. Due to the number of cocktails on the page, there is an overlay on the drinks section, to ***


2.	As someone who rarely makes cocktails, rather buys them, I’d like to know how to make some of my favourite cocktails at home. So, I would like to get an appropriate amount of information regarding the ingredients, quantity and direction.
    - The hover-over effect allows the user to learn more about the cocktail that they choose, rather than being overwhelmed with information about every cocktail on the site. The front of each card provides the name and picture of the drink, while the back details the ingredients, method and rating. 

3.	As an infrequent drinker, I’m curious to find a cocktail that would be to my taste. So, I would like there to be a sufficient search function that allows me to browse the cocktails meticulously, or a function that suggests a cocktail for me.
     - The search function allows the user to search in-depth to discover a cocktail that they like. If there nothing matches their search, they will be notified. If for example the user wanted to search for a cocktail by name but wasn’t sure of the spelling, the X function, makes the search easier and makes it more likely for them to find the cocktail that they are looking for. If the user doesn’t know what they are looking for, the lucky dip function randomly selects a cocktail from the array to provide some inspiration for the user.  


The testing process intended to ensure that website was fulfilling the needs of the user. After running through the entire website checking links, anchors, the search bar (for positive and negative results), the random generator, website compatibility and responsiveness, it is deducible that it functions as intended. The user stories mentioned in the UX section have been tested and proven success. All data fetched from the data has been received and presented as intended.

1.	Search bar
     2. Type in a search that does not match an item in the array, you are presented with a message informing that there were no results matching the values entered. 
     3. Start typing some letters into the search bar, and every matching result with the same values will be presented, as well of the number of matches that are returned. 

All links provided on the website have been coded with 'target="_blank"' so that the user can maintain their position on the website, whilst exploring the link's destination in a new tab. These have been tested and proven to work efficiently. The anchor tags surrounding the 'home', 'drinks', ‘lucky dip' and ‘links’, are fully functioning and allow the user to skip to their desired section. 

With thanks to Flexbox’s framework, the website has been tested and is successfully responsive to different screen sizes, and the elements on the page wrap accordingly and appropriately. The tested mobile devices were iPhone model 5 through to iPhone 8, Galaxy S5, pixel and pixel XL. 


### DEPLOYMENT
This project has been deployed from the master branch to the hosting platform, GitPages. To run locally, copy the following link into an editor: https://github.com/AnnaRaman/milestone2.git.
Deployment
GitHub Pages
The project was deployed to GitHub Pages using the following steps:
1.	Log in to GitHub and locate the GitHub Repository
2.	At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3.	Scroll down the Settings page until you locate the "GitHub Pages" Section.
4.	Under "Source", click the dropdown called "None" and select "Master Branch".
5.	The page will automatically refresh.
6.	Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.
Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

    1.	Log in to GitHub and locate the GitHub Repository
    2.	At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
    3.	You should now have a copy of the original repository in your GitHub account.


Making a Local Clone
1.	Log in to GitHub and locate the GitHub Repository
2.	Under the repository name, click "Clone or download".
3.	To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4.	Open Git Bash
5.	Change the current working directory to the location where you want the cloned directory to be made.
6.	Type git clone, and then paste the URL you copied in Step 3.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
7.	Press Enter. Your local clone will be created.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
Click Here to retrieve pictures for some of the buttons and more detailed explanations of the above process.


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