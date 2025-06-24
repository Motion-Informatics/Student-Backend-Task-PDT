# Student-Backend-Task: Background

We are a digital healthcare company specializing in developing innovative therapeutic solutions for Parkinson’s disease. Parkinson’s is a progressive neurodegenerative disorder that affects movement and quality of life. Our product combines physical therapy protocols with real-time data collection to help track patient progress and optimize treatment plans.

As part of this effort, we are building a web-based application that allows therapists to manage and monitor their patients’ sessions. The backend system you’ll be working on is the foundation of that therapist-facing interface. It is responsible for:
- Storing patient and user data.
- Recording session information.
- Providing endpoints for basic operations (e.g., adding a new patient, registering a user, etc.).

This task simulates a real-world backend challenge at our company. You are not expected to build the entire application from scratch. Instead, you will be provided with a ready-to-use project skeleton inside a Dockerized Flask environment, which includes a preconfigured local SQLite database. Your responsibility is to complete specific parts of the implementation and demonstrate your understanding of backend development principles.

## 🚀 What You’ll Be Learning (and Demonstrating)

This task is designed to test and strengthen your understanding of:

- ✅ **Flask application architecture:** how routes, models, and handlers work together.
- ✅ **API design and HTTP request handling.**
- ✅ **Working with Docker images** and running services in isolated containers.
- ✅ **Using SQLite** as a lightweight, file-based relational database, stored locally within the container environment.
- ✅ **Writing unit tests** to validate functionality and logic correctness.

You don’t need to set up Docker or Flask from scratch, but you do need to understand how they work and how to use them effectively.

## 🛠️ Environment Setup (Windows/PowerShell)

