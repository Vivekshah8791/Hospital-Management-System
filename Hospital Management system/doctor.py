from database import get_connection

class Doctor:
    def __init__(self, name, specialization, age, contact, fees, salary):
        self.name = name
        self.specialization = specialization
        self.age = age
        self.contact = contact
        self.fees = fees
        self.salary = salary
    
    def add_doctor(self):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO doctors (name, specialization, age, contact, fees, salary)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (self.name, self.specialization, self.age, 
                     self.contact, self.fees, self.salary)
            cursor.execute(query, values)
            conn.commit()
            print(f"Doctor {self.name} added successfully!")
            cursor.close()
            conn.close()
    
    @staticmethod
    def view_all_doctors():
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM doctors")
            doctors = cursor.fetchall()
            
            if doctors:
                print("\n" + "="*80)
                print("DOCTOR RECORDS")
                print("="*80)
                for doctor in doctors:
                    print(f"ID: {doctor[0]}, Name: {doctor[1]}, Specialization: {doctor[2]}, "
                          f"Contact: {doctor[4]}, Fees: Rs.{doctor[5]}")
                print("="*80)
            else:
                print("No doctors found!")
            
            cursor.close()
            conn.close()
    
    @staticmethod
    def delete_doctor(doctor_id):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM doctors WHERE doctor_id = %s", (doctor_id,))
            conn.commit()
            print(f"Doctor with ID {doctor_id} deleted successfully!")
            cursor.close()
            conn.close()
