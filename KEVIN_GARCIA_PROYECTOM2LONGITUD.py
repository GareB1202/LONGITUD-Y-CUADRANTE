palabra1 = input("Introduce la primera palabra:")
palabra2 = input("Introduce la segunda palabra:")
palabra3 = input("Introduce la tercera palabra:")

if len(palabra1) <2:
    palabra1 = "X" + palabra1

if len(palabra2) <2:
    palabra2 = "X" + palabra2
    
if len(palabra3) <2:
    palabra3 = "X" + palabra3
    
contrasena = palabra1 [0] + palabra2 [0] + palabra3 [0] + palabra1 [1] + palabra2 [1] + palabra3 [1]
print("Tu contrasena es:", contrasena)
  
contrasena_usuario = input("Introduce la contrasena: ")
if len(contrasena_usuario) < len(contrasena):
    print("Faltan", len(contrasena) - len(contrasena_usuario), "caracteres")
elif len(contrasena_usuario) > len(contrasena):
    print("Sobran", len(contrasena_usuario) - len(contrasena), "caracteres")
if contrasena_usuario == contrasena:
    print("Contrasena correcta")
else:
    print("Contrasena incorrecta") 
