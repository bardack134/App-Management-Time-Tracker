from tkinter import *
from tkinter.simpledialog import askstring
import datetime


#VARIABLES GLOBALES Y CONSTANTES
BEIGE="#FFF6E9"
BLUE="#40A2E3"
PURPLE="#AD88C6"
PEACH="#FEECE2"
index=1
overall_hours=0
overall_minutes=0
overall_seconds=0


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
    #convierto task_get, start_hour, start_minute, start_second en variables Globales para usarlas en otras funciones
    global task_get
    global start_hour
    global start_minute
    global start_seconds
            
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
    
    
    # Imprime en consola la hora de inicio del proyecto (en formato de 24 horas), para hacer los calculos matematicos mas facilmente
    start_hour=int((current_time.strftime("%H")))
    print(type(start_hour))
    print(start_hour)
    
    # Imprime en consola el minuto de inicio del proyecto
    start_minute=int((current_time.strftime("%M")))
    print(type(start_minute))
    print(start_minute)
    
    # Imprime en consola los segundos  de inicio del proyecto
    start_seconds=int((current_time.strftime("%S")))
    print(type(start_seconds))
    print(start_seconds)
    
    # Cambia el texto del botón "play" a "Project Running"
    play_button.config( text="Project Running")
    
    # Inserta la cadena de texto creada en el widget "duration_report"
    duration_report.insert(INSERT, data)
    
  
#TODO: FUNCION PARA SABER LA HORA A LA HORA DE OPRIMIR EL BOTON "STOP" 

def stop():
    #declartando variables glopbales que usare dentro de la session
    global overall_hours
    global overall_minutes
    global overall_seconds
    
    # Obtiene la hora actual
    current_time=datetime.datetime.now()
    
    # Formatea la hora actual en el formato de 12 horas con AM/PM
    stop_time=current_time.strftime("%I:%M:%S:%p")      
    
    # Crea una cadena de texto con la tarea seleccionada y la hora de inicio
    data = f"'\n{task_get}' ended at {stop_time}"
    
    # Inserta la cadena de texto creada en el widget "duration_report"
    duration_report.insert(INSERT, data)
    
    # Imprime en consola la hora actual (en formato de 24 horas), para hacer los calculos matematicos mas facilmente
    end_hour=int((current_time.strftime("%H")))
    print(type(end_hour))
    print(end_hour)
    
    # Imprime en consola los minutos actuales
    end_minute=int((current_time.strftime("%M")))
    print(type(end_minute))
    print(end_minute)
    
    # Imprime en consola los segundos actuales
    end_seconds=int((current_time.strftime("%S")))
    print(type(end_seconds))
    print(end_seconds)
    
    #calculando el tiempo que duro la seccion de proyecto
    total_hours=start_hour-end_hour
    total_minutes=start_minute-end_minute
    total_seconds=start_seconds-end_seconds
    total_time=f"\nSession duration: {abs((total_hours))} h, {abs((total_minutes))} min, {abs((total_seconds))} s\n"
    
    #calculando el tiempo total empleado hasta hora en todas las sessiones
    overall_hours += total_hours
    overall_minutes += total_minutes
    overall_seconds += total_seconds
    overall_time=f"\nTotal Report: {abs((overall_hours))} h, {abs((overall_minutes))} min, {abs((overall_seconds))} s\n \n"     
    
    #muestro el tiempo total empleado en la tarea al usuario en el widget "duration_report"
    duration_report.insert(INSERT, total_time)
    duration_report.insert(INSERT, overall_time)
    
    
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
duration_report=Text(window, bg=PEACH, width=40,height=20, font=("Arial", 13))
duration_report.grid(row=2, column=1, padx=15)
                        
                        




window.mainloop()