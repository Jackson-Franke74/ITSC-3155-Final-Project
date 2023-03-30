# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Neel Dadhania](mailto:ndadhani@uncc.edu)
* [Anushrut Neupane](mailto:aneupan1@uncc.edu)
* [Justin Mendoza](mailto:jmendo10@uncc.edu)
* [Jackson Franke](mailto:jfranke5@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
| 1.1 | 03/26/23 | Initial upload | [Justin Mendoza](mailto:jmendo10@uncc.edu) | [Justin Mendoza](mailto:jmendo10@uncc.edu) |
| 1.2 | 03/30/23 | Requirements 1-3 | [Anushrut Neupane](mailto:aneupan1@uncc.edu) | [Anushrut Neupane](mailto:aneupan1@uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

We will be building a multiplayer Trivia bot with a wide range of features. This will include rooms, leaderboards, difficulty levels, and many more. This can used with individuals seeking ways to study, or even initiate a friendly competition

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:
* **REQ-1: Multiplayer**
  * **Description:** The program will be able to create rooms for the user to be able to play with friends
  * **Type:**  Functional
  * **Priority:** 1
  * **Rationale:** It's in the name, this is a multiplayer trivia bot so multiplayer needs to be top prio.
  * **Testing:** We can test this by creating rooms and seeing if anything breaks when we start the trivia,
* **REQ-2: Different rooms with different categories**
  * **Description:** Our project needs to have different rooms where there will be different categories of trivia questions
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** We need to make sure that the bot itself functions and one category works for us to implement different categories. 
  * **Testing:** We can test this by advancing to another room and see different questions.
* **REQ-3: Leaderboards**
  * **Description:** A leaderboard feature to add some friendly competition to the mix
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** Need to make sure everything else works before trying to implement something that's not as important as multiplayer
  * **Testing:** We can test this feature by competing against each other and making sure that it sets the person with the higher score above the person that got the lesser score.

* **REQ-10**: Hint System
* **Description**: A system that asks user if they need help after having tried a question a certain number of times.
*  **Type**: Functional
*  **Priority**: 5
*  **Rationale**: User may not know the answer to the question and instead of choosing to move to the next question, they will also have an option to get a hint for the question.
*  **Testing**: A test function that checks that the hint provided is same as the hint related to the question in the database of hints.

* **REQ-11**: Random select feature
*  **Description**: A system which selects a random catagory for indecisive users
*  **Type**: Functional
*  **Priority**: 4
*  **Rationale**: User may not have a specific category they wish to play in, and this feature selects a random catogory for them.
*  **Testing**: A test function that checks that everytime a random catagory is begin selected when the user decides to activate the feature

* **REQ-12**: "Make your own" feature
*  **Description**: A feature that allows the user to create their own set of questions and answers to play locally with their teammates
*  **Type**: Functional
*  **Priority**: 4
*  **Rationale**: User may have a certain set of questions, with which they want to play the game and this function will allow them to do so.
*  **Testing**: A test function that will check if the questions are linked with the answers that were provided by user, and a function which checks that only the questions provided by the user are asked.


## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.

* **Neel**: The questions for the game will be pulled form an online database, whos API will have to be implimented in the project for smooth operations. Secondly the project template is of an online store, while we plan on making a trevia bot. We will have to make many changes to the templet to allow us to create such a bot.


## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **ID:** A unique identifier for the use case. This should be a number that is unique across the entire document (something like UC-1, UC-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A description of the use case that gives the user a high-level overview of how the system is interacted with.
  * **Actors:** A list of the actors that are involved in the use case. Only include the actors that are directly involved. Actors are the people or things that interact with the system. For example, when ordering at a fast food restaurant, one might have the following actors: the customer, the cashier, and the cook. But only the customer and the cashier are directly involved in the use case of ordering food. The cook is not directly involved in the use case of ordering food.
  * **Preconditions:** A list of the preconditions for the use case. This should be a list of the preconditions for the use case, which are the conditions that must be met before the use case can be executed. Continuing with the restaurant example, the customer must have money in their wallet and the cashier must be logged in to the system before the use case of ordering food can be executed.
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

* **UC-7**: Competative play
*  **Description**: User can decide to play competatively by not using the hint feature, thus making sure they are not hit with a point panelty when using the hint feature for the hint feature. The compatetive leader board will make not using the hint feature worth it as the users will aim to take the highest possible place on the board.
*  **Actors**: User
*  **Preconditions**: The user will need to have an account to be part of the leader board and the user must also be logged in for thier score to appear on the leader board.
*  **Postconditions**: The score, if applicable, must appear on the leader board

* **UC-8**: Locally playing with friends and family
*  **Description**: User can play a game with their own questions locally with a select group of people. The user(s) will be able to play competatively amoung the group with each user having their own score and a final place of 1st, 2nd and 3rd at the end of the game.
*  **Actors**: Users
*  **Preconditons**: The user will need an account and all the people in the group playing will also need an account.
*  **Postconditons**: The final score must be displayed at the end of the game while showing the top three scores


## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **ID:** A unique identifier for the user story. This should be a number that is unique across the entire document (something like US-1, US-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Type of User:** The type of user that the user story is for. This should be a single word that describes the type of user. For example, a user story for a customer might be `Customer` and a user story for an administrator might be `Admin`.
  * **Description:** A description of the user story that gives a narrative from that user's perspective. This can be any length, but it must paint the picture of what the user wants to do, how they intend to do it, why they want to, and what they expect to happen.

* **US-7**:
*  **Type of User**: Player
*  **Description**: After answering a question for three times without getting it right, the player is provided access to the hint button which gives a hint, helping the player answer the question. Using the hint button does have a point panelty which is deducted from your total score.

* **US-8**:
*  **Type of Users**: Players
*  **Description**: A group of players can join a local game in which the questions and thier answers are entered by the player before the game starts. Once the game starts the questions that are asked are from the list of questions entered before and the points of each user is kept track of. At the end of the game the top three scores are displayed from highest to the lowest.


## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** The term that is being defined. This should be a single word or phrase that is being defined.
  * **Definition:** A definition of the term. This should be a short description of the term that is being defined. This should be a single sentence that describes the term.

* **Player**:
*  **Definition**: The user playing the game
