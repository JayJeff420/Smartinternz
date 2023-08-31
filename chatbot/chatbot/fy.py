import random

# Sample list of doctors
doctors = {
    "1": "Dr. Smith",
    "2": "Dr. Johnson",
    "3": "Dr. Williams",
}

# Sample list of specialties
specialties = {
    "1": "General Medicine",
    "2": "Pediatrics",
    "3": "Dermatology",
}

# Sample list of patient symptoms
symptoms = {
    "1": "Fever",
    "2": "Cough",
    "3": "Headache",
}

def get_input(choices, prompt):
    while True:
        print(prompt)
        for key, value in choices.items():
            print(f"{key}: {value}")
        user_input = input("Enter the number corresponding to your choice: ")
        if user_input in choices:
            return user_input
        print("Invalid input. Please try again.")

def doctor_consultation():
    print("Welcome to the doctor consultation service!")
    
    # Select a doctor
    doctor_choice = get_input(doctors, "Please choose a doctor:")
    selected_doctor = doctors[doctor_choice]
    print(f"Great! You've selected {selected_doctor}.")

    # Select a specialty
    specialty_choice = get_input(specialties, "Please choose a specialty:")
    selected_specialty = specialties[specialty_choice]
    print(f"Perfect! You've selected {selected_specialty}.")

    # Describe the symptoms
    print("Please describe your symptoms:")
    patient_symptoms = []
    while True:
        symptom_choice = get_input(symptoms, "Enter the number corresponding to your symptom (or 'done' to finish):")
        if symptom_choice == 'done':
            break
        patient_symptoms.append(symptoms[symptom_choice])
    
    # Generate a response
    response = random.choice([
        f"{selected_doctor} is reviewing your symptoms related to {', '.join(patient_symptoms)}. Please wait for a moment.",
        f"{selected_doctor} is examining your case, considering {', '.join(patient_symptoms)}.",
        f"{selected_doctor} is discussing your symptoms of {', '.join(patient_symptoms)}.",
    ])
    print(response)
    print("Thank you for using our consultation service. Take care!")

if __name__ == "__main__":
    doctor_consultation()
