# MS4---London Music Exchange!
Fourth Milestone Project for Code Institute

 <!-- ![](static/images/devices.PNG) -->

I wanted to design an ecommerce website for users to be able to purchase guitars and other guitar related equipment. I used postgres for the database and I used Django to facilitate building the bulk of the website with templates.

[The live project can be viewed here.](https://ms4--london-music-exchange.herokuapp.com/)

---
# Contents
- [UX](#ux)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Special Thanks](#special-thanks)
---

# UX
## User Stories
- User goals 
    - As a user, I want to immediately understand what is offered by the website
    - As a user, I want to be able to seamlessly navigate through the site to easily find
     more information
    - As a user, I want to be able to easily interact with the site and the applications within
    - As a user, I want to be able to view all the products that are uploaded
    - As a user, I want to be able to sign up so that I can make future purchases easily
    - As a user, I want to be able to edit/update/delete my own recipes

    <!-- I made the wireframe using Balsamiq which you can view the wireframe [here.](static/images/wireframe.png) -->

## Design Choices
---
When designing this website, I looked at existing ecommerce sites such as 
[this one for Guitar Village](https://guitarvillage.co.uk/) 
for inspiration. I opted for a multi-page website with certain pages only being accessible if a registered user is logged in.

## Fonts
I chose [Lato](https://fonts.google.com/specimen/Lato) 
for my main font for its' excellent readability and clean look.

## Icons
I used [Font Awesome](https://fontawesome.com/) for my form icons as well as my button icons.

## Colours
I used [this colour scheme](https://www.canva.com/colors/color-palettes/mountain-haze/) for inspiration and chose these two for my main colours. 
[](/media/hex.png)

# Features
- Responsive on all device sizes
- Ability to sign up and become a registered user
- CRUD Functionality
- Postgres database linked to the website
- Hashed passwords for user security
- Admin privileges to edit/delete any products/blogs/reviews/users

## Future Features
Due to time constraints, I was unable to implement these features but will include them in the future:
- Modal popup to confirm product/review/blog deletion 
- Coupon model to handle discounts at checkout
- Ability to search through blogs by date posted/blog author

# Technologies used
## Languages used
- [HTML5](https://en.wikipedia.org/wiki/HTML)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://www.python.org/)
- [JavaScript](https://www.javascript.com/)

## Tools, Frameworks and Libraries used
- [Git](https://git-scm.com/) 
    - Git was used for version control, using the Terminal to commit and push to GitHub.
- [Font Awesome](https://fontawesome.com/)
    - Font Awesome was used for better UX and aesthetics.
- [Bootstrap](https://getbootstrap.com/)
    - Bootstrap was used to aid with prebuilt classes and the responsiveness of the website across multiple devices.
- [JQuery](https://jquery.com/)
    - JQuery was used in conjunction with the respective Bootstrap elements for responsiveness and to handle various form submits
    including Stripe payment.
- [Django](https://www.djangoproject.com/)
    - Django was used to easily create a multi page website through the use of templates.
- [MySQL](https://www.mysql.com/)
    - MySQL was used to create the database in Django before moving to Postgres on Heroku
- [Postgres](https://www.postgresql.org/)
    - Postgres was used as a database to store a collection of users, products, reviews, blogs, orders and categories.
- [Heroku](https://www.heroku.com/)
    - Heroku was used to host the website.
- [Google Fonts](https://fonts.google.com/)
    - Google Fonts were used to import the Lato font family into the style.css file. 
- [Balsamiq](https://balsamiq.com/) 
    - Balsamiq was used to create the wireframes for the project.

# Testing
I used the [CSS Validator](https://jigsaw.w3.org/css-validator/) which brought no warnings or errors. 
I also used the [HTML Validator](https://validator.w3.org/) which brought up 1 error and 2 warnings which can be seen [here.](media/HTML_Errors.PNG) I fixed the error by replacing the duplicate id of "user-options" in the mobile-top-header template with "mobile-user-options". This also removed one of the warnings as well, I have left the other warning as it is not applicable.

Python code passed the [PEP8](http://pep8online.com/) compliance test

## Testing User Stories from UX 
1. As a user, I want to immediately understand what is offered by the website

    1. Upon entering the website, the user is greeted with an appropriate hero image, a call-to-action button 
    and a navbar with 5 options to go to anywhere on the website as well as a search bar at the top of the page.
    2. The user is also presented with a card panel with two buttons, one with a dropdown menu to enable them to register/login
    and another to take them to their shopping bag.
    3. The user has multiple options, they can either select a link from the navbar, utilise the call-to-action button, or use 
    the search bar

2. As a user, I want to be able to seamlessly navigate through the site to easily find more information

    1. The site has a fixed navbar so the user can always navigate wherever they want to go

3. As a user, I want to be able to easily interact with the site and the applications within

    1. The user is presented with a simple register and log in template
    2. The product templates have a number of ways of sorting (by price, name, rating etc)
    3. The product detail template has intuitive buttons for the user to increase quantity and add to bag

## Further Testing 
- The project was tested on Google Chrome, Mozilla Firefox, Safari for iOS and Microsoft Edge.
- The project was viewed on a variety of different devices such as Desktop, Laptop, iPhone 7, iPhone 8, iPhone 11, and iPad.
- I asked friends and family to view the project and give feedback on any user experience issues and/or bugs. 

# Bugs
Following on from Testing I also encountered these bugs.
## During development



# Deployment

**London Music Exchange** was developed on **Gitpod**, using **GitHub** to host the repository, **MySQL** to 
initially develop the database before moving to **Postgres** and finally deployed via **Heroku**. **AWS** was used to 
host the static/media files.
These were the steps taken to successfully deploy the website.
- First, open up your **IDE** of preference, open the **terminal** window and type: ``pip3 freeze -- local > requirements.txt.``
- Also in terminal window of your IDE type: ``python app.py > Procfile``
    - These two files are needed for Heroku to see which files to install (**requirements.txt**) and which file is used as the 
    entry point (**Procfile**)
- You need to set up a Heroku account if you have not done so already and select **create a new app** from the **New** dropdown 
button, after which you will be prompted to give a name to your app and select your region.
- Click on the **Deploy** tab and select the **Connect to GitHub** icon
- Underneath that you will be able to search for your repository and then click the **Connect** button once you have selected it
- Scroll back up and click on the tab named **Settings** and then the button named **Reveal Config Vars**
    - You will now need to enter all the variables and their values contained in your `env.py` file i.e.
    (**SECRET_KEY, STRIPE_SECRET_KEY, USE_AWS** etc)
- You will need to set up an AWS account and a bucket in S3.
    - Make sure public access is NOT blocked
    - Add security policy
    - Create a user to access the bucket
    - Add user to a group
- In Heroku ensure all config vars from AWS/Stripe etc are included
- Go back to your **IDE** and add, commit and push both the `Procfile` and the `requirements.txt` to your repository
- Now return to the **Deploy** tab in Heroku and click on **Enable Automatic Deployment**
- Underneath that under **Manual Deploy** click on **Deploy Branch** button and your app should successfully deploy to Heroku

## Cloning the Website
- Open [**GitHub**](https://github.com/) and log in
- Select the **repository**
- Click the **Code** drop down button next to the green GitPod one
- Select **"Clone with HTTPS"** and copy the link
- Open your **IDE** and the **Terminal**
- Specify a new **path directory** where you want to put the clone
- Type `git clone` and then **paste** the previously copied url from before

# Credits

## Code
- I used [Bootstrap](https://getbootstrap.com/) to make the site
responsive on different devices.

- I used the Boutique Ado mini project from Code Institutes' course to base my websites logic on.

## Images
- The hero background image came from
[Fender](https://www.fender.com/en-GB/start)

## Products

- All products were from [Andertons](https://www.andertons.co.uk/)

## Blog

- Blog post was from [Engadget](https://www.engadget.com/winter-namm-2022-delayed-to-june-205550724.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAH0TANTqSqOF3_c8A4O9-xLrfcFCL3A9aUakF_urSzyG-G53JuZ1FWYLR6PaKophCIl-2opOG8orUhnoplMp0cw6qeTZcORW9Y3ywn_pa1QwaT4RWqVbBMDufw0mtU7KPHElea82E55xXJAeb7a8nP9vdGgoBY159OOVYAwUL_ct)

# Special Thanks

Special thanks to the Slack community, Stack Overflow, Tutor Support and my Mentor for all their advice and guidance on this project.
