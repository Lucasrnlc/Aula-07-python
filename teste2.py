valores = [20,71,100,30]

def dobrar (valor):
    resultado = valor * 2
    return resultado

print(dobrar(11))

valores_novos = []
for item  in valores:
    valores_novos.append(dobrar(item))
    print (valores_novos)