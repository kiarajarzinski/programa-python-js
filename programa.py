
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

