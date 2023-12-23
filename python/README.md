# Welcome to my 30 Days of Discipline Repo:

I will use this repo to code and learn daily for 30 days and document things I have learnt

.
.
.

Quiz Game (https://github.com/DianaWangui/30DayOfDiscipline/blob/main/python/Quiz_game_class.py)

# Quiz Game with Classes

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

# University Simple Project Using Abstraction

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
