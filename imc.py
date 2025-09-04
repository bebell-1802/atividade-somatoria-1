
peso = float(input("qual seu peso?"))

altura = float(input("qual sua altura?"))

imc = peso / (altura ** 2)
print(f"seu imc é: {imc: .2f}")

if imc < 18.5:
    print("Abaixo do peso, cuidado pro vento não te levar🍃")
elif 18.5 <= imc <= 24.9:
    print("peso normal, parabéns🎉")
elif 25.0 <= imc <= 29.9:
    print("sobrepeso")
elif 30.0 <= imc <= 34.4:
    print("Obesidade Grau I, tá precisando emagracer")
elif 35.0 <= imc <= 39.9:
    print("Obesidade Grau II, meu Deus...")
elif imc <= 40.0:
    print("Obesidade Grau III (mórbida), já tem a comida de um ano inteiro na sua barriga😕")






