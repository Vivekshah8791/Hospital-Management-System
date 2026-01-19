import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vivek@123", 
            database="hospital_db"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_tables():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS hospital_db")
        cursor.execute("USE hospital_db")
        
        # Create patients table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT,
                gender VARCHAR(10),
                address VARCHAR(200),
                contact VARCHAR(15),
                disease VARCHAR(100),
                doctor_assigned VARCHAR(100)
            )
        """)
        
        # Create doctors table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS doctors (
                doctor_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                specialization VARCHAR(100),
                age INT,
                contact VARCHAR(15),
                fees DECIMAL(10,2),
                salary DECIMAL(10,2)
            )
        """)
        
        # Create appointments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INT AUTO_INCREMENT PRIMARY KEY,
                patient_name VARCHAR(100),
                doctor_name VARCHAR(100),
                appointment_date DATE,
                time VARCHAR(20),
                status VARCHAR(20)
            )
        """)
        
        # Create users table for login
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(50) PRIMARY KEY,
                password VARCHAR(50) NOT NULL
            )
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Database and tables created successfully!")
