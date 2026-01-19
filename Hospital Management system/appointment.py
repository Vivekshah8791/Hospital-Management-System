from database import get_connection
from datetime import datetime

class Appointment:
    def __init__(self, patient_name, doctor_name, appointment_date, time):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_date = appointment_date
        self.time = time
        self.status = "Scheduled"
    
    def book_appointment(self):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO appointments (patient_name, doctor_name, appointment_date, time, status)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (self.patient_name, self.doctor_name, self.appointment_date, 
                     self.time, self.status)
            cursor.execute(query, values)
            conn.commit()
            print("Appointment booked successfully!")
            cursor.close()
            conn.close()
    
    @staticmethod
    def view_all_appointments():
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM appointments")
            appointments = cursor.fetchall()
            
            if appointments:
                print("\n" + "="*80)
                print("APPOINTMENT RECORDS")
                print("="*80)
                for appt in appointments:
                    print(f"ID: {appt[0]}, Patient: {appt[1]}, Doctor: {appt[2]}, "
                          f"Date: {appt[3]}, Time: {appt[4]}, Status: {appt[5]}")
                print("="*80)
            else:
                print("No appointments found!")
            
            cursor.close()
            conn.close()
