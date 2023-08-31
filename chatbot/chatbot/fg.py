import random
# Define a class for the chatbot.
class DoctorConsultationBot:
    def _init_(self, name):
        self.name = name
        self.doctors = []
    # Add a doctor to the chatbot.
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    # Get a random doctor from the chatbot.
    def get_random_doctor(self):
        return random.choice(self.doctors)
    # Start a consultation with a doctor.
    def start_consultation(self):
        doctor = self.get_random_doctor()
        print("Welcome to the doctor's office.")
        print("What can I help you with today?")
        # Get the user's input.
        user_input = input()
        # Get the doctor's response.
        doctor_response = doctor.get_response(user_input)
        # Print the doctor's response.
        print(doctor_response)
        # Continue the consultation until the user is done.
        while True:
            user_input = input()
            doctor_response = doctor.get_response(user_input)
            print(doctor_response)
            if user_input == "quit":
                break
# Create a chatbot object.
chatbot = DoctorConsultationBot("Doctor Consultation Bot")
# Add some doctors to the chatbot.
chatbot.add_doctor(Doctor("Dr. Smith"))
chatbot.add_doctor(Doctor("Dr. Jones"))
# Start a consultation with the chatbot.
chatbot.start_consultation()