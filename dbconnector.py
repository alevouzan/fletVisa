import mysql.connector  # Import the MySQL connector

# Configuration for your database connection
db_config = {
    'host': 'localhost', 
    'user': 'root', 
    'password': 'admin', 
    'database': 'fletdb'
}

def connect_to_db():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None



def create_applicant(name, surname, email, country):
    """Saves a new visa applicant to the database."""
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO visa_applicants (name, surname, email, country, created_at) VALUES (%s, %s, %s, %s, NOW())",
            (name, surname, email, country)
        )
        conn.commit()  
        cursor.close()
        conn.close()
        return True  # Indicate success
    else:
       return False  # Indicate failure


def update_applicant(applicant_id, **kwargs):  # Accept any updates
    """Updates an existing visa applicant."""
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        query_parts = []
        args = []
        for key, value in kwargs.items():
            query_parts.append(f"{key} = %s")
            args.append(value)

        query = f"UPDATE visa_applicants SET {','.join(query_parts)} WHERE id = %s"
        args.append(applicant_id)

        cursor.execute(query, args)
        conn.commit()
        cursor.close()
        conn.close()


def set_applicant_status(applicant_id, complete):
    """Sets the 'complete' status of an applicant."""
    update_applicant(applicant_id, complete=complete)  # Reuse update_applicant



def get_visa_applicants():
    """Retrieves visa applicant data from the database."""
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()  
        cursor.execute("SELECT * FROM visa_applicants")  # Replace with your specific query
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    else:
        return None  # Indicate failure