1. **Install Docker**  
   You will need Docker installed on your machine to run the backend environment.  
   - If you don’t have Docker, please [download and install it from the official website](https://www.docker.com/get-started/).
   - Follow the installation instructions for your operating system.
   - You should register new account with your personal Email if not exist already.

2. **Install Python**  
   You will need Python installed on your machine to run utility scripts and unit tests.  
   - Download and install the latest version of Python from the [official Python website](https://www.python.org/downloads/).
   - Make sure to add Python to your system's environment PATH during installation so you can run `python` or `python3` from the terminal.

3. **Clone the Repository**  
   Clone this repository to your local machine using the following command (replace the link with the actual repository URL when available):

   ```powershell
   git clone --branch Student-Backend-Task-PDT-Windows https://github.com/Motion-Informatics/Student-Backend-Task-PDT.git
   ```

4. **Set Up a Local Python Virtual Environment**  
   Before running Python scripts or installing dependencies, you should create and activate a Python virtual environment (`venv`).  
   This ensures all Python packages are installed in an isolated environment specific to this project.

   **What is a Python Virtual Environment?**  
   A Python virtual environment (`venv`) is an isolated workspace on your system where you can install Python packages and dependencies specific to a project, without affecting other projects or the global Python installation. This helps prevent version conflicts and makes it easier to manage project-specific requirements.  
   When you activate a virtual environment, any Python packages you install or run will be contained within that environment.

   To set up and activate the virtual environment, run the following commands from the project root:

   ```bash
   # Create virtual environment
   python3 -m venv venv

   # For Windows PowerShell, use:
   # venv\Scripts\Activate.ps1

   # For Windows Command Prompt (cmd.exe), use:
   # venv\Scripts\activate.bat

   # Install required dependencies
   pip install -r requirements.txt
   ```

   If you see the environment name (usually `(venv)`) at the beginning of your terminal prompt, the virtual environment is active.  
   If it is already active, you can skip the activation step.


5. **Build the Docker Image**  
   In the root of the project, there is a PowerShell script called `build.ps1` that you need to run in order to build the Docker image for the backend environment.

   Open PowerShell, navigate to the project root directory, and run:

   ```powershell
   .\build.ps1
   ```

   This script will execute the necessary Docker build command for you.  
   The contents of `build.ps1` are as follows:

   ```powershell
   docker build -t student-backend-task .
   ```

   After the build completes, your Docker image will be ready to use.

6. **Deploy the Environment**  
   After building the Docker image, you can deploy the backend environment using the `deploy-local.ps1` script located in the project root.

   This script will start a Docker container based on the image you just built, mapping the necessary ports and mounting the database volume for local development and testing.

   To run the script, use:

   ```powershell
   .\deploy-local.ps1
   ```

   The script will:
   - Map port **9000** on your local machine to port **8080** in the container
   - Mount the local `database` folder into the container at `/var/task/database`
   - Start the container using the `pdt-backend-task` image



7. **Initialize the Database**  
   After deploying the environment, you need to initialize the database using the provided Python script.

   The initialization script is located in the `root` folder and is called `init_db.py`.  
   This script will set up the necessary tables and seed any initial data required for the backend to function.

   To run the script, use:

   ```powershell
   python init_db.py
   ```

   Make sure your Docker container is running before executing this step.

8. **Environment Ready**

At this point, your backend environment is fully set up and running on your local computer.  
You can now proceed to work on the required tasks as described in the assignment.

🛠️ **Utility Scripts Overview**

To help you work efficiently with the backend environment, several utility scripts are provided in the `playground` folder:

- **db_usage_example.py:**  
  This script demonstrates how to connect to the SQLite database from Python.  
  It will connect you to the database and allow you to execute regular SQL commands.  
  You can use it as a reference for establishing database connections and performing basic operations.

- **open_sqlite.ps1:**  
  This is a PowerShell script that, when run, will open an interactive SQLite prompt connected to the project database.  
  You can use this prompt to run SQL queries directly, insert new data, or retrieve information from the database for testing and debugging purposes.

- **test_route_example.ps1:**  
  This PowerShell script provides an example of how to make an HTTP request to the backend API.  
  Specifically, it demonstrates how to test the "add patient" endpoint using a sample request.  
  You can use this script as a template for testing other API routes as well.

- **notes.md:**  
  This markdown file contains a collection of basic PowerShell and command-line commands that can help you navigate and work through this task more efficiently.  
  Refer to it whenever you need a quick reminder or example of useful terminal commands.

---
💡 **Recommendation:**  
For the best development experience, we recommend using [Visual Studio Code (VS Code)](https://code.visualstudio.com/) as your code editor, along with its integrated terminal or PowerShell. This setup makes it easy to run scripts, interact with the backend, and manage your code efficiently.


## 📝 Task Overview

The task is divided into two main parts, plus an optional bonus. Let's start with the first part:

### Part 1: Implement API Route Logic

Your first task is to complete the logic for four API routes.  
These routes are already defined as empty functions, and you will find them in the `app/routes` directory. Each file contains comments and instructions describing the required logic and validation for that specific route.

**What you need to do:**
- Locate the four API route files inside `app/routes`.
- Read the instructions and requirements provided in each file.
- Implement the logic for each route, including input validation and appropriate responses as described in the comments.

Take your time to understand the requirements for each route before you start coding.

> **Note:**  
> After making any changes to the code, you should run the `build.ps1` script again to rebuild the Docker image, and then redeploy the environment using `deploy-local.ps1`.  
> The database and its data will remain unchanged during this process.

### Part 2: Create Unit Tests for the API Routes

The second part of the task is to write unit tests in Python for the four API routes you implemented.

- You will find a `tests` folder in the project, which contains four subfolders—one for each route.
- For each route, create one or more unit tests that you think are important. Consider different scenarios, such as valid input, invalid input, missing fields, and edge cases.
- Your tests should be meaningful and should work (i.e., they should pass or fail appropriately based on your implementation).

**Examples:**  
In the `add_patient` and `add_user` folders, you will find two example test files:
- One example shows how to check the status code returned by the API.
- The other example demonstrates how to check the data returned from the database after making a request.

Use these examples as a reference for writing your own tests for all four routes.

**How to run your unit tests:**  
You can use [pytest](https://docs.pytest.org/) to run your unit tests from the terminal.  
For example, to run all tests in a specific test file, use:

```
pytest <test_file>.py
```

Or, to run all tests in the `tests` directory:

```
pytest tests/
```

## ⭐ Bonus Tasks

If you want to challenge yourself further, here are three optional bonus tasks:

1. **Add Logging:**  
   Add meaningful logs throughout your route logic.  
   Log important events, errors, and decision points in your code to help with debugging and traceability.  
   (Logging is not required in your unit tests.)

2. **Refactor Using Utils:**  
   In the `utils` folder, you will find four utility files—one for each API route.  
   As a bonus, move as much logic as possible from your route handlers into these utility files by implementing the necessary functions.  
   The goal is to keep your route functions very simple, delegating all processing and validation to the utility functions.

3. **Custom Status Codes:**  
   Implement custom return status codes in your API responses (in addition to the standard HTTP status codes).  
   These should be unique codes (at least five digits) that can help identify specific issues or scenarios for each route.  
   Choose and document your codes as you see fit, ensuring each scenario is clearly represented.

   4. **Use Git Integration:**  
   Create a branch with your ID number.<br>
   Make meaningful commits.<br>
   Use clear, descriptive commit messages and maintain a clean commit history. <br> 
   Good version control practices are a plus!<br>
   Push access will be enabled for a 30-minute window at the final date of the task.<br>

---

## 📝 Final Notes

As you work on this task, please keep the following in mind:

- **Clarity and Organization:**  
  Write your code in a clear and organized manner. Structure your files and functions so that it’s easy for others to follow your logic.

- **Simplicity:**  
  Aim for simple, readable solutions. Avoid overcomplicating your code—straightforward logic is best.

- **Meaningful Comments:**  
  Add detailed comments throughout your code to explain what each part does and why. Good comments help others (and your future self) quickly understand your approach and reasoning.

- **Use Any Tools You Need:**  
  You are welcome to use any tools that help you complete the task, including AI tools, database visualization helpers, or any other resources that make your work easier and more effective.

Your attention to these details will make your work stand out and ensure it’s easy to review and maintain.

---

## 🌟 Final Words

I know this is a lot to handle, and there may be things in this task that you haven’t seen or worked with before. That’s exactly the point—this exercise is not just about writing logic, but about seeing how you approach new services and infrastructures for the first time.

Please don’t hesitate to contact me if you have questions or need help with anything. I’m here to support you throughout the process.

You can contact me at:  
📞 054-5638066 <br>
✉️ shawn@motioninformatics.ai

Good luck, and I look forward to seeing your work!