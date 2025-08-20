from patient import Patient
import main_tDNA
import foods_gi
import patient_manager
import csv, os
import random

def randomize_test_patient():

    #Asian Female (moderate risk)
    asian_F_attr_lst = ["Lina Chen","Asian","F",24.0,75,["low activity"]]

    #Asian Male (high risk)
    asian_M_attr_lst = ["Kenji Takahashi", "Asian", "M", 32.5, 95, [
                            "hypertension", "low activity", 
                           "family/patient history of cardiovascular event"
        ]]
    #Non-Asian Female (low risk)
    non_asian_F_attr_lst = ["Lupita Gonzalez","Hispanic","F",22.0,80, []]
    
    #Non-Asian Male (very high risk)
    non_asian_M_attr_lst = ["Jack Smith","White","M",36.0, 122,[
            "hypertension",
            "dyslipidemia",
            "low activity",
            "family/patient history of cardiovascular event"
        ] ]

    test_patients_list = [asian_F_attr_lst, asian_M_attr_lst, 
                          non_asian_F_attr_lst, non_asian_M_attr_lst]

    random_pt = random.choice(test_patients_list)

    return random_pt


###############################################################################
###############################################################################

def test_add_new_patient(pt_attributes_list):
    print()
    print("=" * 80)
    print("TESTING: add_new_patient() from patient_manager.py... ")
    print("-" * 5)
    
    name = pt_attributes_list[0]
    ethnicity = pt_attributes_list[1]
    sex = pt_attributes_list[2]
    bmi = pt_attributes_list[3]
    wc_cm = pt_attributes_list[4]
    risk_factors_list = pt_attributes_list[5]

    #1. Call method to test
    test_patient = test_pt_manager.add_new_patient(name, ethnicity, sex, bmi, wc_cm, risk_factors_list)

    #2. Assert patient object was returned correctly
    assert isinstance(test_patient, Patient), (
        f"ERROR: Did not return a Patient object"
    )

    #3. Check if patient was added to the CSV
    found_in_csv = False
    with open(test_pt_manager.file_name, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["name"] == test_patient.name:
                found_in_csv = True
                break
    assert found_in_csv, "ERROR: Patient was not added to CSV file"

    #4. Print sucess message
    print("-" * 5)
    print(
          f"--- add_new_patient() PASSED TEST: "
          f"patient information was correctly added to CSV file ---\n"
    )
    print("=" * 80)

    return test_patient

###
def test_update_patient_in_CSV(test_patient):
    print()
    print("=" * 80)
    print("TESTING: update_patient_in_CSV() from patient_manager.py... ")
    
    print("*** NOTE: Original bmi value will be reinstated after completing this test.\n")
    print("-" * 5)

    print(f"\n{test_patient.name}'s original bmi is: {test_patient.bmi}\n")
    print("Updating bmi to 40.0 ...\n")

    #Hold original value to reinstate after unit test
    original_bmi = float(test_patient.bmi)

    #1. Update value
    test_patient.bmi = 40.0
    print(f"{test_patient.name}'s updated bmi is: {test_patient.bmi}")

    #2 Call method to test
    test_pt_manager.update_patient_in_CSV(test_patient)

    #3. Check if patient was added to the CSV
    updated_in_csv = False
    with open(test_pt_manager.file_name, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["bmi"] == "40.0":
                updated_in_csv = True
                break
    assert updated_in_csv, (
        f"ERROR: Updated information was not found in CSV file."
    )

    #Reinstate original bmi
    test_patient.bmi = original_bmi
    print(f"\n{test_patient.name}'s reinstated bmi is: {test_patient.bmi}")
    assert test_patient.bmi == original_bmi, "DIDN'T REINSTATE"

    #4. Print sucess message
    print()
    print("-" * 5)
    print(
          f"--- update_patient_in_CSV() PASSED TEST: "
          f"patient information was correctly updated to CSV file ---\n"
    )
    print("=" * 80)

    

###
def test_calculate_risk(test_patient):

    print()
    print("=" * 80)
    print("TESTING: calculate_disease_risk() from patient.py... ")
    print("-" * 5)

    #1. Call method to test
    category, risk = test_patient.calculate_disease_risk()
    print(f"\nBMI category: {category}\nRisk level: {risk} diabetes")

    #2. Assert return types
    assert isinstance(category, str), "ERROR: category is not a string"
    assert isinstance(risk, str), "ERROR: risk is not a string"

    #3. Match & assert expected outputs by patient
    if test_patient.name == "Lina Chen":
        assert category == "Overweight - Class I", (
            f"ERROR: Expected 'Overweight - Class I', got '{category}'"
        )
        assert risk == "increased risk", (
            f"ERROR: Expected 'increased risk', got '{risk}'"
        )

    elif test_patient.name == "Kenji Takahashi":
        assert category == "Extremely obese - Class III", (
            f"ERROR: Expected 'Extremely obese - Class III', got '{category}'"
        )
        assert risk == "severe risk", (
            f"ERROR: Expected 'severe risk', got '{risk}'"
        )

    elif test_patient.name == "Lupita Gonzalez":
        assert category == "Normal", (
            f"ERROR: Expected 'Normal', got '{category}'"
        )
        assert risk == "N/A", (
            f"ERROR: Expected 'N/A', got '{risk}'"
        )

    elif test_patient.name == "Jack Smith":
        assert category == "Obese - Class II", (
            f"ERROR: Expected 'Obese - Class II', got '{category}'"
        )
        assert risk == "very high risk", (
            f"ERROR: Expected 'very high risk', got '{risk}'"
        )

    else:
        raise ValueError(
            f"ERROR: Unknown test patient '{test_patient.name}'"
        )
    
    #4. Print sucess message
    print()
    print("-" * 5)
    print(
          f"--- calculate_disease_risk() PASSED TEST: "
          f"correct logic and output ---\n"
    )
    print("=" * 80)

###
def test_get_rec(test_patient):
    print()
    print("=" * 80)
    print("TESTING: get_rec() from patient.py...")
    print("-" * 5)

    #Call method to test
    test_patient.get_rec()
    print(f"\nPatient's recommendations are: {test_patient.recs}")

    if len(test_patient.risk_factors) == 0:
        assert "Maintain current habits" in test_patient.recs, (
            f"ERROR: Expected 'Maintain current habits' "
            f"for no-risk patients not found."
        )

    else:
        if "hypertension" in test_patient.risk_factors:
            assert "Antihypertensive diet" in test_patient.recs, (
                f"ERROR: Expected 'Antihypertensive diet' not found in recs."
            )
        if "Underweight" in test_patient.bmi_category or \
            "Normal" in test_patient.bmi_category:
            assert (
                "Diabetes-specific nutrition supplements" in test_patient.recs
        ), (
                f"ERROR: Expected 'Diabetes-specific nutrition supplements' "
                f"not found in recs."
            )
            assert "Increase physical activity" not in test_patient.recs, (
                f"ERROR: This patient should not have"
                f" 'Increase physical activity' in recs."
            )
        if "dyslipidemia" in test_patient.risk_factors or \
               "family/patient history of cardiovascular event" in \
                test_patient.risk_factors:
            assert "Follow low-GI foods" in test_patient.recs, (
                f"ERROR: Expected 'Follow low-GI foods' not found in recs."
            )

    #4. Print sucess message
    print()
    print("-" * 5)
    print(
          f"--- get_rec() PASSED TEST: "
          f"correct logic and output ---\n"
    )
    print("=" * 80)

###
def test_get_formatted_foods(test_patient):

    print()
    print("=" * 80)
    print("TESTING: get_formatted_foods() from foods_gi.py...")
    print("-" * 5)

    #1. Ensure recommendations are generated
    test_patient.get_rec() #Function to test depends on its output/return

    #2. Call function to test
    formatted_text = foods_gi.get_formatted_foods(test_patient.recs)

    confirmation_output = "Formatted foods contain: "
    if "Low GI" in formatted_text:
        confirmation_output += "Low GI"
    if "High GI" in formatted_text:
        confirmation_output += "', High GI'"
    if "Medium GI" in formatted_text:
        confirmation_output += "', Medium GI"
    print(f"\n{confirmation_output}")

    #3. Assert text contains Low GI foods (all patients get this list)
    assert "Low GI" in formatted_text, (
        "ERROR: Low GI section missing in formatted output."
    )

    #4. Assert text contains correct food lists based on patient's recs
    if "Follow low-GI foods" in test_patient.recs:
        assert "High GI" not in formatted_text,(
            "ERROR: High GI section should not appear."
        )
        assert "Medium GI" not in formatted_text,(
            "ERROR: Medium GI section should not appear."
        )
    else:
        assert "High GI" in formatted_text,(
            "ERROR: High GI section missing from formatted string."
        )
        assert "Medium GI" in formatted_text,(
            "ERROR: Medium GI section missing from formatted string."
        )

    #5. Print sucess message
    print()
    print("-" * 5)
    print(
        f"--- get_formatted_foods() PASSED TEST: "
        f"output matched expected content ---\n"
    )
    print("=" * 80)

###
def test_generate_handout(test_patient):

    print("=" * 80)
    print("TESTING: generate_rec_handout() from main_tDNA.py... ")
    print(f"*** NOTE: Generated handout will be deleted "
          f"after this test is sucessfully completed.")
    print("-" * 5)

    #1. Construct expected base name
    base_name = f"{test_patient.name.replace(' ', '_')}_recommendations"
    expected_file_name = f"{base_name}.txt"
    version = 1

    #2. Use main's program logic to determine expected file name
    while os.path.exists(expected_file_name):
        expected_file_name = f"{base_name}_v{version}.txt"
        version += 1

    #3. Run function
    main_tDNA.generate_rec_handout(test_patient)

    #4. Assert file was created
    assert os.path.exists(expected_file_name), (
        f"ERROR: Recommendation file '{expected_file_name}' was not created"
    )

    #5. Assert file was named correctly
    generated_files = [f for f in os.listdir('.') if f.startswith(base_name)]
    assert expected_file_name in generated_files, (
        f"ERROR: Expected file name '{expected_file_name}' " 
        f"not found in directory."
    )

    #6. Assert file contains expected content
    with open(expected_file_name, "r") as f:
        contents = f.read()
        assert len(contents) > 0, "ERROR: File was created but is empty."
        assert "PATIENT INFORMATION" in contents, (
            "ERROR: Expected section header not found in file."
        )
        assert test_patient.name in contents, (
            "ERROR: Patient name not found in the file."
        )
        assert "High GI" or "Medium GI" or "Low GI" in contents, (
            "ERROR: Expected food recommendations section not found in file."
        )
        if "Antihypertensive diet" in test_patient.recs:
            assert "ANTIHYPERTENSIVE DIET" in contents, (
                f"ERROR: Expected antihypertensive diet section "
                f"not found in file."
        )

    #7. Delete test file
    print(f"\n *** Deleting '{expected_file_name}' file...\n")
    os.remove(expected_file_name) #CONVERT TO COMMENT TO KEEP FILE

    #8. Print sucess message
    print()
    print("-" * 5)
    print(
        f"--- generate_rec_handout() PASSED TEST: "
        f"info was written into correctly named file ---\n"
    )
    print("=" * 80)

###############################################################################
###############################################################################

if __name__ == "__main__":
    FILE_NAME = "test_tDNA.csv" 
    PREDEFINED_RISKS = [
            "family/patient history of cardiovascular event",
            "hypertension",
            "dyslipidemia",
            "low activity"
        ]
    
    print("~" * 80)
    print()
    print("-" * 29 ,"UNIT TEST mock-tDNA", "-" * 29)

    print(f"\n>>> TESTING PROGRAM USING FILE: '{FILE_NAME}' ...\n")
    print(f"*** NOTE: '{FILE_NAME}' will be deleted "
          f"after all tests are sucessfully completed.")

    test_pt_manager = patient_manager.PatientManager(
        FILE_NAME, PREDEFINED_RISKS
    )

    #Get random patient out of 4 predefined options
    pt_attributes_list = randomize_test_patient()

    #Create patient object and test add_new_patient()
    test_patient = test_add_new_patient(pt_attributes_list)

    print(f"\n>>> TESTING REMAINING FUNCTIONS USING TEST PATIENT:"
          f" '{test_patient.name}'...\n")

    #CALL TEST FUNCTIONS

    test_update_patient_in_CSV(test_patient)
    test_calculate_risk(test_patient)
    test_get_rec(test_patient)
    test_get_formatted_foods(test_patient)
    test_generate_handout(test_patient)

    if os.path.exists(FILE_NAME): #CONVERT TO COMMENT TO KEEP FILE
        print(f"\n *** Deleting '{FILE_NAME}' file...\n") 
        os.remove(FILE_NAME) #CONVERT TO COMMENT TO KEEP FILE

    print(">>> TESTING PROGRAM FINISHED: All tests passed successfully!\n")
    print("-" * 25 ,"End of UNIT TEST mock-tDNA", "-" * 25)










