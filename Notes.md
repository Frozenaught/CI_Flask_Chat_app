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

