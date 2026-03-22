class Employee:
    def __init__(self, id, name, salary):
        self.id = id 
        self.name = name
        self.salary = salary

class EmployeeDirector(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)
        self._team = []

    @property
    def team(self):
        return self._team
    
    def add_team(self, member):
        if member not in self._team:
            self._team.append(member)
        else:
            print("This Member Alredy Exists!")

employee_1 = Employee(12345, "Guilherme Sobrenome", 4000)
employee_2 = Employee(52134, "Ruan Sobrenome", 4500)
employee_3 = Employee(54321, "Lanilsson Sobrenome", 2300)

director_1 = EmployeeDirector(
    11111, 
    "Fernando Sobrenome", 
    40000
    )


print(f"Current team members: {director_1.team}")
for i in (employee_3.id, employee_2.id, employee_1.id):
    director_1.add_team(i)
print(f"Current team members: {director_1.team}")
director_1.add_team(employee_3.id)
print(f"Current team members: {director_1.team}")