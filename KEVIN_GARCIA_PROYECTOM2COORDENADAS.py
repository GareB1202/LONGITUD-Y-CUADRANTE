X = float(input("Ingrese la coordenada x:"))
Y = float(input("Ingrese la coordenada de y:"))

if X >0 and Y >0:
    cuadrante = "Primer cuadrante"
elif X >0 and Y <0:
    cuadrante = "Segundo cuadrante"
elif X <0 and Y <0:
    cuadrante = "Tercer cuadrante"
elif X >0 and Y <0:
    cuadrante = "Cuarto cuadrante"
else:
    cuadrante = "origen"
print("El punto se encuentra en el", cuadrante)
    
