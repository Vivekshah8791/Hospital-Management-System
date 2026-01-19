from database import get_connection

class Patient:
    def __init__(self, name, age, gender, address, contact, disease, doctor_assigned):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.contact = contact
        self.disease = disease
        self.doctor_assigned = doctor_assigned
    
    def add_patient(self):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO patients (name, age, gender, address, contact, disease, doctor_assigned)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (self.name, self.age, self.gender, self.address, 
                     self.contact, self.disease, self.doctor_assigned)
            cursor.execute(query, values)
            conn.commit()
            print(f"Patient {self.name} added successfully!")
            cursor.close()
            conn.close()
    
    @staticmethod
    def view_all_patients():
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM patients")
            patients = cursor.fetchall()
            
            if patients:
                print("\n" + "="*80)
                print("PATIENT RECORDS")
                print("="*80)
                for patient in patients:
                    print(f"ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}, "
                          f"Gender: {patient[3]}, Contact: {patient[5]}, Disease: {patient[6]}")
                print("="*80)
            else:
                print("No patients found!")
            
            cursor.close()
            conn.close()
    
    @staticmethod
    def search_patient(name):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM patients WHERE name LIKE %s", (f"%{name}%",))
            patients = cursor.fetchall()
            
            if patients:
                for patient in patients:
                    print(f"\nID: {patient[0]}")
                    print(f"Name: {patient[1]}")
                    print(f"Age: {patient[2]}")
                    print(f"Gender: {patient[3]}")
                    print(f"Address: {patient[4]}")
                    print(f"Contact: {patient[5]}")
                    print(f"Disease: {patient[6]}")
                    print(f"Doctor: {patient[7]}")
            else:
                print("Patient not found!")
            
            cursor.close()
            conn.close()
    
    @staticmethod
    def delete_patient(patient_id):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM patients WHERE patient_id = %s", (patient_id,))
            conn.commit()
            print(f"Patient with ID {patient_id} deleted successfully!")
            cursor.close()
            conn.close()
