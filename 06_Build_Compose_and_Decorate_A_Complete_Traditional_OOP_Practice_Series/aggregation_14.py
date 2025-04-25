# 14.  Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.


from colorama import init, Fore, Style # type: ignore

# Initialize colorama
init(autoreset=True)

# 🏢 Main Heading
print(Fore.MAGENTA + Style.BRIGHT + "\n========== 🏢 DEPARTMENT & EMPLOYEE AGGREGATION SYSTEM ==========\n")

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return Fore.YELLOW + f"👤 Employee: {self.name} | ID: {self.emp_id}"
    


class Department:
    def __init__(self, dept_name, employee):
        
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Department HAS-A reference to an existing Employee




    def show_department_info(self):
        print(Fore.CYAN + f"🏢 Department: {self.dept_name}")
        print(self.employee.get_details())



# Create an Employee (exists independently)
emp1 = Employee("Ayesha Khan", 102)



# Pass the Employee to a Department (aggregation)
dept1 = Department("Human Resources", emp1)



# Display the department info
dept1.show_department_info()
