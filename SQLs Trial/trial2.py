import psycopg2
from db_config import DB_CONFIG


# connect to the database
def connect():
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to Database:{e}")
        return None


# initailiseing the databse


def init_db():

    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """
                CREATE TABLE  IF NOT EXISTS employee (id SERIAL PRIMARY KEY, 
                name VARCHAR(70) NOT NULL, 
                age INT NOT NULL, 
                department VARCHAR NOT NULL); """
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True


# Operations for CRUD


def add_employee(name, age, department):
    try:
        connection = connect()
        if connection is None:
            return False
        cursor = connection.cursor()

        cursor.execute(
            """
                       INSERT INTO employee(name, age, department)
                       VALUES (%s, %s, %s) RETURNING id""",
            (name, age, department),
        )
        employee_id = cursor.fetchone()[0]
        connection.commit()
        print(f"Employee has been added. New employee ID is {employee_id}")
        return True
    except psycopg2.Error as e:
        print(f"Erro adding enew employee {e}")
        return False
    finally:
        if connection:
            cursor.close()
            connection.close()


def view_employee():
    try:
        connection = connect()
        if connection is None:
            return False
        cursor = connection.cursor()

        # SQL for viewing
        cursor.execute(""" SELECT * FROM employee ORDER BY id;""")
        employees = cursor.fetchall()
        return employees
    except psycopg2.Error as e:
        print(f"Error Viewing Employees:{e}")
        return None
    finally:
        if connection:
            cursor.close()
            connection.close()


def update_table(employee_id, name, age, department):
    try:

        connection = connect()
        if connection is None:
            return False

        cursor = connection.cursor()

        # Building Update Query
        query = "UPDATE employee SET "
        params = []

        if name:
            query += "name = %s, "
            params.append(name)
        if age:
            age = int(age)
            query += "age = %s, "
            params.append(age)
        if department:
            query += "department = %s, "
            params.append(department)

        # removing last comma in query
        query = query.rstrip(", ")

        # adding Where clause and id
        query += "WHERE id = %s; "
        params.append(employee_id)

        # execute the query
        cursor.execute(query, params)

        if cursor.rowcount == 0:
            print(f"Employee with ID {employee_id} not found")
            return False

        connection.commit()
        print(f"Employee with ID {employee_id} is updated")
        return True
    except psycopg2.Error as e:
        print(f"Error Updating Employee:{e}")
        return False
    finally:
        if connection:
            cursor.close()
            connection.close()


def delete(employee_id):
    try:
        connection = connect()
        if connection is None:
            return False

        cursor = connection.cursor()

        cursor.execute("""DELETE FROM employee WHERE id = %s""", (employee_id,))

        if cursor.rowcount == 0:
            print(f"Employee  with id {employee_id} not found")
            return False

        connection.commit()
        print(f"EMployee with ID {employee_id} has been deleted")
        return True
    except psycopg2.Error as e:
        print(f"Error with Deleting employee:{e}")
        return False
    finally:
        if connection:
            cursor.close()
            connection.close()


def main():

    if not init_db():
        print("Falied to initilaise Database")
        return

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice of operation (1-5): ")

        if choice == "1":
            name = input("Enter the name of the employee:")
            while True:
                try:
                    age = int(input("Enter employee age: "))
                    break
                except ValueError:
                    print("Please enter a valid number for age")

            department = input("Enter employee department: ")
            add_employee(name, age, department)
        elif choice == "2":
            employees = view_employee()
            if employees:
                print("\n----- EMPLOYEE LIST -----")
                print(f"{'ID':<5}{'Name':<20}{'Age':<10}{'Department':<20}")
                print("-" * 55)

                for employee in employees:
                    print(
                        f"{employee[0]:<5}{employee[1]:<20}{employee[2]:<10}{employee[3]:<20}"
                    )
            else:
                print("No employees found or error retrieving data")
        elif choice == "3":
            employee_id = int(
                input("Enter the ID of the employee record to be updated")
            )

            print("Leave empty for no change")
            name = input("Enter new name:(Press Enter to keep current)")
            age = input("Enter new age:(Press Enter to keep current)")
            department = input("Enter new department:(Press Enter to keep current)")

            if not name:
                name = None
            if not age:
                age = None

            update_table(employee_id, name, age, department)
        elif choice == "4":
            employee_id = int(
                input("Enter the ID of the employee record to be deleted")
            )
            delete(employee_id)

        elif choice == "5":
            print("Exiting the system")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5")


if __name__ == "__main__":
    main()
