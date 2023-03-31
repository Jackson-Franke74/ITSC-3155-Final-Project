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
| 1.3 | 03/30/23 | Requirements 4-6 | [Justin Mendoza](mailto:jmendo10@uncc.edu) | [Justin Mendoza](mailto:jmendo10@uncc.edu) |
| 1.4 | 03/30/23 | Constrains, User Stories, Glossary | [Anushrut Neupane](mailto:aneupan1@uncc.edu) | [Anushrut Neupane](mailto:aneupan1@uncc.edu) |
| 1.5 | 03/30/23 | Constraints, UC 5-6, US 5-6. , glossary | [Justin Mendoza](mailto:jmendo10@uncc.edu) | [Justin Mendoza](mailto:jmendo10@uncc.edu) |
| 1.6 | 03/30/23 | Requirements 7-9 | [Jackson Franke](mailto:jfranke5@uncc.edu) | [Jackson Franke](mailto:jfranke5@uncc.edu) |

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
  * **Type:**  `Functional`
  * **Priority:** 1
  * **Rationale:** It's in the name, this is a multiplayer trivia bot so multiplayer needs to be top priority.
  * **Testing:** We can test this by creating rooms and seeing if anything breaks when we start the trivia,
* **REQ-2: Different rooms with different categories**
  * **Description:** Our project needs to have different rooms where there will be different categories of trivia questions
  * **Type:** `Functional`
  * **Priority:** 3
  * **Rationale:** We need to make sure that the bot itself functions and one category works for us to implement different categories. 
  * **Testing:** We can test this by advancing to another room and see different questions.
* **REQ-3: Leaderboards**
  * **Description:** A leaderboard feature to add some friendly competition to the mix
  * **Type:** `Functional`
  * **Priority:** 3
  * **Rationale:** Need to make sure everything else works before trying to implement something that's not as important as multiplayer
  * **Testing:** We can test this feature by competing against each other and making sure that it sets the person with the higher score above the person that got the lesser score.
* **REQ-4:**
  * **Description:** A timed mode where it gives you questions and you have to answer within a certain time limit
  * **Type:** `Functional`
  * **Priority:** 1
  * **Rationale:** This requirement is a necessary need for the purpose of the Trivia bot.
  * **Testing:** Wether or not a timed countdown will be initiated.
* **REQ-5:**
  * **Description:** A presentable multiple choice mode
  * **Type:** `Functional`
  * **Priority:** 1
  * **Rationale:** The system will present a multiple choice format for the questions purpose.
  * **Testing:** Whether or not a series of answers will show up or not.
* **REQ-6:**
  * **Description:** A free response mode for open ended questions
  * **Type:** `Functional`
  * **Priority:** 1
  * **Rationale:** A mode for users to initiate in the trivia bot 
  * **Testing:** Whether or not users can answer presented questions freely in this specific mode. 
* **REQ-10**: Hint System
  * **Description**: A system that asks user if they need help after having tried a question a certain number of times.
  *  **Type**: Functional
  *  **Priority**: 5
  *  **Rationale**: User may not know the answer to the question and instead of choosing to move to the next question, they will also have an option to get a hint for the question.
  *  **Testing**: A test function that checks that the hint provided is same as the hint related to the question in the database of hints.
* **REQ-11**: Random select feature
  *  **Description**: A system which selects a random category for indecisive users
  *  **Type**: Functional
  *  **Priority**: 4
  *  **Rationale**: User may not have a specific category they wish to play in, and this feature selects a random category for them.
  *  **Testing**: A test function that checks that every time a random category is begin selected when the user decides to activate the feature
* **REQ-12**: "Make your own" feature
  *  **Description**: A feature that allows the user to create their own set of questions and answers to play locally with their teammates
  *  **Type**: Functional
  *  **Priority**: 4
  *  **Rationale**: User may have a certain set of questions, with which they want to play the game and this function will allow them to do so.
  *  **Testing**: A test function that will check if the questions are linked with the answers that were provided by user, and a function which checks that only the questions provided by the user are asked.

## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.

* **Neel**: The questions for the game will be pulled form an online database, who's API will have to be implemented in the project for smooth operations. Secondly the project template is of an online store, while we plan on making a trivia bot. We will have to make many changes to the template to allow us to create such a bot.

* **Jackson**: To implement the difficulty levels, each question will need a difficulty rating, which means we will need a way of determining how hard a question is. Another is to implement the social media sharing aspect, we will have to design a way to format the scores in a graphic or a text message, etc.

* **Justin**: With our Trivia bot we must enforce formatting as this can be subject of hindering results of the game. Another constraint can be debating which of our features will be completed at each phase. Time and bot input will be a dictating factor on this.

