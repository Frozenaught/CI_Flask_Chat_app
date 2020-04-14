# Flask Chat Application

## Introduction

[![Flask Intro Video](http://img.youtube.com/vi/miLkppyHLCA/0.jpg)](http://www.youtube.com/watch?v=miLkppyHLCA)

## Beginning The Project

![What is it](Markdown_Images/whatis.png "what is")

## What is it

Beginning a Flask project

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

Gives us a starting point for our project

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By creating a new Flask project

[![Beginning The Project](http://img.youtube.com/vi/4bV8BAOsR6M/0.jpg)](http://www.youtube.com/watch?v=4bV8BAOsR6M)

---

##  Basic Routes And Views

![What is it](Markdown_Images/whatis.png "what is")

## What is it

The main routes and views that we'll be using in our project

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

Allows us to send messages via our URLs

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By creating views that will handle those URLs

[![Basic Routes And Views](http://img.youtube.com/vi/xVuYl88-yhQ/0.jpg)](http://www.youtube.com/watch?v=xVuYl88-yhQ)

---

##   Storing Our Messages

![What is it](Markdown_Images/whatis.png "what is")

## What is it

A Python list

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

Allows us to store our messages as strings

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By appending an item to the list every time a new message is created

[![Storing Our Messages](http://img.youtube.com/vi/9TzsFe00pQM/0.jpg)](http://www.youtube.com/watch?v=9TzsFe00pQM)

---

## Presenting Our Messages

![What is it](Markdown_Images/whatis.png "what is")

## What is it

Displaying our chats messages

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

Renders our messages in the browser

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By outputting the messages as a string

### Oops! We have found an issue in this video

The underlying Flask libraries have been updated since this video was made. Therefore, the `return redirect(username)` code that we add from 0:39 in this video no longer works.

To rectify this, you need to change this line to the following:
`return redirect("/" + username)`

>**The Issue Above Is Currently Being Rectified. In The Meantime The Necessary Fix Is Highlighted Above. Apologies For Any Inconvenience This May Have Caused.**

The code is correct in the Source Code link beneath this video.

[![Presenting Our Messages](http://img.youtube.com/vi/qtI-mMN3-NU/0.jpg)](http://www.youtube.com/watch?v=qtI-mMN3-NU)

---

## Adding Timestamps

![What is it](Markdown_Images/whatis.png "what is")

## What is it

A timestamp

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

It will enable us to show the time at which the message was sent

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By using Python's datetime module

[![Adding Timestamps](http://img.youtube.com/vi/f0UDl23pfLo/0.jpg)](http://www.youtube.com/watch?v=f0UDl23pfLo)

---

##  Creating An Index.Html Page

![What is it](Markdown_Images/whatis.png "what is")

## What is it

The index.html page

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

It will display a form that will ask users for a username

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By creating the HTML page and handling the form submission on the backend

[![Creating An Index.Html Page](http://img.youtube.com/vi/CyaSQUjoIIU/0.jpg)](http://www.youtube.com/watch?v=CyaSQUjoIIU)

---

##  Creating Users

![What is it](Markdown_Images/whatis.png "what is")

## What is it

Storing Users in a session variable

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

Allows us to persist usernames in a browser session to automatically redirect users to their homepage

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By initialising a session and a variable

[![Creating Users](http://img.youtube.com/vi/miakE-jDNzo/0.jpg)](http://www.youtube.com/watch?v=miakE-jDNzo)

---

##  Storing Our Messages In A Dict

![What is it](Markdown_Images/whatis.png "what is")

## What is it

A dictionary

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

Allows us to store data using Key/Value pairs

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

my_dict = {}

[![Storing Our Messages In A Dict](http://img.youtube.com/vi/3e7AjN9eBAg/0.jpg)](http://www.youtube.com/watch?v=3e7AjN9eBAg)

---

##  Refactoring To Use Chat.Html Instead Of A Single String

![What is it](Markdown_Images/whatis.png "what is")

## What is it

An HTML file

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

It will display our chat messages

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By passing it the necessary chat messages

[![Refactoring To Use Chat.Html Instead Of A Single String
](http://img.youtube.com/vi/Rq7rC3GYgQw/0.jpg)](http://www.youtube.com/watch?v=Rq7rC3GYgQw)

---

## Simple Long Polling With JavaScript

![What is it](Markdown_Images/whatis.png "what is")

## What is it

Long polling

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

Refreshes the page after a specified period of time

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By using JavaScript's setTimeout function

[![Simple Long Polling With JavaScript](http://img.youtube.com/vi/o4qjxNvrpyw/0.jpg)](http://www.youtube.com/watch?v=o4qjxNvrpyw)

---

## Creating A Message Textbox

![What is it](Markdown_Images/whatis.png "what is")

## What is it

A textbox to allow us to enter a message instead of using the URL

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

Improves the functionality of our chat app

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By creating a textbox and using the POST form method

[![Creating A Message Textbox](http://img.youtube.com/vi/3CntDFdJS7I/0.jpg)](http://www.youtube.com/watch?v=3CntDFdJS7I)

---

##  Simplifying Our Code

![What is it](Markdown_Images/whatis.png "what is")

## What is it

Code refactoring

![What does it do](Markdown_Images/whatdoes.png "what does")

## What does it do

Simplifies our code

![How do you use it](Markdown_Images/howdo.png "how do")

## How do you use it

By making our code more understandable

[![Simplifying Our Code](http://img.youtube.com/vi/xzURhaMXjWY/0.jpg)](http://www.youtube.com/watch?v=xzURhaMXjWY)

# heoku
[![heroku](http://img.youtube.com/vi/URHT33CReYs/0.jpg)](http://www.youtube.com/watch?v=URHT33CReYs)

---

- requrements.txt
- create procfile
    - `echo web: run.py > Procfile`
- create new heroku app
- create config variables
