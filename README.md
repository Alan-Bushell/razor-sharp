# Razor Sharp

![am I responsive screenshot](media/readme/amiresponsive.png)

## A Mens Grooming E-commerce Store.
> A Men's grooming e-commerce website that provides goods for sale as well as blog content to share tips and advice.


### - By Alan Bushell

## **[Live site](https://abushell-razor-sharp.herokuapp.com/)**

---

## **[Repository](https://github.com/Alan-Bushell/razor-sharp)**

---
  
## Table of contents
<a name="contents">Back to Top</a>
 1. [ UX ](#ux)
 2. [Agile Development](#agile)
 3. [ Features ](#features)  
 4. [ Features Left to Implement ](#left)  
 5. [ Technology used ](#tech) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#bugs)  
 8. [ Deployment](#deployment)
 9. [ Credits](#credits)
 10. [ Content](#content)  
 11. [ Acknowledgements](#acknowledgements)  
 

## UX

<a name="ux"></a>
### Color Pallette

<details>
<summary> Color Pallete </summary>
<br>

![Color Pallette](media/readme/color-pallette.png)
</details>


### Database Schema

<details>
<summary> Database Structure</summary>
<br>

This was the suspected preproject planning database structure. As the project was being developed changes were made to the final project due to time contraints and project scope.

![Lucid Diagram](media/readme/erd-preproject.png)
</details>

---
### Accounts App

#### Account Model
| id | Field |
|--|--|
|first_name|CharField|
|last_name|CharField|
|username|CharField|
|email|EmailField|
|phone_number|CharField|
|date_joined|DateTimeField|
|last_login|DateTimeField|
|is_admin|BooleanField|
|is_staff|BooleanField|
|is_active|BooleanField|
|is_superadmin|BooleanField|

---

#### UserProfile Model

| id | Field |
|--|--|
|user|OneToOneField|
|street_address1|CharField|
|street_address2|CharField|
|town_or_city|CharField|
|county|CharField|
|postcode|CharField|
|country|CountryField|
|profile_picture|ImageField|


---
### Blog App

#### Post Model

| id | Field |
|--|--|
|title|CharField|
|slug|SlugField|
|author|ForeignKey|
|updated_on|DateTimeField|
|content|TextField|
|featured_image|ImageField|
|excerpt|TextField|
|created_on|DateTimeField|
|status|BooleanField|
|likes|ManyToManyField|

---

#### Comment Model

| id | Field |
|--|--|
|post|ForeignKey|
|body|TextField|
|created_on|DateTimeField|
|username|ForeignKey|
---

### Cart App

#### Cart Model

| id | Field |
|--|--|
|cart_id|CharField|
|date_added|DateField|

---

#### CartItem Model

| id | Field |
|--|--|
|product|ForeignKey|
|cart|ForeignKey|
|quantity|IntegerField|
|is_active|BooleanField|

### Checkout App

#### Order Model

| id | Field |
|--|--|
|user|ForeignKey|
|order_number|CharField|
|first_name|CharField|
|last_name|CharField|
|email|EmailField|
|phone_number|CharField|
|country|CountryField|
|street_address1|CharField|
|street_address2|CharField|
|town_or_city|CharField|
|postcode|CharField|
|county|CharField|
|date|DateTimeField|
|deliver_cost|DecimalField|
|order_total|DecimalField|
|grand_total|DecimalField|
|original_cart|TextField|
|stripe_pid|CharField|
|is_ordered|BooleanField|

---

#### OrderLineItem Model
| id | Field |
|--|--|
|order|ForeignKey|
|product|ForeignKey|
|quantity|IntegerField|
|lineitem_total|DecimalField|


# UX design

## Overview




### Site User
The typical site user would be a male aged between 18 and 50 who has an interest in self care, grooming and presenting a good outward image. Additional site users could be partners of user 1 and may be browsing the site to purchase gifts for them.


###  Goals for the website
The goals for the website are:
- An easy to navigate website with clear purpose
- Provide users with products that meet their expectations
- Allow users to view, read and comment on articles that may help or interest them.
- To gain insights or tips on self care.
- Allow users to checkout quickly and easily
- To allow users to create a profile to view past orders and update profile information


## Wireframes

<details>
<summary> Wireframes </summary>
<br>

![Wireframe Index](media/readme/wireframe-index.png)

![Wireframe Mobile](media/readme/wireframe-mobile.png)

![Wireframe Products](media/readme/wireframe-products.png)
</details>



## Agile Development

<a name="agile"></a>

### Agile Overview


#### User stories

#####  Completed User Stories


 1. [USER STORY: Sample](issues/57)

 ##### NINTH User stories
 
 1. [USER STORY: Sample](https://github.com/Alan-Bushell/razor-sharp/issues/57)


[Back to Top of page](#contents)

---

## Features

<a name="features"></a>

<details>
<summary> Navigation </summary>
<br>

![Navbar Desktop](media/readme/navbar-desktop.png)

![Navbar Mobile](media/readme/mobile-nav.png)

![Mobile Navbar Expanded](media/readme/mobile-nav-expanded.png)
  
![Footer](media/readme/footer.png)

</details>

<details>
<summary> Authentication </summary>
<br>

![Sign Up](media/readme/sign-up.png)

![Login](media/readme/login.png)

</details>

<details>
<summary> Products Page </summary>
<br>

![Products Page](media/readme/products-page.png)

![Products Details](media/readme/product-details.png)

</details>


<details>
<summary> Cart & Checkout Flow </summary>
<br>

![Cart Page](media/readme/cart-page.png)

![Checkout Page](media/readme/checkout-page.png)

![Payment Success Page](media/readme/payment-success-page.png)

</details>


<details>
<summary> Account Profiles </summary>
<br>

![Accounts](media/readme/accounts-home.png)

![Shipping Details](media/readme/shipping-info.png)

![Change Profile Photo](media/readme/change-profile-photo.png)

![Order History](media/readme/order-history.png)

</details>

<details>
<summary> Blog </summary>
<br>

![Blog Page](media/readme/blog-page.png)

![Blog Details](media/readme/blog-details.png)

![Blog Comments](media/readme/blog-comments.png)

</details>

<details>
<summary> Contact Page </summary>
<br>

![Contact Form](media/readme/contact-form.png)

![Contact form Dropdown](media/readme/contact-form-dropdown.png)

</details>


<details>
<summary> Account Notifications </summary>
<br>

![Sign-in Notification](media/readme/sign-in-notification.png)

![Order History Notification](media/readme/order-history-notification.png)
  
![Add to cart notification](media/readme/add-cart-notification.png)

</details>

<details>
<summary> Admin related permissions </summary>
<br>

![Admin Product Permissions](media/readme/admin-product-permissions.png)

![Admin Product Add Form](media/readme/admin-product-add-form.png)

</details>


<details>
<summary> Additional Pages </summary>
<br>

![Shipping Policy](media/readme/shipping-policy.png)

![FAQ's](media/readme/sample-faqs.png)
  
![Subscribe](media/readme/subscribe.png)

</details>


#### Account restrictions:



[Back to Top of page](#contents)

---

<a name="left"></a>
## Features left to Implement 

[Back to Top of page](#contents)

---

<a name="tech"></a>
##  Technology Used

### Html

 - Used to structure my webpages and the base templating language

### CSS

 - Custom CSS was written on large chunks of this site to make it as close to the wireframes as I felt it needed to be.

### JavaScript

 -  Used to add timeout function for messages as well as to enable the menu on index.html

### Python

 -  Used for the logic in this project.

### Django

 -  Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient.

### Font Awesome

 -  Icon library used

### Bootstrap 4
 - Used as the base front end framework to work alongside Django

### Jinja Templating with Django
 - Used to render logic within html documents and make the website more dynamic.

### GitHub
 - Used to store the code for this project & for the projects Kanban board used to complete it.

### Heroku
- Used to host and deploy this project

### Heroku PostgreSQL
-Heroku PostgreSQL was used as the database for this project during development and in production.


### Git
- Used for version control throughout the project and to ensure a good clean record of work done was maintained.

[Back to Top of page](#contents)

---

<a name="testing"></a>
## Testing


### Testing Phase

#### Manual Testing

>If the intended outcome completes then this will be flagged as pass. If it does not then this is a fail.


#### Account Registration Tests
| Test |Result  |
|--|--|


---

#### User Navigation Tests

| Test |Result  |
|--|--|


---

#### Account Security Tests

| Test |Result  |
|--|--|


--- 

#### Profile Tests

| Test |Result  |
|--|--|



#### Admin Tests

| Test |Result  |
|--|--|

---

## Google Lighthouse Testing

### Desktop

> index.html


![Google Lighthouse Index]()

> profile.html


![Google Lighthouse Profile]()


## HTML W3 Validation

### index.html


![W3 Validation checker]()
#### Result: 

### CSS Validation


![w3 Jigsaw CSS checker]()
#### Result: 

[Back to Top of page](#contents)

---

<a name="bugs"></a>
## **Bugs**

[Back to Top of page](#contents)

---

<a name="deployment"></a>
## Deployment


#### Forking the repository


[Back to Top of page](#contents)

---
  
<a name="credits"></a>
## Credits
  
[Back to Top of page](#contents)

---

<a name="content"></a>
## Content & Resources
  
##### Django Documentation
  - Read through the django documentation multiple times when trying to implement models and other content.
  
##### W3 Schools
  - Used for reference throughout for simple css examples.
  
##### Code Institute
  - Course content for portfolio project 5 helped greatly in being able to complete this project.
  - I found the walkthroughs informative and well paced.
  - Initial structure based heavily on the CI walkthrough until I got more comfortable with the framework and started to make it my own.
  - Some legacy code regarding nav remains.

[Back to Top of page](#contents)

---

<a name="acknowlegements"></a>
## Acknowledgements

### Dick Vlandeeren
> My mentor who provided me with constructive feedback  and guidance throughout.
