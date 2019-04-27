class Bouncy():

    def calcularPorcentaje(self,porcentaje):
        porc = 0.0   
        numero =100
        abultados = 0
        totalNumeros = 99

        while porc < porcentaje:
            numeros = str(numero)
            creciente = True            
            for indice in range(len(numeros)-1):
                if int(numeros[indice]) > int(numeros[indice+1]):
                    creciente = False
                    break
            
            decreciente = True
            for indice in range(len(numeros)-1):
                if int(numeros[indice]) < int(numeros[indice+1]):
                    decreciente = False          
                    break
            
            if creciente == False and decreciente == False:
                abultados = abultados + 1
                porc = (abultados*100.0)/numero
            else:
                porc = 0.0

            if porc > 0:
                print (porc,'%','=====>','Cantidad abultados: ',abultados)     

            numero+=1
            totalNumeros += 1        

        print('*********RESULTADOS*********')
        print ('TOTAL NÚMEROS:',totalNumeros) 
        print ('Número Abultados',abultados)


    def calcularNumerosAbultados(self,numero,numeroFinal):
        porc = 0.0   
        abultados = 0
        totalNumeros = 99

        for i in range (numero, numeroFinal+1):
            numeros = str(numero)
            creciente = True            
            for indice in range(len(numeros)-1):
                if int(numeros[indice]) > int(numeros[indice+1]):
                    creciente = False
                    break
            
            decreciente = True
            for indice in range(len(numeros)-1):
                if int(numeros[indice]) < int(numeros[indice+1]):
                    decreciente = False          
                    break
            
            if creciente == False and decreciente == False:
                abultados = abultados + 1
                porc = (abultados*100.0)/numero
            else:
                porc = 0.0
            if porc > 0:    
                print (porc,'%','=====>','Cantidad abultados: ',abultados) 
            numero+=1
            totalNumeros += 1        

        print('*********RESULTADOS*********')
        print ('TOTAL NÚMEROS:',totalNumeros) 
        print ('Número Abultados',abultados)


ejercicio = Bouncy()
ejercicio.calcularPorcentaje(50)
ejercicio.calcularNumerosAbultados(100,538)