from tkinter import *
from tkinter.simpledialog import askstring
import datetime


#VARIABLES GLOBALES Y CONSTANTES
BEIGE="#FFF6E9"
BLUE="#40A2E3"
PURPLE="#AD88C6"
PEACH="#FEECE2"
index=1


#TODO: CONFIGURACION DE LA VENTANA
window=Tk()

#titulo para la ventana
window.title('Time management')

#fondo de nuestra ventana
window.config(bg=BEIGE, padx=30, pady=20, )

# window.geometry("300x350")




#TODO:AGREGAR TAREA A LA LISTA DE TAREAS
#funcion que se ejecuta cuando se da clik en el boton "add task"
def ask_task():
    global task
    global index
    
    # Solicita al usuario ingresar el nombre del nuevo proyecto
    task = askstring("input", "Add New Project").capitalize()
    
    # Imprime el nombre del proyecto y el índice, para saber que si se estan obteniendo correctamente
    print(task, index)
    
    # Inserta el proyecto en la lista de tareas 
    task_list.insert(index, task)
    
    # Incrementa el índice
    index+=1


#TODO: AL OPRIMIR EL BOTON PLAY, EMPEZAR A CALCULAR EL TIEMPO DE INICIO DEL PROYECTO
def start_time():
    #convierto task_get en variable Global para usarla en otras funciones
    global task_get
    
    # Selecciona un ítem de la lista (el que esté seleccionado en ese momento), al oprimir el boton play
    task_get=task_list.get(ANCHOR).capitalize()
    
    #seleccionado el item del listbox con exito y se imprime en consola
    print(f'the selected item by the user is {task_get}')
    
    # Obtiene la hora actual
    current_time=datetime.datetime.now()
    
    # Formatea la hora actual en el formato de 12 horas con AM/PM
    start_time=current_time.strftime("%I:%M:%S:%p")
    
    # Crea una cadena de texto con la tarea seleccionada y la hora de inicio
    data = f"'{task_get}' started at {start_time}"
    
    # Imprime en consola la cadena de texto creada
    print(data)
    
    # Imprime en consola la hora actual (en formato de 12 horas)
    print(current_time.hour-12)
    
    # Imprime en consola los minutos actuales
    print(current_time.minute)
    
    # Imprime en consola los segundos actuales
    print(current_time.second)
    
    # Cambia el texto del botón "play" a "Project Running"
    play_button.config( text="Project Running")
    
    # Inserta la cadena de texto creada en el widget "duration_report"
    duration_report.insert(INSERT, data)
    
  
#TODO: FUNCION PARA SABER LA HORA A LA HORA DE OPRIMIR EL BOTON "STOP" 

def stop():
    # Obtiene la hora actual
    current_time=datetime.datetime.now()
    
    # Formatea la hora actual en el formato de 12 horas con AM/PM
    stop_time=current_time.strftime("%I:%M:%S:%p")      
    
    # Crea una cadena de texto con la tarea seleccionada y la hora de inicio
    data = f"'\n{task_get}' started at {stop_time}"
    
    # Inserta la cadena de texto creada en el widget "duration_report"
    duration_report.insert(INSERT, data)
    
    #calculando el tiempo que duro la seccion de proyecto
    
    
#TODO: TITULO DE LA APP, BOTON AGREGAR TAREA, LISTA DE TAREAS, BOTON DE "PLAY"
#Titulo
# creamos un Frame con un color de fondo azul y lo expandimos para que ocupe toda la fila.
title_frame=Frame(window, bg=BLUE)

nb_of_columns = 2

# 'ew' hace que el frame se expanda horizontalmente, el widget se adhiere a los lados este y oeste de la celda.
title_frame.grid(row=0, column=0, sticky='ew', columnspan=nb_of_columns, pady=5)

# Empaquetamos el título dentro de el frame
title=Label(title_frame, text="Projects", bg=BLUE, fg="white", font=("Arial", 10, "bold") )

title.pack()


#creando frame para poner el boton agregar tareas adentro
add_task_frame=Frame(window, bg=BEIGE)

# 'ew' hace que el frame se expanda horizontalmente, el widget se adhiere a los lados este y oeste de la celda.
add_task_frame.grid(row=1, column=0, sticky='ew', columnspan=nb_of_columns, pady=5)

#Empaquetamos boton de agregar tareas dentro del add_task_frame
add_task=Button(add_task_frame, text="Add New Project",   bg=PURPLE, fg="white", font=("Arial", 10, "bold"), command=ask_task)
add_task.pack()


#Lista de tareas
task_list=Listbox(width=15, font=("Arial", 13, "bold") )
task_list.grid(row=2, column=0,  pady=5)


#boton de play
play_button=Button(window, text="Play", command=start_time)
play_button.grid(row=3, column=0, pady=5)


#boton de "ver informe de duracion"
stop_button=Button(window, text="Stop Project", command=stop)
stop_button.grid(row=3, column=1, pady=5)



#TODO: CREANDO TEXT WIDGET PARA MOSTRAR INFORMACION AL USER DEL TIEMPO DE DURACION DE CADA TAREA
duration_report=Text(window, bg=PEACH, width=30,height=20, font=("Arial", 13))
                                   
duration_report.grid(row=2, column=1, padx=15)
                        
                        




window.mainloop()