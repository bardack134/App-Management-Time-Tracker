from tkinter import *
from tkinter.simpledialog import askstring
import datetime


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

#TODO: CREANDO 2 VENTANAS DIFERENTES, UNA PARA LA PANTALLA DE LA APP Y OTRA PARA VER INFORME DE DURACION



#TODO:AGREGAR TAREA A LA LISTA DE TAREAS
#funcion que se ejecuta cuando se da clik en el boton "add task"
def ask_task():
    global task
    global index
    
    # Solicita al usuario ingresar el nombre del nuevo proyecto
    task = askstring("input", "Add New Project")
    
    # Imprime el nombre del proyecto y el índice, para saber que si se estan obteniendo correctamente
    print(task, index)
    
    # Inserta el proyecto en la lista de tareas 
    task_list.insert(index, task)
    
    # Incrementa el índice
    index+=1


#TODO: AL OPRIMIR EL BOTON PLAY, EMPEZAR A CALCULAR EL TIEMPO DE INICIO DEL PROYECTO
def start_time():
    #vamos a seleccionar un item de la lista e imprimirlo en consola despues de oprimir el boton play
    task_get=task_list.get(ANCHOR)
    
    #seleccionado el item del listbox con exito y se imprime en consola
    print(f'the selected item by the user is {task_get}')
    
    current_time=datetime.datetime.now()
    formatted_time=current_time.strftime("%I:%M:%S:%p")
    print(f"The user started the task at the time {formatted_time}")
    print(current_time.hour-12)
    print(current_time.minute)
    print(current_time.second)

    play_button.config( text="Project Running")

#TODO: TITULO DE LA APP, BOTON AGREGAR TAREA, LISTA DE TAREAS, BOTON DE "PLAY"
#Titulo
# creamos un Frame con un color de fondo azul y lo expandimos para que ocupe toda la fila.
title_frame=Frame(window, bg=BLUE)

nb_of_columns = 2

# 'ew' hace que el frame se expanda horizontalmente, el widget se adhiere a los lados este y oeste de la celda.
title_frame.grid(row=0, column=0, sticky='ew', columnspan=nb_of_columns, pady=5)

# Empaquetamos el título dentro de el frame
title=Label(title_frame, text="Projects", bg=BLUE, fg="white", font=("Arial", 10, "bold"), width=30 )

title.pack()


#boton de agregar tareas
add_task=Button(window, text="Add New Project", width=30,  bg=PURPLE, fg="white", font=("Arial", 10, "bold"), command=ask_task)
add_task.grid(row=1, column=1, pady=6 )

#Lista de tareas
task_list=Listbox(width=30 )
task_list.grid(row=2, column=1,  pady=5)

#boton de play
play_button=Button(window, text="Play", command=start_time)
play_button.grid(row=3, column=1, pady=5)

#boton de "ver informe de duracion"
report_button=Button(window, text="Duration Report")
report_button.grid(row=4, column=1, pady=5)

window.mainloop()






