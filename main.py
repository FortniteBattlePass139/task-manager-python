# Task Manager en consola
# Autor: Rodrigo Monsalve Vasquez
# Descripción: Aplicación simple en Python para gestionar tareas desde la terminal

import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def show_tasks(tasks):
    if not tasks:
        print("\nNo hay tareas registradas.\n")
        return
    print("\nLista de tareas:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['title']}")
    print()

def add_task(tasks):
    title = input("Ingresa el título de la tarea: ").strip()
    if not title:
        print("El título no puede estar vacío.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Tarea agregada correctamente.")

def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Número de la tarea a marcar como completada: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            save_tasks(tasks)
            print("Tarea marcada como completada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Debes ingresar un número válido.")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Número de la tarea a eliminar: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Tarea eliminada: {removed['title']}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Debes ingresar un número válido.")

def menu():
    print("==== TASK MANAGER ====")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    tasks = load_tasks()
    while True:
        menu()
        option = input("Elige una opción: ").strip()
        if option == "1":
            show_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
