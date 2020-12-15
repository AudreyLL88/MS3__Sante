# Santé! #
---
![Hero Screenshot]

## Contents ##
---

* UX
    * [Project Goals](#project-goals)
    * [User Stories](#user-stories)
    * [User Requirements and Expectations](#requirements)
    * [Design Choices](#design-choices)
        * [Fonts](#fonts)
        * [Icons](#icons)
        * [Colors](#colors)
* [Wireframing](#wireframing)
* [Features](#features)
    * [Features that have been developed](#developed)
    * [Features that will be implemented in the future](#implemented)
* [Technologies](#technologies)
* [Testing](#testing)
* [Issues](#issues)
* [Deployment](#deployment)
* [Credit](#credits)

## UX (User Experience) ##
---
<a name="project-goals"></a>
### Project Goals ###

* Santé! is a collaborative platform where registered users can share cocktail recipes from all around the world, discover new cocktails and upgrade their knowledge and skills about mixology.
* Santé! is also accessible to guest users without to possibility to post their own recipe or "like" a cocktail recipe.


<a name="user-stories"></a>
### User Stories ### 

Guest user

* As a guest user of Santé! I want to find this website when I search for cocktail recipes.
* As a guest user of Santé! I want to browse and understand the concept of the website easily.
* As a guest user of Santé! I want to be able to access this website from different devices easily.
* As a guest user of Santé! I want be entertained and discover/search for new cocktail recipes.
* As a guest user of Santé! I want to find out more about the website on social media.
* As a guest user of Santé! I want to see the popularity of the cocktail recipes.
* As a guest user of Santé! I want to suscribe to the newsletter.
* As a guest user of Santé! I want the clear possibility to register to the website.

Registered user

* As a registered user of Santé! I want be able to log in with my username and password.
* As a registered user of Santé! I want to get a visual confirmation when I am logged in.
* As a registered user of Santé! I want to be able to create and add cocktail recipes to the website.
* As a registered user of Santé! I want to get a visual confirmation when I added a recipe.
* As a registered user of Santé! I want to be able to search for specific recipes.
* As a registered user of Santé! I want to be able to "like" a cocktail recipe.
* As a registered user of Santé! I want to be able to edit my cocktail recipes.
* As a registered user of Santé! I want to get a visual confirmation when I edited my cocktail
* As a registered user of Santé! I want to be able to delete my cocktail recipes.
* As a registered user of Santé! I want to see who has published a cocktail recipe that isn't mine.
* As a registered user of Santé! I want to be able to add a picture and relevant informations to my profile.
* As a registered user of Santé! I want to be able to delete my profile.

Admin

* As an admin of Santé! I want all of the above options but I would also be able to access and delete all the recipes from other users, as well as their profile.

<a name="requirements"></a>

### Research ###

* To create Santé! I researched several popular Food and Beverages websites such as [**Epicurious**](https://www.epicurious.com/), [**Delish**](https://www.delish.com/) and [**Cocktail Flow**](https://cocktailflow.com/).
* I also checked which website had the most interesting cocktail recipes (classics and originals) and my choice went to:
* Most of these websites usually include a story around the cocktail and I decided to turn it only in a small description as I as a user usually skip most of the text and prefer to have the ingredients right away.

<a name="design-choices"></a>

### Design Choices ##
---

<a name="framework"></a>

### Frameworks ###

* Bootstrap 4. I used the [**Small Business Template**](https://startbootstrap.com/template/small-business) for the landing page structure as well as the [**Business Template**](https://startbootstrap.com/template/business-frontpage) for the profile page.
* [**Flask**](https://flask.palletsprojects.com/en/1.1.x/)
* [**GSAP**](https://greensock.com/gsap/)

<a name="fonts"></a>

### Fonts ###

* For the titles and the website logo I decided to go for the [**Goggle Fonts**](https://fonts.google.com/) cursive "Lobster" for a playful and sophisticated look and paired it my all-time favourite sans-serif Google fonts 'Montserrat' for readability.

<a name="icons"></a>

### Icons and Images ###

* All icons used on this website are taken from [**Font Awesome**](https://fontawesome.com/).
* I have decided to choose icons for the buttons Edit/View/Delete on the cocktail cards in the profile and in the instructions field of the recipe template.

<a name="colors"></a>

### Colors ###

* I choose to work with a very momocromatic color scheme of light and dark yellows. 
* I choose yellow because it is a color that increase cheerfulness and stimulate the user mentally. This website is all about a positive and fun message in these pretty dark times, and I thought yellow was the right amount of playfulness.
![Color Scheme]() 


<a name="wireframing"></a>

## Wireframing ##
---
For **wireframing** I used the tool [**Balsamiq**](https://balsamiq.com/).

View my wireframes [here]().

* 
<a name="features"></a>
## Features ## 
---

<a name="developed"></a>
### Implemented Features ###

*Features for all users (guest/registered/admin)*

**Navigation bar**

* The navigation bar is completely responsive.
* The Navigation Bar displays the logo of the website and the options "Home", "Cocktail Recipes", "Log In" and "Register" when the user is not logged in.

**Animated landing page**

* For this feature I coded along and adapted this [**Youtube tutorial by Bedimcode**](https://www.youtube.com/watch?v=Lf6zONwYeec). I made my own elements to animate using [**Maya**](). You can see in my CSS/HTML/JS files that I have credited the owner of the tutorial as well as I've left the CSS and SASS classes  as they are in the tutorial.
* I wanted to implement this feature because I wanted to learn a bit more about the GSAP library and I really enjoyed coding along this tutorial.

**It's Apero Time**

* This feature is a pretty straightforward section of the website explaining the goal and concept of Santé!. 
* I added a Bootstrap carousel that display images on demand or automatically to for a visually more engaging user experience.

**Newsletter**

* This feature allows the user no matter if he is registered or not to subscribe to the website's newsletter. The email given by the user is registered in the database in a collection called "subscriptions" and is separate from users.

**Featured Recipes**

* This feature is an introduction to some of the cocktail recipes showcased on the website and are cocktail recipes created in the database by the admin only.

**Cocktail Recipes**

* The recipe page showcases all the recipes submitted by the registered users and the admin. All recipes are displayed in responsive cards including a picture, a category, a short description and a name all submitted by the user/author of the recipe.
* If the user is the author of the recipe or the admin and is logged in, the buttons "edit and "delete" appears. They are not visbible if the author or admin is not logged in.

**Search box**

* This feature allows the user to search through keywords specific cocktails in the Cocktails.html.
* When no results match the search, the text "No Result Found" is displayed.


**Individual Recipe Page**

* This page allows the user to view a custom recipe including
    - Cocktail Name 
    - Category Name
    - Cocktail Description 
    - Cocktail Image 
    - Cocktail Image Credentials 
    - Cocktail Preparation Time 
    - Cocktail Difficulty 
    - Cocktail Ingredients 
    - Cocktail Instructions
    - Cocktail Date Submission
    - Cocktail Likes
    - Cocktail Author's Name

* The user needs to be registered to "like" a recipe


**Register**

* The registration form takes the informations of the user to create an account : 
    - the user's email address,
    - The user's username,
    - The user's password,
    - The user's picture,
    - The user's description.
* The passwords  are hashed and protected using the import "generate_password_hash, check_password_hash" from werkzeug security.
* As Santé! is promoting alcohol beverages, the user must confirm that he/she/is over 18.

**Log In**

* When a user is already registered, he/she/them uses the log in form to access their account. The user needs their password and username to log in.

*Features visible for registered users*

**Navigation bar**

* The navigation bar is completely responsive.
* The Navigation Bar displays the logo of the website and the options "Home", "Cocktail Recipes", "Profile" and "Log Out" when the user is not logged in.

**Profile**

* The user's profile showcases their personal informations.
* The section "Your cocktails" displays the cocktail recipes submitted by the user. The user can also create a recipe by clicking on a specified button next to the recipe cards.
* Each recipe card has 3 buttons : View, Edit, Delete.


**Add a Cocktail**

* This feature allows the user to submit a custom recipe through a form including the following required blank fields and options:
    - Cocktail name (blank)
    - Category (option)
    - Cocktail Description (blank)
    - Cocktail Image (blank)
    - Cocktail Image Credentials (blank)
    - Cocktail Preparation Time (blank)
    - Cocktail Difficulty (option)
    - Cocktail Ingredients (blank)
    - Cocktail Instructions (blank)

* After clicking on the submit button, the user can see the new recipe page topped with a validation flash message. The recipe will then appear in the user's profile.
*This feature is accessible through the navigation bar and the user's profile.

**Edit a Cocktail**

* The user can edit the choosen recipe only when logged in.
* The form passes the informations previously submitted for more clarity and can all be changed.
* To submit these new information, the user needs to click on the "submit" button at the bottom of the page.
* The edit  functionnality can be accessed through the recipe cards on the cocktails.html page, profile.html and the specific cocktail/cocktail_id.html.

**Delete a Cocktail**

* The user can delete the choosen recipe only when logged in.
* The delete functionnality can be accessed through the recipe cards on the cocktails.html page, profile.html and the specific cocktail/cocktail_id.html.
*  When the delete button is clicked, it throws a modal asking confirmation to prevent the user from accidentally delenting the recipe.
* If confirmed, tge recipe is deleted forever.

**Like a Cocktail**

* The user can only like a recipe when logged in.
* The user can only like a recipe once.
* When clicked the recipe page reloads and adds to the like count.
* A message on top of the recipe confirms the "like" to the user.

**Log Out**

* The user can access this functionnality through the navigation bar.
* When clicked, a modal appears and ask for confirmation.
* If confirmed, the user is redirected towards the landing page.

*Features only for the admin (all of the above plus the following)*

**Manage Categories**

* The admin can edit, delete and view all cocktail categories through buttons displayed on the category cards.
* The admin can access the Categories through their profile.

**Profile**

* All recipes are displayed on the admin dashboard.
* The admin can view and delete any of the recipe. 
* The admin cannot edit a recipe.

<a name="implemented"></a>
### Future implemented features ###

<a name="technologies"></a>
## Technologies, libraries and tools used ##

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Bootstrap](https://bootstrap4.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
* [Heroku](https://dashboard.heroku.com/)
* [MongoDB](https://www.mongodb.com/1)
* [Font-Awesome](https://fontawesome.com/)
* [Google fonts](https://fonts.google.com/)
* [Git](https://git-scm.com/)
* [Maya](https://www.autodesk.com/products/maya/overview)
* [GSAP](https://greensock.com/gsap/)
* [SCSS](https://sass-lang.com/)
* [W3C HTML Validator](https://validator.w3.org/)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* [PEP8 online](http://pep8online.com/)
* [JSHint](https://jshint.com/)


<a name="testing"></a>

## Feature Testing ##
---
![Testing]()

* 

**Responsiveness**

* **Implementation** 

* 

**GSAP Animation**

![GSAP]()

* **Implementation** 

* 

**Featured Cocktails**

![featured]()

* **Implementation** 

* 

**All Cocktails**

![all]()

* **Implementation**

* 

**Cocktail Recipe**

![recipe]

* **Implementation**

* 

**Search bar**

![search]() 

* **Implementation**

* 

**Log In**

![login]()

* **Implementation**

* 

**Register**

![register]()

* **Implementation**

* 

**Profile**

![profile]()

* **Implementation**

* 

**Submit a cocktail**

![submit]()

* **Implementation**

* 

**Edit a cocktail**

![submit]()

* **Implementation**

* 

**Delete a cocktail**

![delete]()

* **Implementation**

* 

**Manage Category**

![manage]()

* **Implementation**

* 

**Rate a cocktail**

![rate]()

* **Implementation**

* 

**Share a cocktail**

![submit]()

* **Implementation**

* 

<a name="issues"></a>
## Issues ##
---

**During development**

* 



# Deployment<hr>

***Requirements to deploy:***

- An IDE: I used Gitpod but will use a IDE that is not online for my next project. I choose Gitpod as this is the recommended IDE at Code Institute.
- Python3: In order to to run the application and use Flask.
- PIP3: To install all application imports (such as Flask and OS).
- A template folder: To link with the app routes.
- A database: I choose MongoDB Atlas. 


## Local Deployment<hr>

* Open browser od choice.
* Copy/Paste the address of [**Santé! repository**](https://github.com/AudreyLL88/MS3__Sante) in your search box.
* When on the page, click on the "Code" button.
* Copy the the |**HTTPS link**](https://github.com/AudreyLL88/MS3__Sante.git).
* Open your IDE and in your terminal, type "git clone" and paste the [**HTTPS Link**](https://github.com/AudreyLL88/MS3__Sante.git).
* Create an environement file called ".flaskenv" and add :
    - FLASK_APP=run.py 
    - FLASK_ENV=development
* Install the modules used to run the application using "pip -r requirement.txt" in your terminal.
* In parallel, create a MongoDB account and create a database called **"sante_project"**.
* Add the following collections in the new database:

***categories***
```
_id:<ObjectId>
category_name:<string>
```

***users***
```
_id:<ObjectId>
username:<string>
password:<string>
```

***cocktails***
```
_id:5fd7340324e59fddee695828
category_name:<string>
cocktail_name:<string>
cocktail_description:<string>
cocktail_img:<string>
cocktail_ingredients:<string>
cocktail_instructions:<string>
cocktail_prep: <decimal128>
cocktail_diff:<string>
cocktail_serv:<decimal128>
cocktail_img_cred:<string>
created_by:<string>
cocktail_like:<Array>
```


## Deploying on Heroku<hr>
- 


<a name="credits"></a>
## Credits ##
---

**Text Credits:**

* 

**Image Credits:**

* 

**Many thanks to:**

* My mentor **Ignatius Ukwuoma** for his patience and kindness
* **Kasia** for her very inspiring ReadME
* **Code Institute Slack community** for the technical and emotional support
* **Ivar Dahlberg**, for all the beautiful designs he created and his assistance
* **Mesaicos Stockholm LandHockey team** for cutting me some slack for not being very alert (and I am the goalkeeper...)

**Site for educational purposes only!** (for now)