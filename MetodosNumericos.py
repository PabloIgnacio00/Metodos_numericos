num = 10 #numero de datos que arroja
while True:
    print(" __  __      _            _                                             _               ")    
    print("|  \/  | ___| |_ ___   __| | ___  ___   _ __  _   _ _ __ ___   ___ _ __(_) ___ ___  ___ ")
    print("| |\/| |/ _ \ __/ _ \ / _` |/ _ \/ __| | '_ \| | | | '_ ` _ \ / _ \ '__| |/ __/ _ \/ __|")
    print("| |  | |  __/ || (_) | (_| | (_) \__ \ | | | | |_| | | | | | |  __/ |  | | (_| (_) \__ )")
    print("|_|  |_|\___|\__\___/ \__,_|\___/|___/ |_| |_|\__,_|_| |_| |_|\___|_|  |_|\___\___/|___/")
    print(" ")    
    print("1. EULER")
    print("2. IMPROVED EULER")
    print("3. Runge Kutta 4th Order")
    print("4. Adams-Bashforth-Moulton")
    print("5. Manual de Sintaxis para funciones") 
    print("6. Cambiar número de datos que arroja. Actual-> "+str(num))
    print("7. Salir")
    opcion = int(input())
    import math
    if (opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4):
        fun = input("Ingrese su funcion: dy/dx = : \n")
        x_init = float(input("Ingrese el valor inicial de x: \n"))
        y_init = float(input("Ingrese el valor de y cuando x vale "+str(x_init)+": \n"))
        h = float(input("Ingrese el paso h: \n"))
        
        valores = [x_init,y_init]
        x_next = x_init # x + h 
        resultado = [y_init] #LISTA CON LOS VALORES DE Yi
    
    def evaluar(funcion_copia): #EVALUAR LA FUNCION EN (Xi, Yi) # K1
        for x in range(2):
            try: prueba = int(funcion_copia[abs(funcion_copia.index(str(chr(x+120)))-1)])
            except: prueba = str
            if type(prueba) == int: funcion_copia = funcion_copia.replace(str(chr(x+120)),("*"+str((valores[len(valores) -2+x]))),1)
            else: funcion_copia = funcion_copia.replace(str(chr(x+120)),(str((valores[len(valores) -2+x]))),1)
        try: return (eval(funcion_copia))
        except: print("Su funcion no puede ser evaluada. Chéquela, pana")
        
    def evaluarNext(funcion_copia,x_next, Yi, Y_0): #EVALUAR LA FUNCION EN (Xi+1, Yi+1)
        y = Y_0 + h*(Yi)
        nums = [x_next, y]
        for x in range(2):
            try: prueba = int(funcion_copia[abs(funcion_copia.index(str(chr(x+120)))-1)])
            except: prueba = str
            if type(prueba) == int: funcion_copia = funcion_copia.replace(str(chr(x+120)),("*"+str((nums[x]))),1)
            else: funcion_copia = funcion_copia.replace(str(chr(x+120)),(str(nums[x])),1)
        try: return (eval(funcion_copia))
        except: print("Su funcion no puede ser evaluada. Chéquela, pana")
    
    def rungeMiddle(funcion_copia,k): # K2 y K3
        #print(type(k),type(h))
        y = valores[len(valores) -1] + 0.5*h*k
        x_runge = valores[len(valores) -2] + 0.5*h
        nums2 = [x_runge,y]
        for x in range(2):
            try: prueba = int(funcion_copia[abs(funcion_copia.index(str(chr(x+120)))-1)])
            except: prueba = str
            if type(prueba) == int: funcion_copia = funcion_copia.replace(str(chr(x+120)),("*"+str(nums2[x])),1)
            else: funcion_copia = funcion_copia.replace(str(chr(x+120)),(str((nums2[x]))),1)
        try: return (eval(funcion_copia))
        except: print("Su funcion no puede ser evaluada. Chéquela, pana")
        
    def rungeK4(funcion_copia,k):
        y = valores[len(valores) -1] + h*k
        x_runge = valores[len(valores) -2] + h
        nums3 = [x_runge,y]
        for x in range(2):
            try: prueba = int(funcion_copia[abs(funcion_copia.index(str(chr(x+120)))-1)])
            except: prueba = str
            if type(prueba) == int: funcion_copia = funcion_copia.replace(str(chr(x+120)),("*"+str(nums3[x])),1)
            else: funcion_copia = funcion_copia.replace(str(chr(x+120)),(str((nums3[x]))),1)
        try: return (eval(funcion_copia))
        except: print("Su funcion no puede ser evaluada. Chéquela, pana")
    def evaluarParametros(funcion_copia, x, y):
        nums4 = [x,y]
        for x in range(2):
            try: prueba = int(funcion_copia[abs(funcion_copia.index(str(chr(x+120)))-1)])
            except: prueba = str
            if type(prueba) == int: funcion_copia = funcion_copia.replace(str(chr(x+120)),("*"+str((nums4[x]))),1)
            else: funcion_copia = funcion_copia.replace(str(chr(x+120)),(str((nums4[x]))),1)
        try: return (eval(funcion_copia))
        except: print("Su funcion no puede ser evaluada. Chéquela, pana")
        
    if opcion == 1:  #EULER
        print(" Xn -   Yn")
        for i in range(num):
            x_next += h
            y_n = ((resultado[i]) + h*(evaluar(fun)))
            resultado.append(y_n)
            valores.append(x_next)
            valores.append(y_n)
            print(str(round(x_next,2)) +" - " +str(round(y_n,4)))
        
    elif opcion == 2:  #IMPROVED EULER
        print(" Xn -  Yn")
        for i in range(num):
            x_next += h
            Yi = evaluar(fun)
            Y_0 = resultado[i]
            y_n = ((Y_0) + (h/2)*((Yi)+evaluarNext(fun,x_next,Yi,Y_0)))
            resultado.append(y_n)
            valores.append(x_next)
            valores.append(y_n)
            print(str(round(x_next,2)) +" - " +str(round(y_n,4)))   
            
    elif opcion == 3: #RUNGE KUTTA 4th ORDER
        print(" Xn -  Yn")
        for i in range(num):
            x_next += h
            k_1 = evaluar(fun)
            Y_0 = resultado[i]
            k_2 = rungeMiddle(fun,k_1)
            k_3 = rungeMiddle(fun, k_2)
            k_4 = rungeK4(fun, k_3)
            y_n = resultado[i] + (h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
            resultado.append(y_n)
            valores.append(x_next)
            valores.append(y_n)
            print(str(round(x_next,2)) +" - " +str(round(y_n,4)))   
        
    elif opcion == 4:
        objetivo = float(input("Ingrese el valor de t que quiere obtener. Y(t) cuando t = "))
        Adam = [] 
    
        if(h-(objetivo % h) > 0.0000001 and h-(objetivo % h)< h):
            print("Ingrese un valor de t, que sea múltiplo de "+str(h))
            break
        
        if(objetivo == h*4):
            y_especial = evaluarParametros(fun, x_init, y_init)
            Adam.append(y_especial)
            print("entro")
            
        for i in range(int(objetivo/h)-1):
            x_next += h
            k_1 = evaluar(fun)
            Y_0 = resultado[i]
            k_2 = rungeMiddle(fun,k_1)
            k_3 = rungeMiddle(fun, k_2)
            k_4 = rungeK4(fun, k_3)
            y_n = resultado[i] + (h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
            y_n_prime = evaluarParametros(fun, x_next,y_n)
            Adam.append(y_n_prime)
            resultado.append(y_n)
            valores.append(x_next)
            valores.append(y_n)
            print(str(round(x_next,2)) +" - " +str(round(y_n,4)))   
        ultimo = len(Adam)
        cambio_y4 = (h/24)*(55*Adam[ultimo-1] - 59*Adam[ultimo-2] + 37*Adam[ultimo-3] - 9*Adam[ultimo -4])
        y4 =  valores[len(valores)-1] + cambio_y4
        y4_prime = evaluarParametros(fun, objetivo, y4)
        Adam.append(y4_prime)
        print(ultimo)
        cambio = (h/24)*(9*Adam[ultimo] + 19*Adam[ultimo-1] - 5*Adam[ultimo-2] +Adam[ultimo-3])
        respuesta = valores[len(valores)-1] + cambio
        print("Y("+str(objetivo)+") = "+str(respuesta))

        
    elif opcion == 5:
        print("-----------------------------------------------------------------------")
        print("Multiplicacion: xy -> x * y ,  4*(6x+7y) . No olvides poner el * siempre y cuando")
        print("sea una multiplicación de dos variables o factores.")
        print("Para coeficientes de una variable, no se debe poner '*', ejemplo:")
        print("2x + 3y -> 2x + 3y. NO se escribe con * (2*x + 3*y)")
        print("\nExponentes: y^2 se escribe como y**2. Se usa ** para indicar exponentes")
        print("\nFunciones trigonometricas: Sin -> math.sin(x), Cos -> math.cos(x).")
        print("\nEste programa es un programa para derivadas de primer orden")  
        print("No puedes incluir derivadas en la funcion")    
        print("EJEMPLOS:")        
        print("Para escribir\n sin(x^2)+cos(y^2) -> math.sin(x**2) + math.cos(y**2)")
        print ("x^2 + 2y + 8 -> (x**2) + 2y + 8")   
        print("----------------------------------------------------------------------")
    elif opcion == 6:
        print("Ingrese el número de datos que quiere arrojar. Actual-> "+str(num))
        num = int(input())
    elif opcion == 7:
        print("HASTA LA PROCSIMAAAAA")
        break
    else:
        print("Ingrese un valor válido")
