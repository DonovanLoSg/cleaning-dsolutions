<img src="http://resume.donovanlo.sg/images/donovanlogo150x131.png" style="margin: 0; background-color: white" alt="By Donovan">

# Cleaning d'Solutions
*Python and Data Centric Development Milestone Project*

<hr>

Solutions to griminess and messiness. Crowdsourced information, guides, recipes, tips and hacks on cleaning.

## Demo

Deployed project: http://cleaning.dsolutions.sg/

Source code: https://github.com/DonovanLoSg/cleaningdsolutions

## Contents

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




## Defining the Project (Strategy)

### Site owner's goal

- Create an online cleaners’ library.
- Find solutions to my own cleaning issues, and possibility earns some income through google advertisement placement.

### Users

- General Users – the consist of first-time visitor and repeated visitors who are looking for solutions to their cleaning issues.
- Contributors – they are users who are interested to validate the article contents, leave comments to the articles or contribute their own insights, tips and hacks. They will have to register as members.
- Administrators – they are the super user who are given authority to manage the users.

### Users' stories
- As a general user,
    - I will like to locate a relevant article in the system, so that I can have the solutions to my cleaning problems.

- As a contributor (member),
    - I will like to store the article in the library, so that I can access them easily later.
    - I will like to contribute an article so that I can share it with the community.
    - I will like to leave a comment on an article so that I feedback the result of trying out the written methods.

- As an administrator,
    - I will like to access the user tables, so that I can mange the users and resetting password.
    - I will like to access the articles, so that I can manage or delete undesirable articles.

### Users' goals
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

### Use case diagram
<img src="/readme/use-case-diagram.png" style="margin: 0; width: 100%" alt="Use Case Diagram">

## Defining the Project (Scope)

### Functional Specification

#### Public Access
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

#### Member Access
- Display a list of all articles the member contributed.
- Allow member to select one of the articles by clicking on the article titles from the list to view the article.
- Allow member to select one of the articles by clicking on the corresponding delete button.
- Allow member to delete the article by clicking on the delete confirmation button on the article itself.
- Allow member to edit the article by clicking on the edit button on the article itself.
- Allow member to add a comment on the article page.
- Allow member to edit the comment he left on the article page
- Allow member to validate the article content by voting whether it works, somewhat works, or doesn’t work.
- Allow member to change their validating votes.
- Allow member to edit articles they contributed.
- Allow member to delete articles they contributed.
- Include an article creation page accepting article titles, cleaning location, article content, cleaning items, cleaning supplies and tags.
- Allow member to view their own profile comprising of nickname, email address and password.
- Allow member to update their nickname or reset their password.

#### Administrator Access
- Display a search panel to allow administrator to search using different methods: search by article titles, search by cleaning location or search by tags.
- When a search is executed, it will return the result in a list containing article titles and cleaning locations.
- Allow administrator to select one of article by clicking on the article titles from the search results to view the article.
- Allow administrator to delete an article by clicking on the corresponding delete button.
- Allow administrator to delete an article by clicking on the delete button on the article itself.
- Allow administrator to edit an article by clicking on the edit button on the article itself.
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

### Content Requirement

#### Static Content

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
- Content for stepy by step instructions for administrator
    - Search for user profiles
    - Modifying/Deleting user profiles
    - Assigning admin rights
    - Modifying/Deleting articles 

#### Dynamic Content

- Records of articles comprising of article id, article title, cleaning location, article content, cleaning items, cleaning supplies, tags, creator, date created, date modified, count of the three different type of validated results.
- Comments attached to the articles record (maximum one per user per article)
- Validation (i.e. working, somewhat working, not working) (maximum one per user per article)
- Records of users comprising of user id, nickname, email address, password and a flag indicating whether he has administration rights.
- List of cleaning locations

## Developing the Site Structure and Organize Information (Structure)

### Information Architecture

#### ER diagram

