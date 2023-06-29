def coloreo_grafo_mayor():
    print("Coloreo de Grafos: Metodo de mayor a menor volumen")
    #Se importan las librerias
    import random
    import time
    inicio = time.time()
    #Delimita cantidad de equipos(nodos) y colores maximos, por cada elemento de la lista
    cantidad = int(input("Ingrese la cantidad de nodos a generar: "))
    elementos = []

    for i in range(cantidad):
        elemento = str(i + 1)
        elementos.append(elemento)
    colores = ["Verde","Rojo","Azul"]
    #A partir del tamaño de la lista equipos se crea un valor numero
    maximo_nodos=(len(elementos))
    #Se define el diccionario nodos donde cada elemento(nombre, volumen,color) es una lista del tamaño del maximo de nodos
    nodos=dict(nombre=list(("X"*maximo_nodos)),volumen=list(("0"*maximo_nodos)),color=list(("sincolor"*maximo_nodos)))
    #Se define el maximo y minimo volumen (Aristas relacionadas) de un nodo 
    maximo_volumen=5
    minimo_volumen=2
    #Obtiene el tiempo de ejecucion en segundos diviendo el time.time por 10^9, y redondeando el resultado a 2 decimales
    segundos= round(((time.time())/10**9),2)
    #Ciclo que parte del cero al maximo de nodos-1
    for a in range(0,maximo_nodos):
            #Se reasigna un valor aleatorio a cada elemento del diccionario nodos.volumen, del minimo al maximo, los valores pueden repetirse
            nodos["volumen"][a]=random.randrange(minimo_volumen,(maximo_volumen+1))
    #Se ordena de mayor a menor cada volumen asignado
    ordenados=sorted(nodos["volumen"],reverse=True)    
    #Ciclo que recorre cada volumen ordenado, usando la variable c que empieza en 0 como punto de control
    c=0
    for b in ordenados:
            #Se reasigna el valor del elemento c de nodos.volumen al valor del volumen actual
            nodos["volumen"][c]=b
            #Se le da el nombre al nodo C de tal forma que el primer equipo siempre sera el Source y el ultimo equipo sera el Summit
            nodos["nombre"][c]=elementos[c]
            #Se la asigna un color al nodo C, usando el metodo random
            nodos["color"][c]=colores[random.randrange(0,len(colores))]
            #En caso de que el nodo anterior tenga el mismo color que el nodo actual, se repite el proceso
            while nodos["color"][c]==nodos["color"][(c-1)] or nodos["color"][c]==nodos["color"][(c+1)]:
                #Esto evita que se muestren dos nodos subsecuentes de un mismo color
                nodos["color"][c]=colores[random.randrange(0,len(colores))]
            #Imprime los datos del nodo actual, es decir, su nombre, color y volumen
            print("Nombre del nodo: "+nodos["nombre"][c]+" Color: "+nodos["color"][c]+" Volumen: "+str(nodos["volumen"][c]))
            #Aumenta la variable c en 1 para continuar con el nodo siguiente
            c=c+1
    fin = time.time()
    print(fin-inicio)
    return
coloreo_grafo_mayor()