# tDNA_IS Simple Version


## About this version:

While the original tDNA integrates advanced multifactorial inputs to tailor clinical practice guidelines and generate personalized nutrition and lifestyle recommendations, this project contains a simpler risk stratification and more basic nutrition recommendations.

This program does the following:
1. Reads patient data from a CSV file
2. Creates Patient objects
    * By reading information from file or obtaining new patient data via user input through prompts
        * If user adds new patient, the program adds the information to the CSV file
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
    * Antihypertensive diet guidelines if patient has “hypertension” in their risk factors
5. Validates and tests functions and methods


## How to use:

This program can be executed by ensuring the following 6 files are saved in the same folder:
1. *main_tDNA.py*
2. *patient_manager.py*
3. *patient.py* 
4. *foods_gi.py*
5. *mock_patients.csv*
6. *antihypertensive_diet.txt*

The program only utilizes the built-int modules *datetime*, *csv*, and *os*. No installation of third-party modules is necessary. 

To use program, open *main_tDNA.py* and run the file. The program has a user-friendly interface with prompts that provide options to navigate through the different features. 

The core functionalities that the interface will offer are:
- Add a new patient
- Select an existing patient
- Generate a recommendations handout
- Update patient
- Exit the program

### Unit Test File:

There is an additional 7th file called *unit_test_tDNA.py* which contains functions that test core methods and functions of the program. This file is not needed to run the program, but the other 6 files are necessary to run this unit test file. 

The unit test file has lines of code that automatically delete any files created while running the tests. To avoid test files from automatically deleting, convert to comments the code lines 352, and 404-406.
