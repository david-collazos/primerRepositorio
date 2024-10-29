# Función para calcular el IMC
def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc

# Ejemplo de uso
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# Calcula el IMC
imc = calcular_imc(peso, estatura)

# Muestra el resultado
print(f"Tu IMC es: {imc:.2f}")

# Opcional: clasificar el IMC según las categorías de la OMS
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Clasificación: Peso normal")
elif 25 <= imc < 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
