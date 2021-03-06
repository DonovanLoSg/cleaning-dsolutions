<img src="http://resume.donovanlo.sg/images/donovanlogo150x131.png" style="margin: 0; background-color: white" alt="By Donovan">

# Cleaning d'Solutions
*Python and Data Centric Development Milestone Project*

____________________________________________________________

![Cleaning d'Solution landing page](readme/cleaning-dsolutions.png)

Solutions to griminess and messiness.  
Crowdsourced information, guides, recipes, tips and hacks on cleaning.

> # Demo
> - Deployed project: http://cleaning.dsolutions.sg/
> - Source code: https://github.com/DonovanLoSg/cleaningdsolutions

# Contents

- [Defining the project (Strategy)](#defining-the-project-strategy)
    - [Site owner's goal](#site-owners-goal)
    - [Users](#users)
    - [Users' stories](#users-stories)
    - [User’s goals](#users-goals)
    - [Use Case Diagram](#use-case-diagram)
- [Defining the Project (Scope)](#defining-the-project-scope)
    - [Functional Specification](#functional-specification)
        - [Public Access](#public-access)
        - [Member Access](#member-access)
        - [Administrators’ Access](#administrator-access)
    - [Content Requirement](#content-requirement)
        - [Static Content](#static-content)
        - [Dynamic Content](#dynamic-content)
- [Developing the Site Structure and Organize Information (Structure)](#developing-the-site-structure-and-organize-information-structure)
    - [Information Architecture](#information-architecture)
        - [ER diagram](#er-diagram)
   - [Interaction Design](#interaction-design)
        - [User Flow Diagram for General Users](#user-flow-diagram-for-general-users)
        - [User Flow Diagram for Members](#user-flow-diagram-for-members)
        - [User Flow Diagram for Administrators](#user-flow-diagram-for-administrators)
- [Developing Page Structure and Organise Interactions (Skeleton)](#developing-page-structure-and-organise-interaction-skeleton)
    - [Navigation Design](#navigation-design)
        - [Logo](#logo)
        - [Main Navigation](#main-navigation)
        - [Collapsible Hamburger Mobile Menu](#collapsible-hamburger-mobile-menu)
    - [Interface Design](#interface-design)
        - [Site Map](#site-map)
        - [Wireframes](#wireframes)
    - [Information Design](#information-design)
        - [Accessing the information](#accessing-the-information)
        - [Contributing knowledge](#contributing-knowledge)
        - [Validating the information](#validating-the-information)
        - [Managing information submitted](#managing-information-submitted)
- [Designing Graphics User Interface (Surface)](#designing-graphics-user-interface-surface)
    - [Visual Design](#visual-design)
        - [Colour](#colour)
        - [Fonts](#fonts)
        - [Images](#images)
- [Features](#features)
	- [Three Level of Access Rights](#three-level-of-access-rights)
	- [Article Library](#article-library)
    - [Article Listing](#article-listing)
    - [Advanced Article Search](#advanced-article-sort)
	- [Reference Table for the Cleaning Location](#reference-table-for-the-cleaning-location)
	- [Online HTML Editor](#online-html-editor)
	- [Article Commenting](#article-commenting)
	- [Article Rating](#article-rating)
	- [Tagging](#tagging)
	- [Random Articles](#random-articles)
    - [Responsiveness](#responsiveness)
    - [Features to Implements](#features-to-implements)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
    - [Automated Testing](#automated-testing)
        - [W3C MarkUp Validation](#w3c-markup-validation)
        - [W3C CSS Validaton](#w3c-css-validation)
        - [W3C Link Checking](#w3c-link-checking)
        - [Color Contrast Accessibility Validation](#color-contrast-accessibility-validation)
        - [Spell Checking](#spell-checking)
        - [Alt Text Checking](#alt-text-checking)
    - [Manual Testing](#maual-testing)
        - [Compatibility Testing](#compatibility-testing)
        - [User Acceptance Testing](#user-acceptance-testing)
- [Deployment](#deployment)
    - [GitHub](#github)
    - [Git Bash](#git-bash)
    - [Clone repository](#clone-repository)
    - [MongoDB](#mongodb)
    - [Default Administrator](#default-administrator)
    - [Session Key](#session-key)
    - [Heroku](#heroku)
    - [App Deployment](#app-deployment)
    - [Domain Name](#domain-name)
    - [Domain Name Registrar](domain-name-registrar)
- [Credits](#credits)
    - [Codes](#codes)
    - [Fonts](#fonts) 
    - [Frosted Glass Effect using CSS](#frosted-glass-effect-using-css)
    - [Face Icons](#face-icons)
    - [Website Logo](#website-logo)
    - [Background Image](#background-image)


____________________________________________________________

# Defining the Project (Strategy)

## Site owner's goal

- Create an online cleaners’ library.
- Find solutions to my own cleaning issues, and possibility earns some income through google advertisement placement.

## Users

- General Users – this consist of first-time visitor and repeated visitors who are looking for solutions to their cleaning issues.
- Contributors – they are users who are interested to validate the article contents, leave comments to the articles or contribute their own insights, tips and hacks. They will have to register as members.
- Administrators – they are the super user who are given authority to manage the users.

## Users' stories

- As a general user,
    - I would like to locate a relevant article in the system, so that I can have the solutions to my cleaning problems.

- As a contributor (member),
    - I would like to store the article in the library, so that I can access them easily later.
    - I would like to contribute an article so that I can share it with the community.
    - I would like to leave a comment on an article so that I provide feedback with result after trying out the written methods.

- As an administrator,
    - I would like to access the user tables, so that I can mange the users and resetting password.
    - I would like to access the articles, so that I can manage or delete undesirable articles.

## Users' goals

- General Users’ goals 
    - User will search the corresponding guides, depending on the issue they want to solve, by inputting different criteria, such as: article titles, cleaning locations and tags. 

- Contributors’ (Members') goals
    - Contributors will search the corresponding guides, depending on the issue they want to solve, by inputting different criteria, such as: article titles, cleaning locations and tags.
    - Contributors will login to access a secure area to allow them to validate and comments on articles. 
    - Contributors will login to access a secure area to view the articles they contributed. 
    - Contributors will login to access a secure area to allow them to create, edit and delete their own articles. 
    - Contributors will login to access their own profile to change personal information and password

- Administrator’s goal 
    - Administrators will search the corresponding guides, depending on the issue they want to solve, by inputting different criteria, such as: article titles, cleaning locations and tags.
    - Administrators will login to access a secure area to allow them to validate and comments on articles. 
    - Administrators will login to access a secure area to view the articles they contributed. 
    - Administrators will login to access a secure area to allow them to create, edit and delete their own articles. 
    - Administrators will login to access a secure area to allow them to manage or delete articles 
    - Administrators will login to access their own profile to change personal information and reset password 
    - Administrators will login to assign users to be administrators
    - Administrators will login to manage the list of cleaning locations

## Use case diagram

![Use Case Diagram](readme/use-case-diagram.png)

____________________________________________________________

# Defining the Project (Scope)

## Functional Specification

### Public Access

- Get up to 5 articles from the database and display it on the homepage, allow user to click on one of these 5 default article titles to view the article.
- Display a search panel to allow users to search using different methods: search by article titles, search by cleaning location or search by tags.
- When a search is executed, it will return the result in a list containing article titles and cleaning locations.
- Allow user to select one of the articles by clicking on the article titles from the search results to view the article.
- Display the article containing article titles, cleaning location, article content, cleaning items, cleaning supplies and tags.
- List the comments for individual articles
- Display the count of validating vote.
- Include an option to display all the articles.
- Include a link to the user registration page which accept nickname, email address, password and password retype. The email address must be valid and unique in the system, the password must be at least eight characters and contain at least one letter and one number, the password retype must be same as the password.
- Allow members and administrators to log in through a login page accepting nickname and password. If the validation is successful, redirect the user to administrators’ access area if they are administrators, else they will be redirected to a members’ access area. If the validation is unsuccessful, they will be alerted with a message and allowed to retry again.

### Member Access

- Display a list of all articles the member contributed.
- Allow member to select one of the articles by clicking on the article titles from the list to view the article.
- Allow member to select one of the articles by clicking on the corresponding delete button.
- Allow member to delete the article by clicking on the "delete confirmation" button on the article itself.
- Allow member to edit the article by clicking on the "edit" button on the article itself.
- Allow member to add a comment on the article page.
- Allow member to edit the comment he left on the article page
- Allow member to validate the article content by voting whether it works, somewhat works, or doesn’t work.
- Allow member to change their validating votes.
- Allow member to edit articles they contributed.
- Allow member to delete articles they contributed.
- Include an article creation page accepting article titles, cleaning location, article content, cleaning items, cleaning supplies and tags.
- Allow member to view their own profile containing of nickname, email address and password.
- Allow member to update their nickname or reset their password.

### Administrator Access

- Display a search panel to allow administrator to search using different methods: search by article titles, search by cleaning location or search by tags.
- When a search is executed, it will return the result in a list containing article titles and cleaning locations.
- Allow administrator to select one of article by clicking on the article titles from the search results to view the article.
- Allow administrator to delete an article by clicking on the corresponding "delete" button.
- Allow administrator to delete an article by clicking on the "delete button" on the article itself.
- Allow administrator to edit an article by clicking on the "edit" button on the article itself.
- Allow administrator to add a comment on the article page.
- Allow administrator to edit the comment he left on the article page.
- Allow administrator to validate the article content by voting whether it works, somewhat works, or doesn’t work.
- Allow administrator to change their validating votes.
- Allow administrator to edit any article.
- Allow administrator to delete any article.
- Include an article creation page accepting article titles, cleaning location, article content, cleaning items, cleaning supplies and tags.
- Allow administrator to view their own profile comprising of nickname, email address and password.
- Allow administrator to update their nickname or reset their password.
- Display a list of all the users.
- Allow administrator to search for a user.
- Display the selected user profile.
- Allow administrator to edit the user profile (modify nickname).
- Allow administrator to delete user profile.
- Allow administrator to reset user password.
- Allow administrator to assign admin rights.
- Allow administrator to manage the list of cleaning location.

## Content Requirement

### Static Content

- Content for an “About” page to introduce this application.
- Content for step by step instructions for the users and members
    - Searching for information
    - Register for a member account
    - Logging In
    - Contribute articles
    - Edit / Delete articles
    - Adding Comments
    - Validating the content
    - Changing nickname
    - Resetting password
- Content for step by step instructions for administrator
    - Search for user profiles
    - Modifying/Deleting user profiles
    - Assigning admin rights
    - Modifying/Deleting articles 

### Dynamic Content

- Records of articles includes article id, article title, cleaning location, article content, cleaning items, cleaning supplies, tags, creator, date created, date modified, count of the three different type of validated results.
- Comments attached to the articles record (maximum one per user per article)
- Validation (i.e. working, somewhat working, not working) (maximum one per user per article)
- Records of users includes user id, nickname, email address, password and a flag indicating whether he has administration rights.
- List of cleaning locations

____________________________________________________________

# Developing the Site Structure and Organize Information (Structure)

## Information Architecture

### ER diagram

![ER Diagram](readme/er-diagram.png)

## Interaction Design

### User Flow Diagram for General Users

![General Users' Flow Diagram](readme/user-flow-diagram-user.png)

### User Flow Diagram for Members

![Members' Flow Diagram](readme/user-flow-diagram-members.png)

### User Flow Diagram for Administrators

![Administrators' Flow Diagram](readme/user-flow-diagram-admin.png)

____________________________________________________________

# Developing Page Structure and Organise Interactions (Skeleton)

## Navigation Design

### Logo

- Logo on every page, clicking on it will bring the visitor to the Splash Page. [Bootstrap Component - Navbar]

### Main Navigation

- Main Navigation is a fixed position menu at the top of every web page. They are hyperlinked to their respective pages. [Bootstrap Component - Navbar]

![Prototype of Navigation Menu displaying different menu when users logged in as a member or administrator](readme/navbar.png)

### Collapsible Hamburger Mobile Menu

- The top navigation will be minimized into a hamburger menu when displayed in mobile screens or other small screens. Clicking on it will display the familiar 3 choices. [Bootstrap Component - Navbar]

## Interface Design

The site consists of pages that are easily to recognise.

- Landing page / Splash page
    - The landing page / splash page have two call to actions buttons, inviting user to either search for an article or read and article.

        ![Splash page](readme/splash-page.png)

Each page are made up of three sections, the header, the title and the main content.

- ![Identifying the three sections of the page: Header, Page Title and Main Content](readme/three-sections.png)

- Header: 
    - The header will include a logo, name of this app and the navigation menu.
    - The navigation menu's items depends on whether the user is logged in and whether he is an administrator.
    - Public users will be able to search and read the articles.
    - A logged in users will be able to see additional menu items like [Contribute Articles]. 
    - A logged in users can access his profile by clicking on his name on the right of the header.
    - If the logged in user is an administrator, he will even more items, like [Manager Users], available to administrators only,

- Page Title:
    - The title of the functions the user is accessing is display in simple words here.

- Main Content:
    - The app embraces a simple layout.
    - Other than the home page which has two panels, the rest of the pages only have one panel.
    - The home page left panel is a search panel allowing the user to input the criteria for the search.
    - The home page right panel display up to 5 random articles which the user can view by clicking on the article titles.

### Site Map

- ![Site Map](readme/sitemap.png)

### Wireframes

- Splash Page
    - ![Splash Page wireframes](readme/wireframe-splash.png)

- Home Page
    - ![Home Page wireframes](readme/wireframe-home.png)

- Page Containing tables
    - ![Wireframes of page containing tables](readme/wireframe-tables.png)

- Page with One Column Layout
    - ![Wireframes of page with one column layout](readme/wireframe-one-column.png)

- Article Page
    - ![Wireframes of article page](readme/wireframe-article.png)

## Information Design

### Accessing the information

- The purpose of the system is to allow public users to find solutions to their cleaning issues.
There are different ways of accessing the articles stored in the database.

    - Search Articles
        - The user can search:
            - for articles which titles contain certain words
            - for articles which targeted at a selected cleaning location
            - for articles that are tagged with certain words
            - on a combination of two or even all the conditions above
        - The result of the search will be displayed in the format similar to the one listing all the articles.
    - Random Articles 
        - The system randomly generate a list of 5 articles from the database and 
        display them on the right panel of the home page.
        - Clicking on the article titles will allow users to access the articles directly
    - All Articles
        - The system will present the list of articles in a table form.

- The results will be return as a list of article titles.
    - Pagination
        - If the list is long, it will be divided into pages.
        - The default number of articles listed per page is ten, but the user can choose to how many articles to show by adjusting the number of show entries.
        - There is an indicator between the displayed list to show the user which are the entries listed.
        - The user can navigator through the pages using the page navigator on the bottom right of the table.  
    -  Enhanced Search
        - The user can do an enhanced search on the list using the search field above the table.
    - Sorting
        - In the table, there are three columns, namely, Article Title, Cleaning Locations and Action.
        - User can sort the Article Title and Cleaning Location by clicking on the column headings.
        - Clicking on the same heading toggles between ascending sort and descending sort.
    - Viewing
        - The user can access the article by clicking on the corresponding 'view' button.
    - Deleting
        - This option will only appears to the administrator. 
        - Clicking on the "delete" button will allow administrator to see the page he selected to confirm his decision.

#### User's Own Articles

- After a user logged in, he can click on the 'Articles' on the navigation menu and select 'My Articles' from the submenu
to access to the list of articles he has contributed to the database.

### Contributing knowledge

- A logged in user can add his knowledge to the database by selecting 'Contribute Articles' 
under the 'Articles' navigation menu.
- The user will need to fill up an online form which include:
    - Article Title: The title of the article will be shown in listings and search results.
    - Targeted cleaning location: The location which the methods describe in the article is applied to.
    - Content: This allows user enter the content he likes share. Formatting like styling, bolding, italics, highlighting, text justifying, indentation can be applied.
    - Cleaning items: equipment and appliances used in the content described.
    - Cleaning supplies: consumables, items which may be used up in the process.
    - Tags: labels that helps users to locate the articles. They can be names of the item being cleaned (e.g. oven, refrigerator), the problems encountered (e.g. choke, stains) etc.

### Validating the information 

- Ratings
    - The user can validate the methods suggested in the article by rating it.
    - There three ratings are:
        1. It works! (smiling face)
        1. Works somewhat.. (blank face)
        1. It doesn't work ! (frowning face)
    - A logged in user will be able to rate on the Article Page.
    - They can change their mind and rate the article differently at a later time.
    - They can also see the total number of each rating given by other users.
    - To see who are the user giving the rating, click on the "view comments" button.

- Comments
    - A logged in user can also be able leave their comments on the Article Page.
    - They can also edit their comments if they have left it previously.
    - They can see what other users commented by clicking on the "view comments" button.

### Managing information submitted

- Editing Articles
    - The contributer of an article can click on the "Edit" button on the article to make changes.
    - The administrator also have the ability to amend any article to rid of inappropriate content.
- Deleting
    - An article can also be deleted by the contributor using the "Delete" button on the article page.
    - He can also click delete to the right of the corresponding article titles from "My Articles" listing.
    - The administrator can delete any articles using the same methods as above, as well as doing it at the "All articles" listing.
    - When a "Delete" button is click, the article will be displayed to seek confirmation of deletion.
- Adding and deleting cleaning location
    - An administrator can add or delete a cleaning location from a managed list.
    - The list acts as a reference to the the dropdown selection in other pages.
    - Deleting any entries from this list does not affect articles with the deleted location.

____________________________________________________________

# Designing Graphics User Interface (Surface)

## Visual Design

### Images

- Background image
    - A background image is specially selected to project a clean home image.
    - The image is able to cover the whole screen with its high resolutions.
    - A smaller version of the image is used when displaying on mobile devices.
- Faces icons
    - The face icons are used for showing the ratings as well as during the user's selection.
    - The smiling face showing "It works", the blank or neutral face indicating "works somewhat', and the frowning face says 'it doesn't work'.

### Color

- The background of all the panel are in white to aids readability.
- The different colored button are used to indicate highlight different things.
    - Most of the buttons are in blue (e.g. 'Search', 'Edit Articles')
    - Some actions requires a bit more of user's attention to prevent unwanted results.
    - They are in yellow as warnings. (e.g. 'Delete') and those in red (e.g. 'Confirm Deletion').
    - Other colors, like green, are used to provide positive affirmation (e.g. Save) and cyan for indicating more information ('View Comments')

### Fonts

- Google fonts are used for this project.
    - The 'Roboto' font is chosen as the main font of the site due to its readability and neatness.
    - 'Baloo Tamma 2' is selected for the splash page wordings as well as for the page title due to its clean look.
    - To differentiate article titles from other text, 'Lora' fonts are used.

__________________________________________________________________

# Features

## Three Level of Access Rights

- In additional to public access, this application allows user to register as a member to access to more features.
- An administrator can also assign administrator rights to a user to manage the application.

    - Public Access  
    Any visitors are allowed to browse or search through the list of titles for articles he is interested in.  
    He can access to view the articles by clicking 'View' from the list.  
    He can register as a member to access more features.

    - Member Access
    Once an user logged in as a member, he will be able to rate and leave comments to articles he views.  
    He can also contribute his own articles.  
    He can access the list of articles to update or even delete them at a later time.  
    A member can also update his own profile, which includes the change of passwords.

    - Administrator  
    Administrators can assign a user admnistrative rights.  
    When an administrator logged in, he will be able to update and delete any articles.  
    He will be able to manage the users as well as the reference table of cleaning locations.

## Article Library

- This application function is to crowdsource and share information on cleaning.
- It allows unrestricted viewing access to the public.
- It also allows a member (registered users) to contribute or store articles.
- The member can also access a page which only list articles he has contributed.
He can decide to edit or delete as deem necessary.

- In every articles, they are made up of 
    - a article title, 
    - targeted cleaning location,
    - main content, 
    - cleaning items list, 
    - cleaning supplies list, and 
    - tags.

## Advanced Article Search

- The search panel on the home page allows users to search for articles in the database.

- Search can be performed for 
    - article titles which contain a certain word.
    - articles which target at one or more specific cleaning location.
    - articles which has a certain tag.

- The search can also be a combination of two or even three criteria by just ticking the criteria to include in the search.  
e.g. Searching for titles that include words like "How to" and the cleaning target being the kitchen and having the tags like "sink, choke".


## Article Listing

- Regardless of whether the user select to browse all articles, search for articles, listing his own articles, the result will be a list of articles titles.
- This list is sortable by clicking on the column header.
    - Clicking on the column header currently sorted by will change the order of sorting.
    - It will toggle between ascending sort and descending sort.
- Pagination is also applied to the table.
    - By default, it will show 10 entries per page, but users can choose to increase it or decrease it,
    - by changing the options on the top left-hand corner of the table.
    - The bottom left of the table indicates which are the entries being displayed in the table.
- Bottom-right of the table shows which page the users are on and the users can navigator through the pages here.
- There is a search field on the top right of the table, this allows user to do a refined search within the entries listed.

## Reference Table for the Cleaning Location

- The cleaning locations uses a reference table to limit variations of entries.
    - This helps to group the articles easily without rounds of data cleaning.
    - The reference table can be access and managed in the Administrator Access area.
    - Deleting entries from the reference tables will not affect the existing entries.
- This table provides options to select from during creation, edition and search.
- The user can only selected one cleaning locations for each article.
- More than one options can be selected to be criteria of performing a search.

## Online HTML Editor

- The main content of the article can be format.
- An online HTML editor is embedded in the page for creation and edition of the articles.

## Article Commenting

- A member will be able to leave a comments on the article he viewed.
- He can also edit his own comments at a later time.
- The comments given by different uses for an article are kept in a list accessible by clicking "View Comments'.

## Article rating

- A member can validate the methods or items is workable by rating.
    - There are three ratings: 
        - "It works!" (smiling face), 
        - "Works somewhat.. (blank face) and 
        - "It doesn't work !" (frowning face).
- The member can rate on the bottom of the article by clicking on the faces.
- He can also update the rating anytime using the same methods.
- The number of each type of ratings are counted and total displayed on top of the article.
- To see the individual's ratings, the member can click on 'View Comments'.

## Tagging

- This system allows users to provide a list of tags. 
- The tags can include names of targeted items to be cleaned (e.g. Sink) and problems encounter (e.g. choke ).
- Tags can be part of the searching criteria, helping with the accuracy of the search result.

## Random Articles

- To give users have a glimpse of the content of the database, up to five random articles are listed on the home page.

## Responsiveness

- This site embrace responsive web design.
- Its layout is coded to adapt to different screen size in order to make it look good on all devices (desktops, tablets, and phones)

## Features to Implements

- Sign up for Google Partners in Google Ads
 
____________________________________________________________

# Technologies Used

In this project I used *HTML5* to structure the web pages and *CSS3* for front end development 
*Python* and *Flask *for the back end.

I use *Git* for Versioning Control System and *GitHub* for development repositories.

Heroku is used for hosting Production files.

Database is hosted on *MongoDB*.

Gitpod, an online IDE, is my main coding platform. I do sometimes test out my codes in Repl.it

I use Bootstrap 4, including its components and utilities for layout (e.g.NavBar is used for the main navigation)

The interactivity  is enabled by Javascript and it's libraries (DataTables, jQuery, TinyMCE), taking advantages of DOM.

A CSS Reset style sheet from Killer Collection of CSS Resets (https://perishablepress.com/a-killer-collection-of-global-css-reset-styles/) is used in additional to Code Institute templates (https://github.com/Code-Institute-Org/gitpod-full-template) to start the coding. The template used for Readme.md is also from Code Institutes (https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md)


For Favicons:
- Favicon & App Icon Generator (https://www.favicon-generator.org/)

For Code formatting
- JavaScript Beautifier (https://www.freeformatter.com/javascript-beautifier.html)
- CSS Beautifier (https://www.freeformatter.com/javascript-beautifier.html)

For Code Validation
- W3C Markup Validation Service (https://validator.w3.org/) 
- W3C CSS Validation Service (https://jigsaw.w3.org/css-validator/)
- W3C Link Checker (https://validator.w3.org/checklink)
- Alt Text Checker (https://rushax.com/tools/alt-tag-checker/)
- JSLint (https://jslint.com/)
- W3C Spell Checker (https://www.w3.org/2002/01/spellchecker)
- Typosaurus (https://typosaur.us/) 
- Color Contrast Accessibility Validator (https://color.a11y.com/Contrast/)
- Favicon Checker (https://www.seoptimer.com/favicon-checker)

For Responsive Checks
- Responsive Design Checker (https://responsivedesignchecker.com/)

For Mindmapping
- Xmind (https://www.xmind.net/)

For Fonts
- Google Fonts (https://fonts.google.com/)

For Wireframe
- MockFlow (https://www.mockflow.com/)

For Diagrams (Use Case Diagrams, User Flow Diagrams, ER Diagrams and Site Map)
- Diagrams.net (https://www.diagrams.net/)

For image editing
- Paint.NET (https://www.getpaint.net)

For grammer and spell check
- Grammer Checker - Online Editor (https://grammarchecker.io/)
- Reverso (https://www.reverso.net/spell-checker/english-spelling-grammar/) -->
- Typosaurus (https://typosaur.us/)

For About and Instructions page
- GitBook (https://www.gitbook.com/)

____________________________________________________________

# Testing

## Automated Testing

### W3C Markup Validation

    Validated with W3C Markup Validation Service (https://validator.w3.org/) 
    Rectified all issues except three elements intentionally placed to prevent caching:
    
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">

### W3C CSS Validation

    Validated with W3C CSS Validator (https://jigsaw.w3.org/css-validator/)

    Checking the 3 CSS files (myStyle.css, splash.css and articleContent.css) by direct input.

    No Error Found.

### W3C Link Checking

    Using W3C Link Checker (https://validator.w3.org/checklink)
- ![Result of link checking performed on this site](readme/w3c-link-check-result.png)



### Color Contrast Accessibility Validation

    Using Color Contrast Accessibility Validator (https://color.a11y.com/Contrast/)

    Tested all the following pages:
        - http://cleaning.dsolutions.sg/
        - http://cleaning.dsolutions.sg/home
        - http://cleaning.dsolutions.sg/auth/login
        - http://cleaning.dsolutions.sg/auth/logout
        - http://cleaning.dsolutions.sg/auth/register
        - http://cleaning.dsolutions.sg/users/my-profile
        - http://cleaning.dsolutions.sg/articles/list
        - http://cleaning.dsolutions.sg/articles/list-all
        - http://cleaning.dsolutions.sg/articles/my-list
        - http://cleaning.dsolutions.sg/articles/contribute
        - http://cleaning.dsolutions.sg/articles/edit/5f31248396c2aae837a48d0f
        - http://cleaning.dsolutions.sg/articles/5f31248396c2aae837a48d0f
        - http://cleaning.dsolutions.sg/articles/delete/5f31248396c2aae837a48d0f/my
        - http://cleaning.dsolutions.sg/rate/5f31248396c2aae837a48d0f/good
        - http://cleaning.dsolutions.sg/comment/add/5f31248396c2aae837a48d0f
        - http://cleaning.dsolutions.sg/comment/view/5f31248396c2aae837a48d0f
        - http://cleaning.dsolutions.sg/cleaning-locations/manage
        - http://cleaning.dsolutions.sg/users/manage
        - http://cleaning.dsolutions.sg/error-encountered

        *Note: 5f31248396c2aae837a48d0f is an article id

    Rectified color contrast issues of BootStrap's .btn-primary and DataTable's .page-item buttons.

### Spell Checking

    Using Typosaurus (https://typosaur.us/)

    Check all pages without an content's spelling issues.
    Except some class name and the website title "d'Solutions"

### Alt Text Checking 

    Using Alt Text Checker (https://rushax.com/tools/alt-tag-checker/)

    Check all pages. 0 missing alt tags.

## Manual Testing

### Compatibility Testing

    Compatibility Testing was done using Chrome DevTool's Mobile Simulation.
    The pages, graphics and tables are checked for it's responsiveness to ensure no codes are broken and no layout runs out of the screens.

### User Acceptance Testing

    Manual User Testing are documented in this Google Sheet:
    https://docs.google.com/spreadsheets/d/1MqkRPLtFEHGlK5F9lae6MqEdbwBf8I4yXKhSMiw6JV0/edit?usp=sharing


____________________________________________________________

# Deployment

The application is developed on GitHub, using Python, with Flask framework, deployed to Heroku and storing the database in MongDB.
If you want to deploy your own instance of this application, here are the steps:

## 1. GitHub

- If you do not have a GitHub account, you can [sign up for one](https://github.com/join?source=login)

## 2. Git Bash

- If you do not have any have any avenue to issue Git commands, you can [download Git Bash](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## 3. Clone repository

1. Navgiate to https://github.com/DonovanLoSg/cleaning-dsolutions.git
1. Clone this repository.
- For instruction how to clone a repository, visit [GitHub Docs > Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

## 4. MongoDB

1. Setup an account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
1. Go to Clusters to create a database and name it 'cleaning-dsolutions'
1. Create three collections ('articles', 'cleaning-locations' and 'registered_users')
1. Go to Database Access under Security, add a Database User with username 'root'
1. To access a cluster, you must connect from an IP address on the Atlas project’s IP whitelist.
You can also add the IP address from the Security tab.
1. Go to the Clusters newly created database, click on Connect.
1. Select 'Connect Your Application' .
1. Click on the 'Copy' button and you will get a string similar to this:
    
    'mongodb+srv://root:<password>@cleaning-dsolutions.gu6vi.gcp.mongodb.net/<dbname>?
    retryWrites=true&w=majority'

1. Replace your string 'password' with your newly created user 'root's password.
1. Relace the <dbname> to cleaning-dsolutions
1. Safe keep this string to be used when setting up Heroku.

## 5. Default Administrator

1. On MongoDB, Go to the cleaning-dsolutions database's registered users collection.
1. Insert a document as follows:

    email:"{replace with yhour email address}"  
    nickname: "admin"  
    password: "{replace with a password with at least 8 characters long}"  
    admin: "true"  

- This will be your default admin account to the new application.

- For more information, you can visit [MongoDB Atlas > Connect to a Cluster](https://docs.atlas.mongodb.com/connect-to-cluster/)

## 6. Session Key

1. Generate a random session key (preferably 504-bit WPA Key). You can obtain one from [RandomKeygen](https://randomkeygen.com/)

## 7. Heroku

1. Set up an account at [Heroku](https://signup.heroku.com/）) 
1. Create a new app
1. Go into the app, and navigate to 'Setting'
1. Scroll down to Config Vars and click on Reveal Config Vars
1. Key in these entries:

    DB_ARTICLE : articles  
    DB_LOCATION : cleaning_locations  
    DB_NAME : cleaning-dsolutions  
    DB_USER : registered_users  
    MONGO_URI : {enter the string generated from MongoDB)  
    SESSION_KEY : {enter the session key you generated in the previous step.}  

## 8. App Deployment

1. On Heroku, go to Deply tab and choose a deployment method.
1. Connect to Github repository you have created.
- Your app will be automaticalled deployed with the help fo 'requirements.txt' file which is in the repository ou have clone.

## 9. Domain Name (Optional)

- If you have registered a domain name for the new app, you can go to Heroku to configure it.

1. On Heroku,
    1. go to your app's Setting, scroll down to Domains
    1. Enter your domain name. (without the 'https://')
    1. You will see a DNS Target.Copy this string to be used to configure at your Domain NAme Registrar
1. In your domain name registrar
        1. Add a new CNAME record and point it at Heroku

    Record: CNAME  
    Name: { use a asterisk (*) if you are using your domain name. you can also use a subdomain name}  
    Value: {pointing it to heroku by entering the DNS Target you copy earlier.}

______________________________________________________

# Credits

## Codes

- GUnicorn - Python Web Server Gateway Interface HTTP server.  
- Popper.js = Positioning tooltips and popovers.
- jQuery - a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax. 
- BootStrap = CSS framework directed at responsive, mobile-first front-end web development
- Flask-Login - provides user session management for Flask
- Flask - a micro web framework written in Python
- Werkzeug - implements WSGI, the standard Python interface between applications and servers.
- Jinja is a template language that renders the pages your application serves.
- MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
- ItsDangerous - securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
- Click -  a framework for writing command line applications. It provides the flask command and allows adding custom management com
- DNSPython - DNS toolkit for Python
- PYthon-DateUtil - provides powerful extensions to the standard datetime module, available in Python.
- Python-dotenv - set environment variables defined in the files .env and .flaskenv
- PyMongo - MongoDB API Docs for python
- DataTables - a plug-in for the jQuery Javascript library, add advanced interaction controls to your HTML tables
- TinyMCE - online rich-text editor
 
## Fonts

- Google Fonts - a interactive web library of free licensed font families

## Frosted Glass Effect using CSS

- Jaime Contreras, Texas Creative
    - https://texascreative.com/blog/frosted-glass-html-css-tweaks

## Face icons

- Fajar Hasyim
    - The Noun Project
    - https://thenounproject.com/fajarhasyim.91/collection/website-icon-set/

## Website Logo

- Woot1234
    - FavPng.com
    - https://favpng.com/png_view/clean-logo-green-cleaning-cleaner-logo-environmentally-friendly-png/sCFxe94P 

## Background Image

- jeanvdmeulen
    - Pixabay
    - https://pixabay.com/photos/dining-room-living-room-modern-3108037/

______________________________________________________

# Acknowledgements

- Mr Paul Chor - Mentor.
- Ms Chia Ching Shyan - My classmate - For sharing of articles, youtubes and notes.
- Mr Kevin Lee - My friend - For spending time helping mid project unit testings.
- Mr Jon Tan - My friend - For helping tedious with the user acceptance testings.
 