""" A resolver el reto!
Vamos a prodecer a crear una lista de diccionarios, 
esto es, un directorio de estudiantes de SKILLS FOR WOMEN IN TECH 
que participarán en una edición en línea.

Cada estudiante debe tener los siguientes atributos:

Nombre
Edad
Temas
Menores de edad
Puedes asignar los datos a mano o utilizar funciones aleatorias para llenar los campos."""


#datos de los alumno

alumno1 = ['Juana Perez', 19, "matematicas", False ]
alumno2 = ["Mariela Romero", 31, "física", False]
alumno3 = ["Rosa Juarez", 17, "Geografía", True]
alumno4 = ["Tania López", 15, "Biología",True]
alumno5 = ["Tatiana Castro", 25, "Ciencia de datos",False]
alumno6 = ["Montserrat Hernández", 35, "Mercadotecnia",False]
alumno7 = ["Danna Hernández", 16, "Circuitos",True]


directorioDeAlumnos = [ alumno1 ,   alumno2 ,  alumno3,  alumno4, alumno5, alumno6, alumno7]

print(directorioDeAlumnos)

import pandas as pd
pd.DataFrame(directorioDeAlumnos, columns=['Nombre de la alumna', 'Edad', 'Asignatura', 'es_menor'])