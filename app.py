# app.py

import_data = username = input("Do you want to import data?")

if import_data == "y":
    import modules.data.tasks
else:
    tasks=[]

import modules.task_functions as tarea
import modules.output as bob
import modules.input as resultado

while (True):
    bob.print_menu()
    option = resultado.selected_inp()
    if (option.lower() == 'q'):
        break
    if option == '1':
        bob.print_list(tarea.tasks)
    elif option == '2':
        bob.print_list(tarea.get_uncompleted_tasks(tarea.tasks))
    elif option == '3':
        bob.print_list(tarea.get_completed_tasks(tarea.tasks))
    elif option == '4':
        description = resultado.selected_task()
        task = tarea.get_task_with_description(tarea.tasks, description)
        if task is not None:
            tarea.mark_task_complete(task)
            bob.print("Task marked complete")
        else:
            bob.print("Task not found")
    elif option == '5':
        time = resultado.selected_dur()
        bob.print_list(tarea.get_tasks_taking_at_least(tarea.tasks, time))
    elif option == '6':
        resultado.selected_task()
        bob.print(tarea.get_task_with_description(tarea.tasks, description))
    elif option == '7':
        description = resultado.enter_desc()
        time_taken = resultado.enter_time_taken()
        task = tarea.create_task(description, time_taken)
        tarea.tasks.append(task)
    else:
        bob.print("Invalid Input - choose another option")