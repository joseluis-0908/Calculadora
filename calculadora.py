print("calculadora con una sola variable \n ")

print("***********************")
print("Menu de opciones ")
print("***********************")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. Divición")
print("5. Division Entera")
print("6. Exponente")
print("7. Modulo o Resto \n")

numero=int(input("introduce la Opcion deseada: "))
if numero==1:
    print("elejiste la suma \n")
    numero = int(input("Introduce el primer numero: "))
    numero += int(input("introduce el segundo numero: "))
    print("El resultado es",numero)

elif numero==2:
    print("elejiste la resta \n")
    numero = int(input("Introduce el primer numero: "))
    numero -= int(input("introduce el segundo numero: "))
    print("El resultado es",numero)
   
elif numero==3:
    print("elegiste la multiplicacion ")
    numero = int(input("Introduce el primer numero: "))
    numero *= int(input("introduce el segundo numero: "))
    print("El resultado es",numero)
    
elif numero==4:
    print("elegiste la divicion \n")
    numero = float(input("Introduce el primer numero: "))
    numero /= float(input("introduce el segundo numero:"))
    print("El resultado es",round(numero,2))

    
elif numero==5:
    print("elegiste la division enterea \n")
    numero = int(input("Introduce el primer numero: "))
    numero //= int(input("introduce el segundo numero: "))
    print("El resultado es",numero)

    
elif numero==6:
    print("elegiste el Exponente \n")
    numero = int(input("Introduce el primer numero: "))
    numero **= int(input("introduce el segundo numero: "))
    print("El resultado es",numero)

      
elif numero==7:
    print("elegiste el Modulo O Resto")
    numero = int(input("Introduce el primer numero: "))
    numero %= int(input("introduce el segundo numero: "))
    print("El resultado es",numero)

   
else:
    print("La Opcion no existe \n")




