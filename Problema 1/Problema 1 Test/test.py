# Fisierele de testare incep intotdeauna cu "test_"
import pytest

# Sunt importate clasele si constantele din fisierul principal
from problema_1_test import Employee, Manager, TEAM_PREFIX, X_MOD_4

# NOTĂ: Pytest va rula toate functiile care incep cu 'test_'

def test_1_contorizare_si_creare():
    """Verifica daca contoarele globale (empCount si mgr_count) functioneaza corect la creare."""
    
    # 1. SETUP: Se seteaza contoarele la 0 pentru a asigura un mediu curat la inceputul testului
    Employee.empCount = 0
    Manager.mgr_count = 0

    # 2. ACT: Se creeaza obiecte
    emp = Employee("Test Emp", 100)
    mgr = Manager("Test Mgr", 200, {"T1": "New"}, "HR")

    # 3. ASSERT: Verificari
    # 1 Manager + 1 Employee = 2 angajati in total
    assert Employee.get_emp_count() == 2
    # 1 Manager
    assert Manager.mgr_count == 1
    
    # Curatare
    del emp
    del mgr


def test_2_prefixare_departament():
    """Verifica daca departamentul este prefixat corect la initializare."""
    dep_original = "Vanzari"
    mgr = Manager("Test Dep", 100, {}, dep_original)
    
    # Verificare: Prefixul plus numele original al departamentului
    assert mgr.department == TEAM_PREFIX + dep_original
    del mgr


def test_3_logica_display_X_mod_3_actual():
    """Verifica cazul X%4 = 3 (taskuri) - cazul tau real."""
    tasks = {"TestTask1": "Done", "TestTask2": "New"}
    mgr = Manager("Test X3", 1000, tasks, "IT")
    
    # Apelam metoda helper cu valoarea 3 (cazul taskurilor)
    rezultat_asteptat = "TestTask1, TestTask2"
    rezultat_real = mgr.get_display_info(3) 
    
    assert rezultat_real == rezultat_asteptat
    del mgr


def test_4_logica_display_X_mod_0_ipotetic():
    """Verifica un caz ipotetic (X%4 = 0) - trebuie sa returneze salariul."""
    # Setezi un salariu
    salariu_test = 50000
    mgr = Manager("Test X0", salariu_test, {}, "Fin")
    
    # Apelam metoda helper cu valoarea 0 (cazul salariului)
    rezultat_asteptat = salariu_test
    rezultat_real = mgr.get_display_info(0) 
    
    # Verificare
    assert rezultat_real == rezultat_asteptat
    del mgr
