"""

Question: Patients with a condition

Summary: Write a function that finds patients with Type I Diabetes by identifying conditions that start with the 'DIAB1' prefix.
The result table includes 'patient_id', 'patient_name', and 'conditions', and can be returned in any order.

Method: Filter the 'patients' DataFrame to include only rows where the 'conditions' column contains the 'DIAB1' prefix.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Filter patients with conditions containing 'DIAB1'
    return patients[patients["conditions"].str.contains(r"\bDIAB1")]


# Example usage
patients_data = {
    'patient_id': [1, 2, 3, 4, 5],
    'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
    'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']
}
patients = pd.DataFrame(patients_data)

result = find_patients(patients)
print(result)
