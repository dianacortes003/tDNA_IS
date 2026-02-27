'''
The program contains attributes and methods of the class PatientManager.
Controls operations requested by main_tDNA and calls methods from patient.py

Input: Patient data in CSV file
Output: Patient data
 
'''

from patient import Patient

import csv, os, string

###############################################################################
###############################################################################


class PatientManager:
    def __init__(self, file_name, predefined_risks):
        self.file_name = file_name
        self.predefined_risks = predefined_risks

    def import_patients(self, file_name):
        """
        Extracts patient data from CSV file.
        Creates a list of Patient objects.
        Returns error if file name not found
        """
        
        patients_list = []
        try:
            #1. Open file in read mode
            file = open(self.file_name, "r")
            file_reader = csv.DictReader(file)
        
            #2. Split risk factors if appropriate
            for row in file_reader:
                    raw_risk_factors = row["risk_factors"].strip()
                    #If no risk factors, return empty list
                    if raw_risk_factors.lower() == "none":
                        risk_factors = []
                    else: #Split risk factors by |
                        risk_factors = raw_risk_factors.split("|")

                    #3. Create Patient object(s)
                    pt = Patient(
                        id=int(row["id"]),
                        name=row["name"],
                        ethnicity=row["ethnicity"],
                        sex=row["sex"],
                        bmi=float(row["bmi"]),
                        wc_cm=float(row["wc_cm"]),
                        risk_factors=risk_factors
                    )
                    #3.1 Append patient(s) to list
                    patients_list.append(pt) 
            
            file.close()

        except FileNotFoundError:
            print(f"File {file_name} not found.")

        return patients_list
    

    def display_patient_directory(self, patients_list):
        """
        Returns dict of {id: name}.
        Prints a formatted list of patients
        """

        pt_dict = {}
        print("\nExisting Patients:")
        for pt in patients_list:
            print(f"  ID: {pt.id} | Name: {pt.name}")
            pt_dict[pt.id] = pt.name
        print()
        return pt_dict
    

    def select_patient(self):
        """
        Displays existing patients and prompts user to select one by ID.
        Returns selected Patient object, or 'new'
        """

        patients_list = self.import_patients(self.file_name)
        if not patients_list:
            print("No patients found.")
            return None  # Goes back to Main Menu if file is empty
        
        pt_dict = self.display_patient_directory(patients_list)

        while True:
            user_input = input(f"> Enter the ID of the patient "
                               f"you would like to select "
                               f"(or type 'm' to return to Main Menu): ").strip()
            
            if user_input.lower() == "m":
                return None

            try:
                selected_id = int(user_input)
                if selected_id in pt_dict:
                    for pt in patients_list:
                        if pt.id == selected_id:
                            print(f"Patient '{pt.name}' was selected.\n")
                            print("PATIENT INFORMATION:")
                            print(pt)
                            print()
                            return pt
                else:
                    print(f"Invalid ID. Please choose a valid patient ID "
                          f"from the list or enter 'new'.\n")
            except ValueError:
                print("Please enter a valid numeric ID or 'new'.\n")

    def add_new_patient(self, name = None, ethnicity = None, sex = None, bmi = None, wc_cm = None , risk_factors_list= None):
        """
        If arguments are not provided, prompts user for patient details & appends new patient to the CSV file.
        Automatically generates a new unique patient ID.
        Returns a Patient object for immediate use
        """

        print("\nAdding a new patient...")

        #1. Determine next available ID
        next_id = 1
        try:
            file = open(self.file_name, "r")
            reader = csv.DictReader(file)
            ids = [int(row["id"]) for row in reader if row["id"].isdigit()]
            if ids:
                next_id = max(ids) + 1
            file.close()
        except FileNotFoundError:
            print("CSV file not found. A new file will be created.")

        print("Collecting information about the new patient...\n")

        #2. Prompt user for data input if not passed in arguments & validate
        if name is None:
            valid_input = False
            while valid_input is False:
                name = input("> Patient's full name: ").title()
                valid_input = self.validate_new_pt_data("name", name)


        if ethnicity is None:
            valid_input = False
            while valid_input is False:
                ethnicity = input("> Patient's ethnicity: ").title()
                valid_input = self.validate_new_pt_data("ethnicity", ethnicity)
                    
        
        if sex is None:
            valid_input = False
            while valid_input is False:    
                sex = input("> Patient's sex (M/F): ").upper()
                valid_input = self.validate_new_pt_data("sex", sex)
                    

        if bmi is None:
            valid_input = False
            while not valid_input:
                try:
                    bmi = float(input("> Patient's BMI (10.0-80.0): "))
                    valid_input = self.validate_new_pt_data("bmi", bmi)
                        
                except ValueError:
                    print("Input error: Please enter a number.")

        if wc_cm is None:
            valid_input = False
            while not valid_input:
                try:
                    wc_cm = float(input(f"> Patient's waist circumference "
                                        f"(50.0-200.0 cm): "))
                    valid_input = self.validate_new_pt_data("wc_cm", wc_cm)

                except ValueError:
                    print("Input error: Please enter a number.")

        #3. Handle risk factors

        #3.a Capture risks via user input 
        if risk_factors_list == None:
            risk_factors_list = self.capture_risks()

        #3.b Validate provided risk factors is passed argument
        elif self.validate_new_pt_data("risk_factors_list", risk_factors_list) is False:
            raise ValueError(
                f"One of the risk factors is not accepted. "
                f"Only 'none' or {self.predefined_risks} are allowed."
            )

        #5. Return new Patient object
        new_patient = Patient(next_id, name, ethnicity, sex, bmi, wc_cm, risk_factors_list)
        self.append_patient_to_CSV(new_patient)
        print("\nNew patient was added.\n")
        print("PATIENT INFORMATION:")
        print(new_patient)
        print()
        return new_patient

    def append_patient_to_CSV(self, patient):
        """Appends a single new patient to the CSV file."""
        
        # Check if file is new or empty
        write_header = False
        if not os.path.exists(self.file_name) or os.stat(self.file_name).st_size == 0:
            write_header = True

        # Prepare risk factor field
        risk_factor_field = "none" if len(patient.risk_factors) == 0 or \
                             None in patient.risk_factors \
                            else "|".join(patient.risk_factors)

        # Write to file
        with open(self.file_name, "a", newline="") as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(["id", "name", "ethnicity", "sex", "bmi", "wc_cm", "risk_factors"])

            writer.writerow([
                patient.id,
                patient.name,
                patient.ethnicity,
                patient.sex,
                patient.bmi,
                patient.wc_cm,
                risk_factor_field
            ])

    def capture_risks(self):
        """Captures patient risks via user input to y/n questions"""

        risk_factors_list = []
        print("\nCollecting risk factors...")
        print("Does the patient have:")
        
        for risk_factor in self.predefined_risks:
            while True:
                user_answer = input(
                    f"   - {risk_factor}?\n"
                    f"      (y) Yes\n"
                    f"      (n) No\n"
                    f"      > Enter your choice: "
                ).strip().lower()

                if user_answer == "y":
                    risk_factors_list.append(risk_factor)
                    break
                elif user_answer == "n":
                    break
                else:
                    print(f" Invalid input. "
                          f"Please only enter 'y' for Yes or 'n' for No.")

        return risk_factors_list

    def validate_new_pt_data(self, field, user_input):
        """Validates user_input matches CSV format and/or is within parameters"""

        valid_input = False
        if field == "name" or field == "ethnicity":
            valid_input = True  # Assume valid until we find a bad character
            for char in user_input:
                if (char in string.ascii_letters or char == " ") is False:
                    valid_input = False
                    print("Input error: Do not use commas or special characters.")
                    break
        elif field == "sex":
            if user_input == "M" or user_input == "F":
                valid_input = True
            else:
                print("Input error: Only 'M' or 'F' characters allowed.")
        elif field == "bmi":
            if 10.0 <= user_input <= 80.0:
                valid_input = True
            else:
                print(f"Input error: "
                      f"Only numbers between 10.0 and 80.0 are valid.")
        elif field == "wc_cm":
            if 50.0 <= user_input <= 200.0:
                valid_input = True
            else:
                print(f"Input error: "
                      f"Only numbers between 50.0 and 200.0 are valid.")
        elif field == "risk_factors_list":
            if user_input == "none":
                valid_input = True
            elif isinstance(user_input, list):
                predefined_risks = [
                "family/patient history of cardiovascular event",
                "hypertension",
                "dyslipidemia",
                "low activity"
                ]
                valid_input = True
                for rf in user_input:
                    if rf not in predefined_risks:
                        valid_input = False
                        break

        return valid_input

    def update_pt_info(self, selected_pt, field_to_update):
        """Allows user to update a selected patient's information in the CSV"""

        if field_to_update == "name":
            valid_input = False
            while not valid_input:
                new_value = input("> Enter new name: ").title()
                valid_input = self.validate_new_pt_data("name", new_value)
            selected_pt.update_info(field_to_update, new_value)

        elif field_to_update == "bmi":
            valid_input = False
            while not valid_input:
                try:
                    new_value = float(input("> Enter new BMI (10.0-80.0): "))
                    valid_input = self.validate_new_pt_data("bmi", new_value)
                except ValueError:
                    print("Please enter a number.")
            selected_pt.update_info(field_to_update, new_value)

        elif field_to_update == "wc_cm":
            valid_input = False
            while not valid_input:
                try:
                    new_value = float(input(f"> Enter new waist circumference"
                                            f" (50.0-200.0 cm): "))
                    valid_input = self.validate_new_pt_data("wc_cm", new_value)
                except ValueError:
                    print("Please enter a number.")
            selected_pt.update_info(field_to_update, new_value)

        elif field_to_update == "risk_factors_list":
            new_value = self.capture_risks()
            selected_pt.update_info(field_to_update, new_value)

        # Write updated patient to file
        try:
            self.update_patient_in_CSV(selected_pt)
        except Exception as e:
            print(f"Error while saving update: {e}")
            return

        print("\nPatient information successfully updated.\n")
        print("UPDATED PATIENT RECORD:")
        print(selected_pt)


    def update_patient_in_CSV(self, updated_patient):
        """Overwrites the CSV with updated info for a single patient"""
        
        patients_list = self.import_patients(self.file_name)

        # Replace the existing patient in the list
        for i, pt in enumerate(patients_list):
            if pt.id == updated_patient.id:
                patients_list[i] = updated_patient
                break
        else:
            print("Warning: Updated patient not found in file. Appending instead.")
            patients_list.append(updated_patient)

        # Rewrite the entire file
        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "ethnicity", "sex", "bmi", "wc_cm", "risk_factors"])

            for pt in patients_list:
                risk_factor_field = "none" if len(pt.risk_factors) == 0 or None in pt.risk_factors \
                                    else "|".join(pt.risk_factors)

                writer.writerow([
                    pt.id,
                    pt.name,
                    pt.ethnicity,
                    pt.sex,
                    pt.bmi,
                    pt.wc_cm,
                    risk_factor_field
                ])