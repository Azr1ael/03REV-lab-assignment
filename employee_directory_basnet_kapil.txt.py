# Review Programming Assignment
# Program Description:
# This program manages a company employee directory using classes,
# objects, file read/write operations, and dictionaries.
# Your Name: Kapil Basnet
# Date: 10/03/2026


# Employee Class
class Employee:
    """Employee class to keep track of employee information."""

    # Initializer
    def __init__(self, ID=-999, name='', department='', pay=0.0):
        """Initialize a new employee object."""
        self.set_ID(ID)
        self.set_name(name)
        self.set_department(department)
        self.set_pay(pay)

    # Getters and setters
    def get_ID(self):
        """Return employee ID."""
        return self.ID

    def set_ID(self, ID):
        """Assign employee ID."""
        self.ID = ID

    def get_name(self):
        """Return employee name."""
        return self.name

    def set_name(self, name):
        """Assign employee name."""
        self.name = name

    def get_department(self):
        """Return employee department."""
        return self.department

    def set_department(self, department):
        """Assign employee department."""
        self.department = department

    def get_pay(self):
        """Return employee pay."""
        return self.pay

    def set_pay(self, pay):
        """Assign employee pay."""
        self.pay = pay

    # String method
    def __str__(self):
        """Return employee information as a string."""
        return (f'{self.get_ID()}\t{self.get_name()}\t'
                f'{self.get_department()}\t{self.get_pay()}')


# EmployeeDirectory Class
class EmployeeDirectory:
    """Track employee information in the directory."""

    def __init__(self):
        """Initialize employee_list and employee_dict."""
        self.employee_list = []
        self.employee_dict = {}

    def add_employee(self, employee):
        """Append employee object to employee_list."""
        # Check for duplicate employee ID
        for emp in self.employee_list:
            if emp.get_ID() == employee.get_ID():
                return

        self.employee_list.append(employee)

    def del_employee(self, employee):
        """Delete employee object from employee_list."""
        # Check whether employee ID exists
        for emp in self.employee_list:
            if emp.get_ID() == employee.get_ID():
                self.employee_list.remove(emp)
                return

        print(f'ID:{employee.get_ID()} does not exist, deletion is aborted')

    def read_file(self, file_name):
        """Read employee data from a file and return a list of objects."""
        employees = []

        with open(file_name, 'r') as infile:
            for line in infile:
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Handle comma, tab, or space delimiters cleanly
                data = line.replace(',', ' ').split()

                # Create an Employee object
                emp = Employee(
                    int(data[0]),
                    data[1],
                    data[2],
                    float(data[3])
                )

                employees.append(emp)

        return employees

    def update_employee_dir(self, file_name):
        """Read file and update employee_list."""
        self.employee_list = self.read_file(file_name)

    def write_to_file(self, file_name):
        """Write updated employee_list to a file."""
        with open(file_name, 'w') as outfile:
            for emp in self.employee_list:
                outfile.write(str(emp) + '\n')

    def write_to_dict(self):
        """Convert employee_list into a dictionary of lists."""

        self.employee_dict = {
            'ID': [],
            'name': [],
            'department': [],
            'pay': []
        }

        for emp in self.employee_list:
            self.employee_dict['ID'].append(emp.get_ID())
            self.employee_dict['name'].append(emp.get_name())
            self.employee_dict['department'].append(
                emp.get_department()
            )
            self.employee_dict['pay'].append(emp.get_pay())

    def display_dict(self):
        """Display employee dictionary in key/value pairs."""
        for key, value in self.employee_dict.items():
            print(f'{key} : {value}')


# Test Class
if __name__ == '__main__':

    try:
        # Create an EmployeeDirectory object
        directory = EmployeeDirectory()

        # Import existing employee information
        directory.update_employee_dir('employees.txt')

        # Create three new employee objects
        emp1 = Employee(106, 'Emp1', 'Accounting', 56000.0)
        emp2 = Employee(107, 'Emp2', 'Sales', 80000.0)
        emp3 = Employee(108, 'Emp3', 'Marketing', 90000.0)

        # Add emp1 and emp2 to the directory
        directory.add_employee(emp1)
        directory.add_employee(emp2)

        # Try to delete emp3
        directory.del_employee(emp3)

        # Write updated employee list to the file
        directory.write_to_file('employees.txt')

        # Convert employee list into a dictionary
        directory.write_to_dict()

        # Display the dictionary
        directory.display_dict()

    except FileNotFoundError as fnfe:
        print(fnfe)

    except KeyError as ke:
        print(ke)

    except Exception as ex:
        print(ex)

    finally:
        print('Program is completed')