<img src="/readme/er-diagram.png" style="margin: 0; width: 100%" alt="ER Diagram">

### Interaction Design

#### User Flow Diagram for General Users

<img src="/readme/user-flow-diagram-user.png" style="margin: 0; width: 100%" alt="Gemeral Users' Flow Diagram">

#### User Flow Diagram for Members

<img src="/readme/user-flow-diagram-members.png" style="margin: 0; width: 100%" alt="Members' Flow Diagram">

#### User Flow Diagram for Administrators

<img src="/readme/user-flow-diagram-admin.png" style="margin: 0; width: 100%" alt="Administrators' Flow Diagram">

## Developing Page Structure and Organise Interactions (Skeleton)

### Navigation Design

#### Logo

Logo on every page, clicking on it will bring the visitor to the Splash Page. [Bootstrap Component - Navbar]

#### Main Navigation

Main Navigation is a fixed position menu at the top of every web page. They are hyperlinked to their respective pages. [Bootstrap Component - Navbar]

<img src="/readme/navbar.png" style="margin: 0; width: 100%" alt="Navigation Menu displaying different menu when users logged in as a member or administrator">

#### Collapsible Hamburger Mobile Menu

The top navigation will be minimised into a hamburger menu when displayed in mobile screens or other small screens. Clicking on it will display the familiar 3 choices. [Bootstrap Component - Navbar]

### Interface Design

The site consists of pages that are easily to recognised.

The landing page / splash page have two call to actions buttons, inviting user to either search for an article or read and article.

<img src="/readme/splash-page.png" style="margin: 0; width: 100%" alt="Splash page">

In the site, each pages are made up of three section, the header, the title and the main content.

<img src="/readme/three-sections.png" style="margin: 0; width: 100%" alt="three sections of the page: header, title and main content">

Header: 
- The header will include a logo, name of this app and the navigation menu.
- The navigation menu's items depends on whether the user is logged in and whether he is an administrator.
- Public users will be able to search and read the articles.
- A logged in users will be able to see additional menu items like [Contribute Articles]. 
- A logged in users can access his profile by clicking on his name on the right of the header.
- If the logged in user is an administrator, he will even more items, like [Manager Users], available to administrators only,

Title:
- The title of the functions the user is accessing is display in simple words here.

Main Content:
- The app embraces a simple layout.
- Other than the home page which has two panels, the rest of the pages only have one panel.
- The home page left panel is a search panel allowing the user to input the criteria for the search.
- The home page right panel display up to 5 random articles which the user can view by clicking on the article titles.

#### Site Map

<img src="/readme/sitemap.png" style="margin: 0; width: 100%" alt="Site Map">

### Information Design

#### Accessing the information
The purpose of the system is allow public users to find a solutions to their cleaning issues.
There are different ways of accessing the articles stored in the database.

##### Search Articles
The user can search:
- for articles which titles contain certain words
- for articles which targetted at a selected cleaning location
- for articles that are tagged with certain words
- on a combination of two or even all the conditions above
The result of the search will be displayed in the format similar to the one listing all the articles.

##### Random Articles 
The system randomly generate a list of 5 articles from the database and 
display them on the right panel of the home page.
Clicking on the article titles will allow users to access the articles directly

##### All Articles
The system will present the list of articles in a table form.

_Pagination_
If the list is long, it will be divided into pages.
The default number of articles listed per page is ten, 
but the user can choose to how many articles to show by adjusting the number of show entries.
There is an indicator between the displayed list to show the user which are the entries listed.
The user can navigator through the pages using the page navigator on the bottom right of the table.

_Enhanced Search_
The user can do an enhanced search on the list using the search field above the table.

_Sorting_
In the table, there are three columns, namely, Article Title, Cleaning Locations and Action.
User can sort the Article Title and Cleaning Location by clicking on the column headings.
Clicking on the same heading toggles between ascending sort and descending sort.

