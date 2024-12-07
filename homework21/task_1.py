import json

def read_json_file(input_file):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file '{input_file}' is not a valid JSON file.")
        return {}

class Employee:
    def __init__(self, name: str, position: str, salary: int):
        self.name = name
        self.position = position
        self.salary = salary

class Department:
    def __init__(self,dep_name = str,description = str,employees = list[Employee]):
        self.dep_name = dep_name
        self.description = description
        self.employees = employees
        
    def average(self):
        if not self.employees:
            return 0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)
    
    def max_salary(self):
        if not self.employees:
            return 0
        max_salary = max(emp.salary for emp in self.employees)    
        return max_salary
    
    def min_salary(self):
        if not self.employees:
            return 0
        min_slary = min(emp.salary for emp in self.employees)    
        return min_slary
    
    def positions(self):
        
        position_counts = {}
        for emp in self.employees:
            position_counts[emp.position] = position_counts.get(emp.position, 0) + 1
        return position_counts    
    
def main():
    data = read_json_file('homework21/data.json')
    if data:
        departments = []
        for dep_key, dep_info in data.items():
            employees = [
                Employee(emp["name"], emp["position"], int(emp["salary"]))
                for emp in dep_info["employees"]
            ]
            department = Department(dep_info["name"], dep_info["description"], employees)
            departments.append(department)
            
        for department in departments:
            print(f"\nDepartment: {department.dep_name}")
            print(f"Description: {department.description}")
            print(f"Average Salary: {department.average():.2f}")
            print(f"Max Salary: {department.max_salary()}")
            print(f"Min Salary: {department.min_salary()}")
            print("Positions Count:", department.positions())

if __name__ == '__main__':
    main()