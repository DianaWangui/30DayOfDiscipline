# Welcome to my 30 Days of Discipline Repo:

I will use this repo to code and learn daily for 30 days and document things I have learnt

.
.
.

Quiz Game (https://github.com/DianaWangui/30DayOfDiscipline/blob/main/python/Quiz_game_class.py)

# PROJECT 1

# Quiz Game with Classes (PROJECT 1)

This Python script implements a simple quiz game using classes. The game consists of a set of questions with multiple-choice answers, and the player's score is calculated based on the correctness of their answers.

## Classes

### `Quiz` Class

The `Quiz` class represents the collection of questions and choices for the quiz. It has the following attributes:

- `questions`: A list of dictionaries, where each dictionary contains a quiz question and its correct answer.
- `choices`: A list of lists, where each inner list contains the multiple-choice options for a corresponding question.

### `Score` Class

The `Score` class handles the scoring mechanism for the quiz. It takes a `Quiz` instance as a parameter during initialization. The class has the following methods:

- `__init__(self, quiz)`: Initializes the `Score` class with a reference to the `Quiz` instance and sets the initial score to zero.

- `check_user_answer(self, user_answer, correct_answer)`: Checks if the user's answer matches the correct answer and returns a boolean value.

- `play_quiz(self)`: Initiates the quiz game, prompting the user to answer each question and updating the score accordingly.

- `display_score(self)`: Displays the final score after completing the quiz.

## Main Execution

The script starts by printing a welcome message and creating instances of the `Quiz` and `Score` classes. It then calls the `play_quiz` method to start the quiz game. After completing the quiz, the final score is displayed using the `display_score` method.

## Usage

To run the script, execute it as a standalone program. The user will be prompted to answer each quiz question, and the final score will be displayed at the end.

## Others

I created another file that works the same as the above but very basic
I used it to understand the basics of the game.
Here (https://github.com/DianaWangui/30DayOfDiscipline/blob/main/python/quiz_game.py)

The game can accomodate other questions, I only used two questions when I implemented this

# PROJECT 2

# University Simple Project Using Abstraction (PROJECT 2)

This Python project demonstrates the concept of abstraction in object-oriented programming using abstract classes and
methods. The code models entities in a university, such as courses, branches, and students, showcasing the organization and structure provided by abstraction.

## Abstraction in Object-Oriented Programming

Abstraction is a key principle in object-oriented programming that involves simplifying complex systems by modeling classes based on essential features and hiding unnecessary details. In Python, abstraction is often implemented using abstract classes and methods.

## Code Structure

The code consists of the following components:

### `University` (Abstract Base Class)

- Represents a university with an abstract method `get_uni_name()`.

### `Course` and `Branch` (Concrete Classes)

- Concrete classes representing a university course and branch, respectively.
- Inherit from the abstract class `University` and implement the abstract method.
- Introduce additional methods (`get_course_name()` and `get_branch_name()`).

### `Student` (Concrete Class with Multiple Inheritance)

- Represents a student enrolled in a course and branch.
- Inherits from both `Course` and `Branch`, demonstrating multiple inheritance.
- Initializes attributes and introduces a method (`student_details()`) to print student details.

## Usage Example

Instantiate a `Student` object, providing information such as university name, course, branch, student name, and registration number. Call the `student_details()` method to print the student's details.

project link(https://github.com/DianaWangui/30DayOfDiscipline/blob/main/python/university_abstraction.py)
link 2(https://github.com/DianaWangui/30DayOfDiscipline/blob/main/python/main_abs.py)

# Project 3

## Duck Typing and Polymorphism in Python

This repository explores the concepts of Duck Typing and Polymorphism in Python through illustrative code examples. The main purpose is to showcase how Python's dynamic typing and object-oriented features allow for flexible and reusable code.

## Duck Typing

Duck typing is a principle in Python where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type. The provided examples demonstrate how different classes can share common behavior, allowing them to be used interchangeably.

## Operator Overloading

Python supports operator overloading, enabling the same operator to behave differently based on the operands involved. The code includes an example of operator overloading using the `Complex` class to illustrate the customization of the `+` operator for complex numbers.

## Polymorphism

Polymorphism is a fundamental concept in object-oriented programming that allows objects of different types to be treated as objects of a common type. The code showcases polymorphism through method overloading and overriding, emphasizing the flexibility and adaptability of Python's object-oriented paradigm.

### Method Overloading

Method overloading is demonstrated using the `Override` class, which provides multiple implementations of a method, either by accepting a different number of arguments or using default values.

### Method Overriding

Method overriding is showcased with the `Person` class, where a subclass provides a specific implementation for a method that is already defined in its superclass. This enhances the customization and extensibility of class behavior.

Link (https://github.com/DianaWangui/30DayOfDiscipline/blob/main/python/Polymorphism/method_overloading.py)
