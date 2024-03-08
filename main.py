from tkinter import *
from tkinter.simpledialog import askstring
#VARIABLES GLOBALES Y CONSTANTES
BEIGE="#FFF6E9"
BLUE="#40A2E3"
PURPLE="#AD88C6"
index=1


#TODO: CONFIGURACION DE LA VENTANA
window=Tk()

#titulo para la ventana
window.title('Time management')

#fondo de nuestra ventana
window.config(bg=BEIGE, padx=30, pady=20, )

window.geometry("300x350")

#TODO:AGREGAR TAREA A LA LISTA DE TAREAS
#funcion que se ejecuta cuando se da clik en el boton "add task"
def ask_task():
    global task
    global index
    
    task = askstring("input", "Add New Project")
    
    print(task, index)
     
    task_list.insert(index, task)
    
    index+=1


#TODO: titulo de la app, boton agregar tarea, lista de tareas, boton de "play"
#Titulo
# creamos un Frame con un color de fondo azul y lo expandimos para que ocupe toda la fila.
title_frame=Frame(window, bg=BLUE)

nb_of_columns = 2

# 'ew' hace que el frame se expanda horizontalmente, el widget se adhiere a los lados este y oeste de la celda.
title_frame.grid(row=0, column=0, sticky='ew', columnspan=nb_of_columns, pady=5)

title=Label(title_frame, text="Projects", bg=BLUE, fg="white", font=("Arial", 10, "bold"), width=30 )

title.pack()


#boton de agregar tareas
add_task=Button(window, text="Add New Project", width=30,  bg=PURPLE, fg="white", font=("Arial", 10, "bold"), command=ask_task)
add_task.grid(row=1, column=1, pady=6 )

#Lista de tareas
task_list=Listbox(width=30 )
task_list.grid(row=2, column=1,  pady=5)

#boton de play
play_button=Button(window, text="Play")
play_button.grid(row=3, column=1, pady=5)

#boton de "ver informe de duracion"
report_button=Button(window, text="Duration Report")
report_button.grid(row=4, column=1, pady=5)

window.mainloop()