class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def __repr__(self):
        return self.name

def search_patients(patients, disease):
    """Search for patients by disease."""
    result = [patient for patient in patients if patient.disease.lower() == disease.lower()]
    return result

def main():
    patients = []
    try:
        n = int(input("Enter number of patients: "))
        if n <= 0:
            print("Please enter a valid number of patients.")
            return

        for _ in range(n):
            name = input("Enter name: ").strip()
            while not name:
                name = input("Name cannot be empty. Please enter the patient's name: ").strip()
            
            age = input("Enter age: ").strip()
            while not age.isdigit():
                age = input("Please enter a valid age: ").strip()
            age = int(age)

            disease = input("Enter disease: ").strip()
            while not disease:
                disease = input("Disease cannot be empty. Please enter the disease: ").strip()

            patient = Patient(name, age, disease)
            patients.append(patient)

        disease_to_search = input("Enter disease to search: ").strip()

        result = search_patients(patients, disease_to_search)
        if result:
            print(f"Patients with {disease_to_search}: {[patient.name for patient in result]}")
        else:
            print(f"No patients found with {disease_to_search}.")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
