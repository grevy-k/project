class Patient:
    def __init__(self, patient_id, name, gender, condition, age, admission_date):
        self.id = patient_id  # Fixed variable name
        self.name = name
        self.gender = gender
        self.condition = condition  # Fixed spelling error
        self.age = age
        self.admission_date = admission_date

    def get_details(self):
        return (f"id: {self.id}, name: {self.name}, gender: {self.gender}, "
                f"condition: {self.condition}, age: {self.age}, "
                f"admission date: {self.admission_date}")

# Creating multiple patient objects
patient1 = Patient(1, "King James", "male", "stable", 30, "10-31-2024")
patient2 = Patient(2, "Sara Mandi", "female", "on medicine", 23, "09-25-2024")
patient3 = Patient(3, "Kim Kardashian", "female", "recovering", 44, "08-18-2024")

# Inserting patients into a list
patient_list = [patient1, patient2, patient3]

# Counting patients
def count_patients(patient_list):
    return len(patient_list)

# Providing patient names
def list_patient_names(patient_list):
    return [patient.name for patient in patient_list]

# Execution
if __name__ == "__main__":  # Fixed assignment operator
    print("Total patients:", count_patients(patient_list))
    print("Patient names:", list_patient_names(patient_list))
    
    # Print patient details by ID
    for patient in patient_list:
        print(patient.get_details())

