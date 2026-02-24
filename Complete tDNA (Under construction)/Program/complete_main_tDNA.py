'''
COMPLETE VERSION

The program runs mock tDNA by requesting user input, and
calling methods and functions from patient_manager.py and foods_gi.py

Input: User input
Output: Generates personalized handout with recommendations for a given patient

'''

from foods_gi import get_formatted_foods
import patient_manager

from datetime import datetime
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

###############################################################################
###############################################################################


#FUNCTIONS

def main_menu(pt_manager):
    """Main menu for adding or selecting a patient"""
    print()
    print("*" * 10 ,"MAIN MENU", "*" * 10)

    while True:
        user_choice = input(
            f"\nWhat would you like to do?\n"
            f"  (1) Add a new patient\n"
            f"  (2) Select an existing patient\n"
            f"  > Enter your choice: "
        ).strip()

        if user_choice == "1":
            patient = pt_manager.add_new_patient()
            return patient  #Return selected patient

        elif user_choice == "2":
            patient = pt_manager.select_patient()
            if patient is not None:
                return patient  #Return selected patient
            else:
                print("No patient was selected.\n")
                # Loop continues

        elif user_choice.lower() == "x":
            return None  #Exit the outer program loop

        else:
            print("Invalid choice. Please enter 1, 2, or 'x' to exit.")


def patient_menu(patient):
    """Handles actions for the selected patient"""
    print()
    print("*" * 10 ,"PATIENT MENU", "*" * 10)

    while True:
        user_choice = input(
            f"\nWhat would you like to do next?\n"
            f"  (1) Generate a recommendations handout for '{patient.name}'\n"
            f"  (2) Update patient '{patient.name}' information\n"
            f"  (3) Select a different patient\n"
            f"  (x) Exit the program\n"
            f"  > Enter your choice: "
        ).strip()

        if user_choice == "1":
            generate_rec_handout(patient)
            while True:
                next_action = input(
                    f"Would you like to do now?\n"
                    f"  (1) Go back to main menu\n"
                    f"  (x) Exit the program\n"
                    f"  > Enter your choice: "
                ).strip().lower()
                if next_action == "1":
                    return "switch"
                elif next_action == "x":
                    return "exit"
                else:
                    print("Invalid choice. Please try again.")

        elif user_choice == "2":
            return "update"
        elif user_choice == "3":
            return "switch" #Go back to main_menu()
        elif user_choice.lower() == "x":
            return "exit"

        else:
            print("Invalid choice. Please try again.")

def update_pt_info_menu(patient):
    """Handles user interactions for updating patient info."""

    print("*" * 10, "UPDATING PATIENT MENU", "*" * 10)

    while True:
        user_choice = input(
            f"\nWhat would you like to update?\n"
            f"  (1) Name\n"
            f"  (2) BMI\n"
            f"  (3) Waist Circumference\n"
            f"  (4) Risk Factors\n"
            f"  (m) Go back to patient menu\n"
            f"  > Enter your choice: "
        ).strip()

        if user_choice == "1":
            pt_manager.update_pt_info(patient, "name")
        elif user_choice == "2":
            pt_manager.update_pt_info(patient, "bmi")
        elif user_choice == "3":
            pt_manager.update_pt_info(patient, "wc_cm")
        elif user_choice == "4":
            pt_manager.update_pt_info(patient, "risk_factors_list")
        elif user_choice.lower() == "m":
            return  # Go back to patient menu
        else:
            print("Invalid choice. Please try again.")

def generate_rec_handout(patient):
    """
    Generates new file for given patient.
    Writes patient-specific recommendations
    """
    
    # 1. Prep file
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    base_name = f"{patient.name.replace(' ', '_')}_recommendations"
    file_name = f"{base_name}.txt"
    version = 1

    # 1.1 Check if file exists and create versioned name if needed
    while os.path.exists(file_name):
        file_name = f"{base_name}_v{version}.txt"
        version += 1

    #2. Write patient info into file
    recs_file = open(file_name, "w")
    recs_file.write(f"Visit Date and Time: {now}\n\n")
    recs_file.write("-" * 80)
    recs_file.write("\nPATIENT INFORMATION:\n\n")
    recs_file.write(str(patient) + "\n\n")
    recs_file.write("-" * 80)

    #3. Obtain formated string of list of foods
    
    formatted_foods = get_formatted_foods(patient.recs)

    #3.1 Write into file
    recs_file.write(
        "\nCOMMON INTERNATIONAL FOODS WITH THEIR GLYCEMIC INDICES:\n\n"
    )
    recs_file.write(formatted_foods)
    recs_file.write("\n")

    #5. Write antihypertensive diet if required
    if "Antihypertensive diet" in patient.recs:
        try:
            antihy_file_path = os.path.join(SCRIPT_DIR, "antihypertensive_diet.txt")
            antihy_file = open(antihy_file_path, "r")
            content = antihy_file.read()
            recs_file.write("-" * 80)
            recs_file.write("\n")
            recs_file.write(content)
            antihy_file.close()
        except FileNotFoundError:
            recs_file.write(
                "\n***Could NOT attach 'antihypertensive_diet.txt': "
                "file not found.***\n"
            )

    recs_file.close()
    print(f"\nA handout was generated for "
          f"'{patient.name}' called '{file_name}'\n")


###############################################################################
###############################################################################

#MAIN PROGRAM

if __name__ == "__main__":
    FILE_NAME = os.path.join(SCRIPT_DIR, "mock_patients.csv")
    PREDEFINED_RISKS = [
            "family/patient history of cardiovascular event",
            "hypertension",
            "dyslipidemia",
            "low activity"
        ]
    print("~" * 80)
    print()
    print("-" * 29 ,"Welcome to mock-tDNA", "-" * 29)

    pt_manager = patient_manager.PatientManager(FILE_NAME, PREDEFINED_RISKS)

    while True:
        patient = main_menu(pt_manager)
        if patient is None:
            print("No patient selected. Exiting.")
            break

        #Continues working with selected patient until user wants to switch/exit
        while True:
            user_done = patient_menu(patient)
            if user_done == "switch":
                break  #Goes back to main_menu()
            if user_done == "update":
                update_pt_info_menu(patient)
            elif user_done == "exit":
                print("\nYou have exited the mock-tDNA program.\n")

                print("-" * 29 ,"End of mock-tDNA", "-" * 29)
                print()
                print("~" * 80)
                exit()
   

    


    

    








    
