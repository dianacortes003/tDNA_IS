'''
The program contains attributes and methods of the class Patient.

Input: Patient data arguments passed throuhg main_patient.py doc
Output: Patient's attributes, disease risk, and recommendations 
'''

class Patient:
    def __init__(self, id, name, ethnicity, sex, bmi, wc_cm, risk_factors=None):
        self.__id = id
        self.name = name
        self.__ethnicity = ethnicity
        self.__sex = sex
        self.bmi = bmi
        self.wc_cm = wc_cm
        self.risk_factors = set(risk_factors) if risk_factors else set()
        self.bmi_category = ""
        self.recs = ()

    #Getter for id
    @property
    def id(self):
        """Patient ID (read-only)"""
        return self.__id

    # Getter and setter for ethnicity
    @property
    def ethnicity(self):
        return self.__ethnicity

    @ethnicity.setter
    def ethnicity(self, value):
        self.__ethnicity = value

    # Getter and setter for sex
    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        self.__sex = value


    def _cm_to_inches(self):
        """Converts centimeters to inches."""
        return self.wc_cm / 2.54
    

    def calculate_disease_risk(self):
        """
        Determines BMI category and risk level based on ethnicity.
        Updates risk_factors if needed.
        """

        if "asian" in self.ethnicity.lower():
            if self.bmi < 18.5:
                bmi_category = "Underweight"
                risk = "average risk"
            elif 18.5 <= self.bmi <= 22.9:
                bmi_category = "Normal"
                risk = "average risk"
            elif 23.0 <= self.bmi <= 24.9:
                bmi_category = "Overweight - Class I"
                if self.sex == 'M':
                    if self.wc_cm <= 90:
                        risk = "increased risk"
                    else:
                        risk = "high risk"
                elif self.sex == 'F':
                    if self.wc_cm <= 80:
                        risk = "increased risk"
                    else:
                        risk = "high risk"
            elif 25.0 <= self.bmi <= 29.9:
                bmi_category = "Obese - Class II"
                if self.sex == 'M':
                    if self.wc_cm <= 90:
                        risk = "high risk"
                    else:
                        risk = "very high risk"
                elif self.sex == 'F':
                    risk = "very high risk"
            elif self.bmi >= 30.0:
                bmi_category = "Extremely obese - Class III"
                risk = "severe risk"
                
        else:  # Non-asian BMI cutoffs
            wc_in = self._cm_to_inches()
            if self.bmi < 18.5:
                bmi_category = "Underweight"
                risk = "N/A"
            elif 18.5 <= self.bmi <= 24.9:
                bmi_category = "Normal"
                risk = "N/A"
            elif 25.0 <= self.bmi <= 29.9:
                bmi_category = "Overweight"
                if self.sex == 'M':
                    if wc_in <= 40:
                        risk = "increased risk"
                    else:
                        risk = "high risk"
                elif self.sex == 'F':
                    if wc_in <= 35:
                        risk = "increased risk"
                    else:
                        risk = "high risk"
            elif 30.0 <= self.bmi <= 34.9:
                bmi_category = "Obese - Class I"
                if self.sex == 'M':
                    if wc_in <= 40:
                        risk = "high risk"
                    else:
                        risk = "very high risk"
                elif self.sex == 'F':
                    if wc_in <= 35:
                        risk = "high risk"
                    else:
                        risk = "very high risk"
            elif 35.0 <= self.bmi <= 39.9:
                bmi_category = "Obese - Class II"
                risk = "very high risk"
            elif self.bmi >= 40:
                bmi_category = "Extremely obese - Class III"
                risk = "extremely high risk"

        self.bmi_category = bmi_category

        if "risk" in risk and "average" not in risk:
            self.risk_factors.add(risk + " diabetes")

        return bmi_category, risk


    def __len__(self):
        """Returns the number of risk factors."""

        return len(self.risk_factors)
    

    def get_rec(self):
        """
        Generates recommendations tuple based on risk factors and BMI category
        """

        self.calculate_disease_risk()
        recs = []

        if len(self) >= 1:
            if "low activity" in self.risk_factors or \
                "Underweight" not in self.bmi_category or \
                "Normal" not in self.bmi_category:
                    recs.append("Increase physical activity")
            if "dyslipidemia" in self.risk_factors or \
               "family/patient history of cardiovascular event" in \
                self.risk_factors:
                    recs.append("Follow low-GI foods")
            if "hypertension" in self.risk_factors:
                recs.append("Antihypertensive diet")
        else:
            recs.extend(["Maintain current habits", "Regular check-ups"])


        if self.bmi_category == "Underweight":
            recs.append("Diabetes-specific nutrition supplements")

        self.recs = tuple(recs)
        return self.recs
    

    def __str__(self):
        """Returns a formatted string with patient info and recommendations"""
        
        self.get_rec()
        risk_factors_display = (
            self.risk_factors if self.risk_factors else {"none"}
        )

        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ethnicity: {self.ethnicity}\n"
            f"Sex: {self.sex}\n"
            f"Risk Factors: {risk_factors_display}\n"
            f"BMI: {self.bmi}\n"
            f"BMI Category: {self.bmi_category}\n"
            f"Waist Circumference: {self.wc_cm}\n"
            f"Recommendations: {self.recs}"
        )
    

    def update_info(self, field_to_update, new_value):
        """
        Updates patient information for a specified field.
        Recalculates risk and recommendations.
        """

        if field_to_update == "name":
            self.name = new_value
        elif field_to_update == "bmi":
            self.bmi = new_value
        elif field_to_update == "wc_cm":
            self.wc_cm = new_value
        elif field_to_update == "risk_factors_list":
            self.risk_factors = set(new_value)

        #Recalculate derived fields
        self.calculate_disease_risk()
        self.get_rec()

        return self
            

