quant_km = float(input("Digite quanto km foi percorrido: "))
dias = int(input("Quantos dias foi alugado o carro: "))
preco_dia = 60
preco_km = 0.15
preco_pago_dias = (dias * preco_dia)
preco_pago_km = (quant_km * preco_km)
preco_final = (dias * preco_dia) + (preco_km * quant_km)

print(f"O valor em dias são {preco_pago_dias}")
print(f"O valor em km rodado é {preco_pago_km}")
print(f"O preço final a sere pago é de {preco_final}")
