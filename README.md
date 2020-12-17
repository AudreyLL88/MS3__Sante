# Santé! #
---
![Hero Screenshot]

## Contents ##
---

* UX
    * [Project Goals](#project-goals)
    * [User Stories](#user-stories)
    * [Design Choices](#design-choices)
        * [Fonts](#fonts)
        * [Icons](#icons)
        * [Colors](#colors)
* [Wireframing](#wireframing)
* [Features](#features)
    * [Features that have been developed](#developed)
    * [Features that will be implemented in the future](#implemented)
* [Technologies](#technologies)
* [Defensive Design](#defensive)
    * [Feature Testing](#ftest)
    * [Defensive Design Testing](#dtest)
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

* As an admin of Santé! I want all of the above options but I would also be able to access and delete all the recipes from other users.
* As an admin of Santé! I want to be able to create, edit and delete cocktail categories.

<a name="requirements"></a>

### Research ###

* To create Santé! I researched several popular Food and Beverages websites such as [**Epicurious**](https://www.epicurious.com/), [**Delish**](https://www.delish.com/) and [**Cocktail Flow**](https://cocktailflow.com/).
* I also checked which website had the most interesting cocktail recipes (classics and originals) and my choice went to:
* Most of these websites usually include a story around the cocktail and I decided to turn it only in a small description as I as a user usually skip most of the text and prefer to have the ingredients right away. I did a small poll among my friends on **Instagram** about the Story vs. No Story topic on recipe website and results showed 89% (on 145 people) in favor of No Story. The people have spoken, No story it is.

<a name="design-choices"></a>

### Design Choices ##
---

<a name="framework"></a>

### Frameworks ###

* Bootstrap 4. I used the [**Small Business Template**](https://startbootstrap.com/template/small-business) for the landing page structure as well as the [**Business Template**](https://startbootstrap.com/template/business-frontpage) for the profile page. I wanted to learn more about Bootstrap and its classes. I tried to implement these as much as possible.
* [**Flask**](https://flask.palletsprojects.com/en/1.1.x/)

<a name="fonts"></a>

### Fonts ###

* For the titles and the website logo I decided to go for the [**Goggle Fonts**](https://fonts.google.com/) cursive "Lobster" for a playful and sophisticated look and paired it with my all-time favourite sans-serif Google fonts 'Montserrat' for readability on all other elements.

<a name="icons"></a>

### Icons and Images ###

* All icons used on this website are taken from [**Font Awesome**](https://fontawesome.com/).
* I have decided to choose icons for the buttons Edit/View/Delete on the cocktail cards in the profile and in recipe template for a better user understanding.


<a name="colors"></a>

### Colors ###

* I choose to work with a very momocromatic color scheme of light and dark yellows. 
* I choose yellow because it is a color that increase cheerfulness and stimulate the user mentally. This website is all about a positive and fun message in these pretty dark times, and I thought yellow was the right amount of playfulness.
* The buttons have their own color code: Red for all delete functionnalities, Green for all Edit functionnalities, Yellow for the Add functionnalities as well as the View cocktail buttons. Only the admin has a blue "Add Category" button as this is a functionnality only the Admin has.
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

* The navigation bar is completely responsive and is not made with Bootstrap as this is part of a [**Youtube tutorial by Bedimcode**](https://www.youtube.com/watch?v=Lf6zONwYeec).
* The Navigation Bar displays the logo of the website and the options "Home", "Cocktail Recipes", "Log In" and "Register" when the user is not logged in.

**Animated landing page**

* For this feature I coded along and adapted this [**Youtube tutorial by Bedimcode**](https://www.youtube.com/watch?v=Lf6zONwYeec). I made my own elements to animate using [**Maya**](). You can see in my CSS/HTML/JS files that I have credited the owner of the tutorial as well as I've left the CSS and SASS classes  as they are in the tutorial.
* I wanted to implement this feature because I wanted to learn a bit more about the GSAP library and I really enjoyed coding along this tutorial.

**It's Apero Time**

* This feature is a pretty straightforward section of the website explaining the goal and concept of Santé!. 
* I added a Bootstrap carousel that display images on demand or automatically to for a visually more engaging user experience.

**Newsletter**

* This feature allows the user, no matter if he is registered or not, to subscribe to the website's newsletter. The email given by the user is registered in the database in a collection called "subscriptions" and is separate from the "users" collection.

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
    - Cocktail Level 
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
    - The user's location,
    - The user's level.
* The passwords  are hashed and protected using the import "generate_password_hash, check_password_hash" from werkzeug security.
* As Santé! is promoting alcohol beverages, the user must confirm that he/she/is over 18.

**Log In**

* When a user is already registered, he/she/them uses the log in form to access their account. The user needs their password and username to log in.

*Features visible for registered users*

**Navigation bar**

* The navigation bar is completely responsive.
* The Navigation Bar displays the logo of the website and the options "Home", "Cocktail Recipes", "Profile" and "Log Out" when the user is not logged in.

**Profile**

* The user's profile showcases their personal informations: username, profile picture, level and location.
* The section "Your cocktails" displays the cocktail recipes submitted by the user. The user can also create a recipe by clicking on a specified button next to the recipe cards.
* Each recipe card has 3 buttons : View, Edit, Delete.

**Edit Profile**

* The user can edit their profile informations by clicking on the green "Edit" button in the dedicated profile card.
* This feature allows the user to edit their picture, level and location. The user cannot edit their username and password (yet)
* The user needs to click on the yellow "Submit" button to edit the changes.
* After clicking on the button the user will be redirected towards their updated profile page with an alert confirming the changes made.

**Delete Profile**

* The user can delete their profile by clicking on the red "Delete" button in the dedicated profile card.
* This feature allows the user to permanently delete their profile.
* When the button is clicked a modal will ask for confirmation to avoid any unfortunate mistake to be made.
* If the confirmation button is clicked, the profile is permanently deleted and the now guest user will be redirected to the registration page with an alert confirming the changes.

**Add a Cocktail**

* This feature allows the user to submit a custom recipe through a form including the following required blank fields and options:
    - Cocktail name (blank)
    - Category (option)
    - Cocktail Description (blank)
    - Cocktail Image (blank)
    - Cocktail Image Credentials (blank)
    - Cocktail Preparation Time (option)
    - Cocktail Level (option)
    - Cocktail Ingredients (blank)
    - Cocktail Instructions (blank)

* After clicking on the submit button, the user can see the new recipe page topped with a validation flash message. The recipe will then appear in the user's profile.
* This feature is accessible through the navigation bar and the user's profile.

**Edit a Cocktail**

* The user can edit the choosen recipe only when logged in.
* The form passes the informations previously submitted for more clarity and can all be changed.
* To submit these new information, the user needs to click on the "submit" button at the bottom of the page.
* After clicking on the submit button, the user can see the updated recipe page topped with a validation flash message. The recipe will be updated in the user's profile.
* The edit  functionnality can be accessed through the recipe cards on the cocktails.html page, profile.html and the specific cocktail/cocktail_id.html.

**Delete a Cocktail**

* The user can delete the choosen recipe only when logged in.
* The delete functionnality can be accessed through the recipe cards on the cocktails.html page, profile.html and the specific cocktail/cocktail_id.html.
* When the delete button is clicked, a modal asks confirmation to prevent the user from accidentally deleting the recipe.
* If confirmed, the recipe is deleted forever.

**Like a Cocktail**

* The user can only like a recipe when logged in.
* The user can only like a recipe once.
* When clicked the recipe page reloads and adds to the like count.
* A message on top of the recipe confirms the "like" to the user.

**Log Out**

* The user can access this functionnality through the navigation bar.
* When clicked, a modal appears and ask for confirmation.
* If confirmed, the user is redirected towards the landing page with an alert confirming that the user is logged out.

*Features only for the admin (all of the above plus the following)*

**Manage Categories**

* The admin can edit, delete and view all cocktail categories through buttons displayed on the category cards.
* The admin can access the Categories through their profile.

**Add Category**

* This feature allows the admin  to Add a category to the "Manage Category" dashboard.
* This feature can be accessed by clicking on the blue "Add category" button on the admin profile page.

**Profile**

* All recipes are displayed on the admin dashboard.
* The admin can view and delete any of the recipe. 
* The admin cannot edit a recipe.
* The admin can edit their profile information like a registered user.

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


<a name="defensive"></a>

## Defensive Design  ##
---
### Feature Testing ###
---
<a name="ftest"></a>

**Responsiveness**
 

* 

**GSAP Animation and Navigation Bar**

![GSAP]()

*  


**Featured Cocktails**

![featured]()

* 

**All Cocktails**

![all]()

* 

**Cocktail Recipe**

![recipe]

* 

**Search box**

![search]() 

* 

**Log In and Profile**

![login]()

* If the user is already registered, access the Login page through the navigation bar.
* Is the login form and background correctly rendered ?
* Try to submit an empty form. Is the bootstrap form validation tooltip shows in the empty fields?
* Try to fill the fields with a password and username under 5 characters or above 15 characters. Is the Bootstrap form validation tooltip showing in the incorrectly filled fields?
* Try to fill the form with a wrong password/username. Is an alert informing you that your password/username is incorrect?
* Fill the form with correct password/username. Is your profile page displayed correctly ?
* Is your profile card displaying your profile picture, username, level and location ?
* Is the dashboard correctly displaying the "Your cocktails" with its content and "Add cocktail" sections?
* Click on the green "Edit Profile" button. Is the Edit Profile template rendered correctly ?
* Make one change in one of the fields and click submit. Are you redirected towards your profile page?
* Is the alert present ?
* Is the change made in your profile displayed ?
* Click the red "Delete profile". Is the modal rendered? 
* Click the "Cancel" modal button. Are you back on your profile page?
* Reclick on "Delete Profile". On the modal, click the "Delete" button. Is the register page rendered?
* Is the delete alert present?

**Register**

![register]()

* Navigate to the Register page through the navigation bar and click. Is the registration form and its background correctly rendered?
* Try to submit an empty form. Is the bootstrap form validation tooltip shows in the empty fields?
* Try to fill the fields with a password and username under 5 characters or above 15 characters. Is the Bootstrap form validation tooltip showing in the incorrectly filled fields?
* Try to fill the form with an already existing username. Is an alert informing you that the username already exists?
* Fill the form correctly and click on the "Register" button. Is the Profile page correctly rendered ?
* Is the "Your cocktail" section empty?

**Your cocktails**

![profile]()

* In your profile page, is the "Your cocktail" section displayed?
* If you haven't submitted any recipe yet, is the message "Wow, such empty." showing ?
* As a registered user, if you have submitted recipe previously, are the cocktail cards showing ?
* Are the buttons "View"(yellow), "Edit"(green), and "Delete"(red) displayed ?
* Is the picture, name and category of the cocktal showing ?
* As an admin, are your cocktails as well as all registered user cocktails showing in "Your cocktail" section?
* As an admin, do you haven "View","Edit" and "Delete" buttons on your recipes and "View" and "Delete" buttons for other users recipes?

**Submit a cocktail (Admin/Registered user)**

![submit]()

* Navigate to the form through your profile page. Is the yellow button "Add a cocktail" rendered ?
* Click on the button, is the "Add a cocktail" form correctly ?
* Are all fields empty, except for the option fields?
* Try to submit the form with empty fields. Is the Bootstrap form validation tooltip showing ?
* Fill the form accordingly and respecting the instruction. Click on the submit button. Is the cocktail page rendered correctly?
* Is the alert present ?

**Edit a cocktail**

![Edit]()

* 

**Delete a cocktail**

![delete]()

* 

**Manage Category**

![manage]()

* 

**Rate a cocktail**

![rate]()

* 

**Share a cocktail**

![submit]()

* 

<a name="dtest"></a>
### Defensive Design Testing ###

**Register and Log In**

* If any field is left empty after the button is clicked, the form will request a valid entry.
* It is impossible to register or log in without filling all the fields.
* If the username already exists, the message "username already exists" will appear to prevent duplication.
* All usernames and passwords must be minimum 5 characters or the form will require the user a valid entry.
* In Log In specifically, if the user submit with the wrong password or username, the message "Incorrect password/username" will appear on the page.

**Category**

* Only the admin can access the category pages :
    - categories.html
    - add_category.html
    - edit_category.html
* When a guest user and/or a registered user try to access the pages by typing the url, they are redirected to the "Login" page.

**Like a cocktail**

* Only registered users can like a cocktail. a message "register/login to vote" appears if the user is not logged in/registered.
* The registered user can only like a cocktail once. After visual confimation that the user voted, the Like button is not clickable anymore.

**Cocktail Recipes**

* Only registered users can access these pages:
    - add_cocktail.html
    - edit_cocktail.html

* When a guest user and/or a registered user try to access the pages by typing the url, they are directed to the login page.

**Delete Profile/Cocktail/Category**

* The registered user/admin cannot delete any of these features without confirming it before on the defensive modal.

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
* Create an environement file called ".env" and add :
    - MONGO_URI=mongodb+srv://...
    - SECRET_KEY=MyLittleSecret
* Add your .env to .gitignore. to avoid it being uploaded.
* In app.py, switch **debug=False** to **debug=True**
* Upgrade pip locally with the command "pip install -U pip".
* Install the modules used to run the application using "pip -r requirement.txt" in your terminal.
* In parallel, create a MongoDB account and create a database called **"sante_project"**.
* Add the following collections in the new database:

***categories***
```
_id:<ObjectId>
category_name:<string>
```
***subscriptions***
```
_id:<ObjectId>
sub_email:<string>
```

***users***
```
_id:<ObjectId>
username:<string>
password:<string>
```

***cocktails***
```
_id:<ObjectId>
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
* You can now run your application locally by typing the command "python3 app.py" in your terminal.

## Deploying on Heroku<hr>

- Create a requirements.txt file using the command **pip3 freeze --local > requirements.txt** in your CLI.
- Create a Procfile (always with an uppercase P) through the command **echo web: python app.py > Procfile**. Commit and Push.
- Create an account on [**Heroku**](https://www.heroku.com/home).
- Create a new app with **unique name**.
- Select your **nearest region**.
- Create a **new python project** within the project.
- Link that project through your **Github repository** in the **deployment** section.
- Navigate to Haroku Settings and set up the following in **Config Vars**

```
_IP = 0.0.0.0
MONGO_DBNAME = [Name of DB]
MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
PORT = 5000
SECRET_KEY = [Your Secret key]

```
* Go back to the Deploy section, select the master branch and deploy the project. 


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