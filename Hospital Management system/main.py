from database import create_tables, get_connection
from patient import Patient
from doctor import Doctor
from appointment import Appointment

def register_user():
    print("\n=== USER REGISTRATION ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", 
                         (username, password))
            conn.commit()
            print("Registration successful!")
        except:
            print("Username already exists!")
        cursor.close()
        conn.close()

def login():
    print("\n=== LOGIN ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", 
                      (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user:
            print(f"Welcome, {username}!")
            return True
        else:
            print("Invalid credentials!")
            return False
    return False

def patient_menu():
    while True:
        print("\n=== PATIENT MANAGEMENT ===")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Back to Main Menu")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender (M/F): ")
            address = input("Enter address: ")
            contact = input("Enter contact: ")
            disease = input("Enter disease: ")
            doctor = input("Enter assigned doctor: ")
            
            patient = Patient(name, age, gender, address, contact, disease, doctor)
            patient.add_patient()
        
        elif choice == '2':
            Patient.view_all_patients()
        
        elif choice == '3':
            name = input("Enter patient name to search: ")
            Patient.search_patient(name)
        
        elif choice == '4':
            patient_id = int(input("Enter patient ID to delete: "))
            Patient.delete_patient(patient_id)
        
        elif choice == '5':
            break

def doctor_menu():
    while True:
        print("\n=== DOCTOR MANAGEMENT ===")
        print("1. Add New Doctor")
        print("2. View All Doctors")
        print("3. Delete Doctor")
        print("4. Back to Main Menu")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            specialization = input("Enter specialization: ")
            age = int(input("Enter age: "))
            contact = input("Enter contact: ")
            fees = float(input("Enter consultation fees: "))
            salary = float(input("Enter monthly salary: "))
            
            doctor = Doctor(name, specialization, age, contact, fees, salary)
            doctor.add_doctor()
        
        elif choice == '2':
            Doctor.view_all_doctors()
        
        elif choice == '3':
            doctor_id = int(input("Enter doctor ID to delete: "))
            Doctor.delete_doctor(doctor_id)
        
        elif choice == '4':
            break

def appointment_menu():
    while True:
        print("\n=== APPOINTMENT MANAGEMENT ===")
        print("1. Book New Appointment")
        print("2. View All Appointments")
        print("3. Back to Main Menu")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            patient_name = input("Enter patient name: ")
            doctor_name = input("Enter doctor name: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            
            appointment = Appointment(patient_name, doctor_name, date, time)
            appointment.book_appointment()
        
        elif choice == '2':
            Appointment.view_all_appointments()
        
        elif choice == '3':
            break

def main():
   
    create_tables()
    
    while True:
        print("\n" + "="*50)
        print("HOSPITAL MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            register_user()
        
        elif choice == '2':
            if login():
                while True:
                    print("\n=== MAIN MENU ===")
                    print("1. Patient Management")
                    print("2. Doctor Management")
                    print("3. Appointment Management")
                    print("4. Logout")
                    
                    main_choice = input("Enter choice: ")
                    
                    if main_choice == '1':
                        patient_menu()
                    elif main_choice == '2':
                        doctor_menu()
                    elif main_choice == '3':
                        appointment_menu()
                    elif main_choice == '4':
                        print("Logging out...")
                        break
        
        elif choice == '3':
            print("Thank you for using Hospital Management System!")
            break

if __name__ == "__main__":
    main()
