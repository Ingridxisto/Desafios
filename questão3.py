import json


with open('faturamento.json', 'r') as file:
    faturamento_diario = json.load(file)


def calcular_faturamento(dados):
    # Ignora dias sem faturamento (faturamento zero)
    valores = [valor for valor in dados["faturamento"] if valor > 0]
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media


menor, maior, dias_acima = calcular_faturamento(faturamento_diario)
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima}")
