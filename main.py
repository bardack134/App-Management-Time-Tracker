from tkinter import *
#VARIABLES GLOBALES Y CONSTANTES
BEIGE="#FFF6E9"
BLUE="#40A2E3"
PURPLE="#AD88C6"

#TODO: CONFIGURACION DE LA VENTANA
window=Tk()

#titulo para la ventana
window.title('Time management')

#fondo de nuestra ventana
window.config(bg=BEIGE, padx=10, pady=10)



#TODO: titulo de la app, boton agregar tarea, lista de tareas, boton de "play"
#Titulo
# creamos un Frame con un color de fondo azul y lo expandimos para que ocupe toda la fila.
title_frame=Frame(window, bg=BLUE)

nb_of_columns = 2

# 'ew' hace que el frame se expanda horizontalmente, el widget se adhiere a los lados este y oeste de la celda.
title_frame.grid(row=0, column=0, sticky='ew', columnspan=nb_of_columns, padx=5, pady=5)

title=Label(title_frame, text="Projects", bg=BLUE, fg="white", font=("Arial", 10, "bold") )

title.pack(fill='both')

#boton de agregar tareas
add_task=Button(window, text="Add New Task", bg=PURPLE, fg="white", font=("Arial", 10, "bold"))
add_task.grid(row=1, column=1, pady=6, )

#Lista de tareas
task_list=Listbox()
task_list.insert(1, "example")
task_list.grid(row=2, column=1)




window.mainloop()