* **Anush:**: Something that we might have to deal with is the possibility that the questions might be a little too obtuse or difficult for the players. This might be solved with the hint system. Another would be that he bot might not be able to recognize the answers given for the free response questions by the users. This might be solved by formatting it before feeding it to the bot to be checked. 

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **UC-1** Pass-time 
  * **Description:** A user might just want to pass some time by challenging themselves and playing alone. They might choose different categories to do themselves and add their score to the leaderboard.
  * **Actors**: User
  * **Preconditions:** User needs to be logged in.
  * **Postconditions:** The score needs to be shown in the leaderboard. 

* **UC-2** Review
  * **Description** A user might use the feature to create your their own set of answers and questions to review for an upcoming test or to study for the final exams
  * **Actors:** User
  * **Preconditions:** User needs to be logged in to be able to create their own set of questions
  * **Postconditions:** The questions and answers need to show up like any other trivia question would in a specific category.

* **US-3** Multiplayer game
  * **Description:** A user wants to play with their friend on the other side of town, so they send a code to their friend, and they both join the same game (like a kahoot)
  * **Actors:** Users
  * **Preconditions:** Both users must have accounts, and a game room must be made so they can join and play together in a coordinated effort
  * **Postconditions:** Scores must be displayed for both users, and a winner declared. 

* **US-4** Score share
  * **Description:** User wants to go back through the game and show a friend their score, without having to play the entire game again. They log in, and their high score appears.
  * **Preconditions** User must have an account and have played the game at least once before
  * **Postcondidtions** User's score must be correctly displayed and be able to be shared if necessary. (Maybe have a home screen with high score displayed?)

* **UC-5:** Study
  * **Description:** User is looking to use this for studying a particular set of questions they have set up.
  * **Actors:** Users
  * **Preconditions:** There will need to be questions set ahead of time as well the type of questions being asked.
  * **Postconditions:** What the user got correct and wrong so they can go back and study more.

* **UC-6:** Class quiz
  * **Description:** Presenter takes the game and present trivia questions to gauge knowledge retention. Using results changes can be made and questions adjusted for later scenarios.
  * **Actors:** Presenter, Users
  * **Preconditions:** Accounts to be set up and users added in to record result information from all. There will need to be questions set ahead of time as well the type of questions being asked.
  * **Postconditions:** Presenter is provided the information of the game. Also what the users got correct and wrong. 

* **UC-7** Competitive play
  *  **Description**: User can decide to play competitively by not using the hint feature, thus making sure they are not hit with a point penalty when using the hint feature for the hint feature. The competitive leader board will make not using the hint feature worth it as the users will aim to take the highest possible place on the board.
  *  **Actors**: User
  *  **Preconditions**: The user will need to have an account to be part of the leader board and the user must also be logged in for their score to appear on the leader board.
  *  **Postconditions**: The score, if applicable, must appear on the leader board

* **UC-8** Locally playing with friends and family
  *  **Description**: User can play a game with their own questions locally with a select group of people. The user(s) will be able to play competitively among the group with each user having their own score and a final place of 1st, 2nd and 3rd at the end of the game.
  *  **Actors**: Users
  *  **Preconditons**: The user will need an account and all the people in the group playing will also need an account.
  *  **Postconditons**: The final score must be displayed at the end of the game while showing the top three scores

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **US-1**
  * **Type of user:** Player
  * **Description:** Trying to challenge themselves, the player started a session to see how well they do in a category that they don't have too much experiece in.

* **US-2**
  * **Type of user:** Player
  * **Description:** A parent, planning a fun night with their kids might select or make their own category to challenge other family members. 

* **US-3**
  * **Type of user:** Player
  * **Description:** User is playing the match variation of the game, they assign each of their answers and hit enter. The game says that 2 of their answers are incorrect. The user switches the two answers, and hits enter again. The game now says that all answers are correct, and moves on to the next question, albeit with less points given to the user because they got the question wrong on the first try.

* **US-4**
  * **Type of user:** Player
* **Description:** The user has just finished the game, and wants to display their score on their instagram story. They click share, and a graphic pops up displaying their final score, how many questions they got right, total time taken, etc.

* **US-5**:
  *  **Type of User**: Presenter
  *  **Description**: After leading a game of different players the presenter can take use of the game information with results. Ranging from what was answered correctly to what was wrong with metrics. 

* **US-6**:
  *  **Type of User**: Presenter
  *  **Description**: Presenter is hosting a fun game with different players as a social activity. This include random and fun interesting questions to keep all that are involved engaged throughout. 

* **US-7**:
  *  **Type of User**: Player
  *  **Description**: After answering a question for three times without getting it right, the player is provided access to the hint button which gives a hint, helping the player answer the question. Using the hint button does have a point penalty which is deducted from your total score.

* **US-8**:
  *  **Type of Users**: Players
  *  **Description**: A group of players can join a local game in which the questions and their answers are entered by the player before the game starts. Once the game starts the questions that are asked are from the list of questions entered before and the points of each user is kept track of. At the end of the game the top three scores are displayed from highest to the lowest.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Player**:
  *  **Definition**: The user playing the game
* **Presenter**:
  *  **Definition**: Leader distributing game
