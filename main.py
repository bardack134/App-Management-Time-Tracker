from tkinter import *

from tkinter import messagebox

from tkinter.filedialog import asksaveasfile
from tkinter.simpledialog import askstring
import datetime


#VARIABLES GLOBALES Y CONSTANTES
BEIGE="#FFF6E9"
BLUE="#40A2E3"
PURPLE="#AD88C6"
PEACH="#FEECE2"
ORANGE="#FFCF96"
index=1
overall_hours=0
overall_minutes=0
overall_seconds=0
#esta variable comprobara que el "start time" haya sido chequiado
running=False

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
    global first_time
    global running        
    # Selecciona un ítem de la lista (el que esté seleccionado en ese momento), al oprimir el boton play
    task_get=task_list.get(ANCHOR).capitalize()
    
    #mostrar error en pantalla en caso de que el usuario de click a 'play' sin seleccionar una tarea
    if task_get=="":
        messagebox.showerror("showerror", "there is not task selected")               
    
    #si el usuario selecciono tarea
    else:
        #cambiamos el valor de la variable de 'False' a 'True' para indicar que el tiempo de inicio fue calculado
        running=True
            
        #seleccionado el item del listbox con exito y se imprime en consola
        print(f'the selected item by the user is {task_get}')
        
        # Obtiene la hora actual
        first_time=datetime.datetime.now()
        
        # Formatea la hora actual en el formato de 12 horas con AM/PM
        start_time=first_time.strftime("%I:%M:%S:%p")
        
        # Crea una cadena de texto con la tarea seleccionada y la hora de inicio
        data = f"{start_time} started '{task_get}'  "
        
        # Imprime en consola la cadena de texto creada
        print(data)
        
        
        # Imprime en consola la hora de inicio del proyecto (en formato de 24 horas), para hacer los calculos matematicos mas facilmente
        # start_hour=int((current_time.strftime("%H")))
        # print(type(start_hour))
        # print(start_hour)
        
        # # Imprime en consola el minuto de inicio del proyecto
        # start_minute=int((current_time.strftime("%M")))
        # print(type(start_minute))
        # print(start_minute)
        
        # # Imprime en consola los segundos  de inicio del proyecto
        # start_seconds=int((current_time.strftime("%S")))
        # print(type(start_seconds))
        # print(start_seconds)
        
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
    global running
    #mostrar error en pantalla en caso de que el usuario de click a 'play' sin seleccionar una tarea
    if task_get=="":
        messagebox.showerror("showerror", "You haven't started any projects.")               
    
    #si el usuario selecciono tarea
    elif running==True:
        
        #cambiamos el valor de 'True' a 'False' para indicar que el tiempo de ejecucion del proyecto ya se detuvbo
        running=False
        # Cambia el texto del botón "play" de "Project Running" a nuevamente "play"
        play_button.config( text="Play")
        
        # Obtiene la hora actual
        later_time=datetime.datetime.now()
        
        # Formatea la hora actual en el formato de 12 horas con AM/PM
        stop_time=later_time.strftime("%I:%M:%S:%p")      
        
        # Crea una cadena de texto con la tarea seleccionada y la hora de inicio
        data = f"'\n{stop_time} ended '{task_get}' "
        
        # Inserta la cadena de texto creada en el widget "duration_report"
        duration_report.insert(INSERT, data)
        
        # Imprime en consola la hora actual (en formato de 24 horas), para hacer los calculos matematicos mas facilmente
        
        # Calcular la diferencia de tiempo entre 'later_time' y 'first_time'
        total_time=later_time-first_time
        
        
        # Dividir los segundos totales por 3600 para obtener las horas completas
        hours=total_time.seconds //3600
        
        # Dividir los segundos totales por 60 para obtener los minutos totales,
        # yluego usar % 60 para obtener los minutos más allá de las horas completas
        minutes =(total_time.seconds //60)%60
        
        # Usar % 60 para obtener los segundos que no completan un minuto
        seconds=total_time.seconds%60
        
        
        total_time=f"\n'{task_get}' Session duration: {abs((hours))} h, {abs((minutes))} min, {abs((seconds))} s\n"
        
        # #calculando el tiempo total empleado hasta hora en todas las sessiones
        overall_hours += hours
        overall_minutes += minutes
        overall_seconds += seconds
        overall_time=f"\n***Total Report: {abs((overall_hours))} h, {abs((overall_minutes))} min, {abs((overall_seconds))} s\n \n"     
        
        #muestro el tiempo total empleado en la tarea al usuario en el widget "duration_report"
        duration_report.insert(INSERT, total_time)
        duration_report.insert(INSERT, overall_time)
    
    else:
        messagebox.showerror("showerror", "Start a project first") 
        
#TODO: FUNCION QUE RESETEA EL TEXTO WIDGET COMO LOS TIEMPOS
def reset():
    global overall_hours
    global overall_minutes
    global overall_seconds
    
    # Resetea las variables globales a cero, Estas variables almacenan el tiempo total transcurrido
    overall_hours = 0
    overall_minutes = 0
    overall_seconds = 0

    # Borra todo el contenido del widget 'duration_report', '1.0' indica el inicio del texto y 'end' indica el final del texto
    duration_report.delete("1.0", "end")
    
    
#TODO: FUNCION QUE EXPORTA LA INFORMACION DEL   TEXTO WIDGER A .TXT FILE
def export():

    # Abre un cuadro de diálogo para guardar un archivo con la extensión predeterminada '.txt'
    file=asksaveasfile(defaultextension='.txt')

    
    # Obtiene el contenido del widget 'duration_report' desde el inicio ('1.0') hasta el final ('end')
    text_widget_data=duration_report.get("1.0", "end")
    file.write(text_widget_data)

    
#TODO: TITULO DE LA APP, BOTON AGREGAR TAREA, LISTA DE TAREAS, BOTON DE "PLAY"
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


#TODO: CREANDO FRAME PARA PONER LOS BOTONES INFERIOES
bottom_buttons_frame=Frame(window, bg=BEIGE)
# 'ew' hace que el frame se expanda horizontalmente, el widget se adhiere a los lados este y oeste de la celda.
bottom_buttons_frame.grid(row=3, column=0, sticky='ew', columnspan=4, pady=5)

#empaquetamos los botones inferioes en el frame botton_buttons_frame

#boton de play
play_button=Button(bottom_buttons_frame, text="Play", bg="white", relief=GROOVE, command=start_time)
play_button.grid(row=0, column=0, padx=30, pady=5)
# play_button.pack()

#boton de "ver informe de duracion"
stop_button=Button(bottom_buttons_frame, text="Stop Project", bg="white", relief=GROOVE, command=stop)
stop_button.grid(row=0, column=2, padx=30, pady=5)

#boton de resetar la informacion del 'text widget'

reset_button=Button(bottom_buttons_frame, text="Reset", bg=ORANGE, relief=GROOVE, command=reset)

reset_button=Button(bottom_buttons_frame, text="Reset", bg="white", relief=GROOVE, command=reset)

reset_button.grid(row=0, column=3, padx=30, pady=5)


#boton de exportar la informacion del 'text widget' a tipo .TXT file
export_information=Button(bottom_buttons_frame, text="Export information", bg="white", relief=GROOVE, command=export)
export_information.grid(row=0, column=4, padx=30, pady=5)

#TODO: CREANDO TEXT WIDGET PARA MOSTRAR INFORMACION AL USER DEL TIEMPO DE DURACION DE CADA TAREA
duration_report=Text(window, bg=PEACH, width=50,height=20, font=("Arial", 13))
duration_report.grid(row=2, column=1, padx=15)
                        
                        




window.mainloop()