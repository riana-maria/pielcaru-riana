import math

X = 19
Y = 4
TEAM_PREFIX = "Echipa_A_Info_"

X_MOD_4 = X % 4
NUM_MANAGERS = Y // 3


# Clasa Employee
class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        # Am sesizat greseala de sintaxa la emp_count, corectat la empCount
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        # Metoda originala
        print(f"[Employee] Nume : {self.name}, Salariu: {self.salary}")

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        # Am eliminat deoarece nu erau necesare
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


# Am construit clasa Manager care mosteneste clasa Employee
class Manager(Employee):
    # Variabila de clasa pentru numarul de Manageri
    mgr_count = 0

    def __init__(self, name, salary, tasks, department):
        # Apel la constructorul clasei parinte (pentru a initializa atributele name, salary si empCount)
        super().__init__(name, salary)

        # Prefixez departamentul cu numele echipei
        self.department = TEAM_PREFIX + department
        self.tasks = tasks

        # Incrementez contorul Manager
        Manager.mgr_count += 1

    def display_employee(self):
        """Suprascrie metoda pentru a afisa un singur atribut, bazat pe X%4."""
        if X_MOD_4 == 0:
            # Daca X%4==0: afiseaza doar salariul angajatului
            print(f"[Manager] Salariu: {self.salary}")

        elif X_MOD_4 == 1:
            # Daca X%4==1: afiseaza doar numele angajatului
            print(f"[Manager] Nume: {self.name}")

        elif X_MOD_4 == 2:
            # Daca X%4==2: afiseaza doar departamentul
            print(f"[Manager] Departament: {self.department}")

        elif X_MOD_4 == 3:
            # Daca X%4==3: afiseaza doar numele taskurilor
            task_names = ', '.join(self.tasks.keys())
            print(f"[Manager] Taskuri: {task_names}")


# Creare obiecte Employee
emp1 = Employee("John Doe", 5000)
emp2 = Employee("Jane Smith", 6000)

# Creare Y/3 obiecte Manager (adica 1 obiect)
managers = []
tasks_data = {
    "Planificare Trimestriala": "Finalizat",
    "Coordonare Resurse": "In Progress"
}

if NUM_MANAGERS > 0:
    mgr1 = Manager("Mike Ross", 9000, tasks_data, "Dezvoltare Produs")
    managers.append(mgr1)

# Se apeleaza metoda 'display_employee' pentru toate obiectele Employee si Manager
emp1.display_employee()
emp2.display_employee()

for mgr in managers:
    mgr.display_employee()

# Se afiseaza valoarea atributului emp_count printr-o instanta Employee si una Manager
print(emp1.empCount)

if managers:
    print(managers[0].empCount)
