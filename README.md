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
Features for all users (guest/registered/admin)

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

**Recipes**

* The recipe page showcases all the recipes submitted by the registered users and the admin. All recipes are displayed in responsive cards including a picture 

<a name="developed"></a>
### Implemented Features ###



* 
<a name="implemented"></a>
### Future implemented features ###

* 


<a name="technologies"></a>
## Technologies used ##

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Javascript]()
* [Python]()


**Tools & Libraries**

* [Bootstrap](https://getbootstrap.com/)
* [Font-Awesome](https://fontawesome.com/icons?d=gallery)
* [Google fonts](https://fonts.google.com/)
* [Git](https://git-scm.com/)
* 
* 

<a name="testing"></a>

## Testing ##
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
***Requirements:***
- 


## Local Deployment<hr>
- 

- 

***categories***
```
_id:<ObjectId>
category_name:<string>
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