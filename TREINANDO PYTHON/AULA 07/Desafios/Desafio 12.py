preco = float(input("Digite o preço para calcular o desconto: "))
desconto = (preco * 0.05)
preco_atual = (preco - desconto)

print(f"O preço atual é o que vale {preco_atual} reais, o desconto foi de {desconto} reais")