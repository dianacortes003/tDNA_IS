# tDNA_IS
## Implementing the Transcultural Diabetes-Specific Nutrition Algorithm (tDNA) as a Health IT System

This project transforms the proposed **Transcultural Diabetes-Specific Nutrition Algorithm (tDNA)** by **_Mechanick et al. (2012)_**[^1]  into a clinical information system. This implementation aims to digitize and automate the recommended approach for enhancing diabetes and prediabetes care through culturally adaptive nutrition guidance. 

The repository contents include:
- A flowchart modeling the clinical logic of the _tDNA_
- A pseudocode version of the _tDNA_ logic
- Python implementations of the tDNA logic
- A system integration diagram showing how the tDNA engine interfaces with hospital systems such as Electronic Health Records (EHR), Laboratory Information System (LIS), and patient portals, as well as with an international nutrition and clinical practice guidelines (CPGs) database. 

This project bridges evidence-based clinical guidelines with health IT systems, supporting scalable integration into hospital infrastructure and global data networks. Ideal for use by clinical informatics professionals, developers, and researchers in digital health.
_________________



<details>
<summary>PURPOSE & GOALS</summary>
  
### Purpose & Goals
  
#### Purpose
The purpose of the tDNA is to address the gap in the efficacy of nutritional guidelines when applied to a variety of ethnocultural population classifications by considering genetic, cultural, and regional factors in diabetes care. Many diabetes nutritional and lifestyle CPGs originate from research made in developed countries with an often undiversified pool of subjects. We know that some populations have a higher risk of certain conditions than others. However, these variations are not always possible to include in generalized CPG research study outcomes.  
When transcultural factors are not weighted in the clinical decision processes, the "promised" effectiveness of the CPGs can be compromised.

>_Finally, CPGs may not be able to be generalized for all patients or populations. Patient age, gender, and genomics, as well as culture, customs, and environment, must be factored into any decision to apply a particular recommendation to a particular patient in particular settings (Mechanick et al., 2012)_

#### Goals
As noted by _Mechanick et al. (2012)_
>_The tDNA is intended to:_
>1) _increase awareness of the benefits of nutritional interventions for patients with T2D and prediabetes;_
>2) _encourage healthy dietary patterns that accommodate regional differences in genetic factors, lifestyles, foods, and cultures;_ 
>3) _enhance the implementation of existing CPGs for T2D and prediabetes management; and_ 
>4) _simplify nutritional therapy for ease of application and portability._

</details>

__________________



<details>
<summary>SCOPE</summary>

### Scope
Based on _Mechanick et al. (2012)_, this algorithm was designed for type 2 diabetes and prediabetes patients. _Mechanick et al_ recommend its use by Primary Care Physicians (PCPs) or equivalent and/or Registered Dietitians (RDNs).

The algorithm, as a decision-tree clinical tool, has been researched in outpatient environments. However, it could also be implemented on an inpatient basis. This inpatient format would probably have to include additional steps to integrate with the dining services system at the facility. This repo does not include that scenario. 

The whole purpose of this nutritional algorithm  is to be multiculturally adapted. _Mechanick_ has published other articles on applying the _tDNA_ in various regions, in addition to some algorithmic adaptations for certain populations.

Implementation locations:
- America
  - US, Brazil, Canada, Mexico, Panama
- Europe
  - The Netherlands, Spain
- Asia
  - China, Taiwan


Adapted version for:
- Southeast Asia 
  - Philippines, Indonesia, Malaysia, Singapore, and Thailand
- India

This repo does not include the adapted versions.

</details>

____________________



<details>
<summary>STRENGTHS & LIMITATIONS</summary>

### Strengths & Limitations

#### Strengths
##### Simple yet multifactorial personalized nutrition
The _tDNA_ contains a risk stratification process that filters CPGs based on multifactorial input and outputs of simple and individually relevant nutrition and lifestyle recommendations.  

##### Culturally-adapted improves patient adherence
Patient adherence is and will always be a significant barrier in patient care. Many other articles demonstrate the positive impact of saliency in treatment plans for more consistent patient adherence. By including culturally-relevant foods in the recommended diet, the tDNA can help ..... 

##### Compiled evidence-based guidelines 
In order to create the tDNA, _Mechanick et al._ compiled and adapted evidence-based nutritional recommendations from the American Association of Clinical Endocrinologists (AACE), the American Diabetes Association (ADA), and other international organizations.

##### Multinational health advice and usage
A task force integrated by internationally respected health care experts in diabetes and nutrition was created in order to provide data, culturally meaningful information, and expert opinion to guide algorithm development.

##### Ongoing collaborations and modifications 
After this initial publication of the tDNA, researchers and task force members have continued to collect transcultural data to create adapted versions that factor in differences within specific populations.

#### Limitations

##### Inequitable local adaptation capabilities
Despite the algorithm's best efforts to include a variety of transcultural factors in the stratification process, the overall gap in available information on underrepresented populations remains a significant challenge. 

Additionally, the article mentions the inequity of general nutrition education, both from an availability and cultural resistance perspective. 

Lastly, one of the algorithms' output recommendations includes diabetes-specific liquid meal formulas. These formulas are not always accessible to many patients. 

##### No HIS integration evidence 
As previously mentioned, the _tDNA_ is a decision-tree tool for clinicians, and it has not been formally converted into a health information system (HIS). Therefore, there is no current evidence of its efficacy in that format, nor the true needs and capabilities for integration into a hospital's information system.  

</details>

_______________________


[^1]: Mechanick, J. I., Marchetti, A. E., Apovian, C., Benchimol, A. K., Bisschop, P. H., Bolio-Galvis, A., ... & Hamdy, O. (2012). Diabetes-specific nutrition algorithm: a transcultural program to optimize diabetes and prediabetes care. Current diabetes reports, 12, 180-194.
