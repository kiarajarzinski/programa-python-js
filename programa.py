
personas = [] 

while ( True ): 
    nombre = input("Ingrese el nombre de la persona(o escriba 'finalizar' para terminar): ")
    if nombre == "finalizar":
        break 

    edad = int(input("ingrese la edad de la persona:"))    
    nota = float(input('ingrese la nota de la persona:'))

    lista = [ nombre, edad, nota]
    personas.append(lista)

    print (personas)

    lista_ordenada = sorted(personas, key=lambda posicion: posicion[2], reverse=True)

    print (lista_ordenada)

    suma_notas = 0 
    for posicion in lista_ordenada:
        suma_notas += posicion[2]

    promedio = suma_notas / len(lista_ordenada)
    
    print ( "El promedio de las notas es:", promedio)

