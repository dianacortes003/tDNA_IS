# tDNA_IS Simple Version


## About this version

While the original tDNA integrates advanced, multifactorial inputs to tailor clinical practice guidelines and generate personalized nutrition and lifestyle recommendations, this project includes simpler risk stratification and more basic nutrition recommendations.

This program does the following:
1. Reads patient data from a CSV file
2. Creates Patient objects
    * By reading information from a file or obtaining new patient data via user input through prompts
        * If the user adds a new patient, the program adds the information to the CSV file
    * Patient class does the following:
        * Determines BMI category and diabetes risk level
        * Personalizes recommendations
3. Updates Patient objects
    * Obtains data to be updated via user input through prompts
    * Updates the CSV file
4. Generates a personalized text file containing:
    * Date of mock visit
    * Patient information, risk profile, and tailored recommendations
    * List(s) of common international foods with their respective glycemic index (GI)
        * Lists are categorized by high, medium, and low GI.
        * Patients get low GI list only if “Follow low-GI diet” is recommended
    * Antihypertensive diet guidelines if the patient has “hypertension” in their risk factors
5. Validates and tests functions and methods

A full example of the program in action is available in the [Simple tDNA Samples](https://github.com/dianacortes003/tDNA_IS/tree/main/Simple%20tDNA%20Version/Simple%20tDNA%20Samples) section. 

## How to use

>The program only utilizes the built-in modules `datetime`, `csv`, and `os`. **No installation of third-party Python modules is necessary**.


To run this program locally:
1. Download [Simple tDNA Program](https://github.com/dianacortes003/tDNA_IS/tree/main/Simple%20tDNA%20Version/Simple%20tDNA%20Program) folder or clone this repository to your local machine.
2. Open the project folder in a code editor such as Cursor or Visual Studio Code.
3. Ensure the following 6 files are located in the same directory:

   - `main_tDNA.py`
   - `patient_manager.py`
   - `patient.py`
   - `foods_gi.py`
   - `mock_patients.csv`
   - `antihypertensive_diet.txt`

4. Run `main_tDNA.py` from the terminal to start the program.

>This project was designed following Object-Oriented Programming (OOP) principles. The supporting modules (e.g., `patient_manager.py`, `patient.py`) define classes and supporting logic and are not intended to be executed directly. **The program should be run EXCLUSIVELY through `main_tDNA.py`.**


The program has a user-friendly interface with prompts that provide options for navigating its different features.

The core functionalities that the interface will offer are:
- Add a new patient
- Select an existing patient
- Generate a recommendations handout
- Update patient
- Exit the program

### Unit Test File

The project's folder contains a 7th file, `unit_test_tDNA.py`, which defines functions that test the program's core methods. This file is not needed to run the program, but the other 6 files are required to run this unit test. 

The unit test file includes lines of code that automatically delete any files created during test execution. To avoid test files from automatically deleting, convert to comments the code lines 352, and 404-406.
