# Quizzler_Application

This is a Python-based Quiz Application that utilizes the Tkinter library for the graphical user interface (GUI) and a Quiz API to fetch questions. The application is built using Object-Oriented Programming (OOP) principles.


# Features

Dynamic Question Fetching: The application fetches 20 questions from a Quiz API at runtime.
Interactive GUI: A user-friendly interface built with Tkinter.
Real-time Scoring: After answering all 20 questions, the application displays the user's final score.
OOP Implementation: The project is structured using OOP principles, ensuring scalability and code reusability.


# Usage

Launch the application: Run the main.py file, and the GUI will start.
Start the Quiz: The application will automatically fetch 20 questions from the Quiz API.
Answer Questions: The questions will be displayed one by one. Choose your answer and proceed to the next question.
View Final Score: After all questions are answered, your final score will be displayed.


# Project Structure

quiz-application/
│
├── main.py               # Entry point of the application
├── quiz_api.py           # Handles the API requests and data parsing
├── gui.py                # Manages the Tkinter GUI components
├── quiz_manager.py       # Implements the core quiz logic using OOP
├── requirements.txt      # Lists the project dependencies
└── README.md             # Project documentation
