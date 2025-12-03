
# CONSTANTE GLOBALE
X = 19
Y = 4
TEAM_PREFIX = "Echipa_A_Info_"

X_MOD_4 = X % 4           # 19 % 4 = 3 (Afișează Taskurile)
NUM_MANAGERS = Y // 3     # 4 // 3 = 1 (Creează 1 obiect Manager)

# CLASA EMPLOYEE (MODIFICATĂ PENTRU TESTARE)
class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    # METODĂ NOUĂ PENTRU TESTARE (Returnează contorul)
    @staticmethod
    def get_emp_count():
        return Employee.empCount
    
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
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

# CLASA MANAGER (MODIFICATĂ PENTRU TESTARE)
class Manager(Employee):
    # Variabila de clasa pentru numarul de Manageri
    mgr_count = 0

    def __init__(self, name, salary, tasks, department):
        super().__init__(name, salary)
        
        # Prefixez departamentul cu numele echipei
        self.department = TEAM_PREFIX + department
        self.tasks = tasks
        
        # Incrementez contorul Manager
        Manager.mgr_count += 1

    # METODĂ NOUĂ PENTRU TESTARE (Returnează valoarea cerută de X%4)
    def get_display_info(self, X_mod_4_test):
        """Returneaza informatia ceruta de tema in functie de X_mod_4_test."""
        if X_mod_4_test == 0:
            return self.salary
        elif X_mod_4_test == 1:
            return self.name
        elif X_mod_4_test == 2:
            return self.department
        elif X_mod_4_test == 3:
            return ', '.join(self.tasks.keys())
        return None 
    
    # Metoda display_employee modificată pentru a folosi helper-ul
    def display_employee(self):
        """Suprascrie metoda pentru a afisa un singur atribut, bazat pe X%4."""
        info = self.get_display_info(X_MOD_4) 
        
        if X_MOD_4 == 0:
            print(f"[Manager] Salariu: {info}")
        elif X_MOD_4 == 1:
            print(f"[Manager] Nume: {info}")
        elif X_MOD_4 == 2:
            print(f"[Manager] Departament: {info}")
        elif X_MOD_4 == 3:
            print(f"[Manager] Taskuri: {info}")

# RULAREA TEMEI (Problema 1)
def run_problema1():
    print("=== RULARE PROBLEMA 1 (Clase) ===")
    
    # Resetăm contoarele pentru a asigura un output curat al rulării finale
    Employee.empCount = 0
    Manager.mgr_count = 0

    # Creare obiecte Employee
    emp1 = Employee("John Doe", 5000)
    emp2 = Employee("Jane Smith", 6000)

    # Creare Y/3 obiecte Manager (adica 1 obiect)
    managers = []
    tasks_data = {"Planificare Trimestriala": "Finalizat", "Coordonare Resurse": "In Progress"}

    if NUM_MANAGERS > 0:
        mgr1 = Manager("Mike Ross", 9000, tasks_data, "Dezvoltare Produs")
        managers.append(mgr1)

    # Se apeleaza metoda 'display_employee' pentru toate obiectele Employee si Manager
    print("\n--- Apel display_employee ---")
    emp1.display_employee()
    emp2.display_employee()

    for mgr in managers:
        mgr.display_employee()

    # Se afiseaza valoarea atributului emp_count printr-o instanta Employee si una Manager
    print("\n--- Contoare ---")
    print(emp1.empCount) 

    if managers:
        print(managers[0].empCount)
        print(f"Contor Manageri: {managers[0].mgr_count}")


if __name__ == '__main__':
    run_problema1()