_Viewing_
The user can access the article by clicking on the corresponding 'View' button.

_Deleting_
This option will only appears to the adminstrator. 
Clicking on the 'Delete' button will allow administrator to see the page he selected 
to confirm his decision.

##### User's Own Articles
After a user logged in,
he can click on the 'Articles' on the navigation menu and select 'My Articles' from the submenu
to access to the list of articles he has contributed to the database.

#### Contributing knowledge
A loggin user can add his knowledge to the database by selecting 'Contribute Articles' 
under the 'Articles' navigation menu.

The user will need to fill up an online form which include:
- Article Title: The title of the article will be shown in listings and search results.
- Targeted cleaning location: The location which the methods describe in the article is applied to.
- Content: This allows user enter the content he likes share. Formatting like styling, bolding, italics, highlighting, text justifying, indentation can be applied.
- Cleaning items: equipments used in the content described.
- Cleaning supplies: consumabls items which may be used up in the process.
- Tags: labels that helps users to locate the articles. They can be name of the item being cleaned (e.g. oven, refrigerator), the problems encountered (e.g. choke, stains) etc.

#### Validating the information 

_Ratings_
The user can validate the methods suggested in the article by rating it.
There three ratings are:
1. It works! (smiling face)
2. Works somewhat.. (blank face)
3. It doesn't work ! (frowning face)

A logged in user will be able to rate on the Article Page.
They can change their mind and rate the article differently at a later time.
They can also see the total number of the each rating given by other users.
To see who are the user giving the rating, click on the view comments button.

_Comments_
A logged in user can also be able leave their comments on the Article Page.
They can also edit their comments if they have leave it previously.
They can see what other users commented by clicking on the view comments button.

#### Managing information submitted

_Editing Articles_
The contributer of an article can click on the "Edit" button on the article to make changes.
The administrator also have the ability to amend any article to rid of inappropirate content.

_Deleting_
An article can also be deleted by the contribute using the "Delete" button on the article page.
He can also click delete to the right of the corresponding article titles from "My Articles" listing.
The administrator can delete any articles using the same methods as above, as well as doing it at the "All articles" listing.
When a "Delete" button is click, the article will be displayed to seek confirmation of deletion.

_Adding and deleting cleaning location_
An administrator can add or delete a cleaning location from a managed list.
The list acts as a reference to the the droped down selection in other pages.
Deleting any entries from this list does not affect articles with the deleted location.

## Designing Graphics User Interface (Surface)

### Visual Design

#### Images

_background image_
A background iamge is specially selected to project a clean home image.
The image is able to cover the whole screen with it's high resolutions.

A smaller version of the image is used when displaying on mobile devices.

_faces icons_
The face icons are used for showing the ratings as well as during the user's selection.
The smiling face showing "It works", the blank or neutral face indicating "works somewhat', and the frowning face says 'it doesn't work'.

#### Colour

The background of all the panel are in white to aids readability.

The different colored button are used to indicate highlight different things.
Most of the buttons are in blue (e.g. 'Search', 'Edit Articles')

Some actions requires a bit more of user's attention to prevent unwanted results.
They are in yellow as warnings. (e.g. 'Delete') and those in red (e.g. 'Confirm Deletion').

Others colors, like green, are used to provide positive affirmation (e.g. Save) and 
cyan for indicating more information ('View Comments')

#### Fonts

Google fonts are used for this project.

The 'Roboto' font is chosen as the main font of the site due to it's readability and neatness.

'Baloo Tamma 2' is selected for the splash page wordings as well as for the page title due to it's clean look.

To differentiate article titles from other text, 'Lora' fonts are used.

<hr>
# Features



<hr>

# Technologies Used

<hr>

# Testing

## Functionality Testing

### Link Testing

### Form Testing

### HTML Testing

### CSS Testing

### Color Contrast Accessibility Testing

## Usability Testing

### Navigation Testing