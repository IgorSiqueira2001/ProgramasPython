import json

def carregar_dados(arquivo):
    """Ler arquivo JSON e retorna uma lista de faturamentos."""
    with open(arquivo, 'r', encoding='utf-8') as file:
        return json.load(file)

def calcular_faturamento(dados):
    """Calcula menor e maior faturamento e quantos dias tiveram faturamento acima da media."""
    valores = [dia["valor"] for dia in dados if dia["valor"] > 0]

    if not valores:
        return "Nao ha dados suficientes para calculo."

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)

    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

########################################################################################################################
def inverter_string(palavra):
    string_invertida = ""
    for i in range(len(palavra) - 1, -1, -1):  # Começa do último caractere até o primeiro
        string_invertida += palavra[i]
    return string_invertida

########################################################################################################################
def fibonacci_sequence(limit):
    """Gerar sequencia de Fibonacci ate um determinado limite."""
    sequence = [0, 1]
    while sequence[-1] < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_fibonacci(num):
    """Verificar se numero pertence a sequencia de Fibonacci."""
    sequence = fibonacci_sequence(num)
    if num in sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."
########################################################################################################################
def executar_opcao(opcao):
    switch = {
        1: lambda: executar_programa_2(),
        2: lambda: executar_programa_3(),
        3: lambda: executar_programa_5(),
    }
    return switch.get(opcao, lambda: "Opção inválida.")()

def executar_programa_3():
    arquivo_json = "faturamento.json"
    dados_faturamento = carregar_dados(arquivo_json)

    resultado = calcular_faturamento(dados_faturamento)

    if isinstance(resultado, str):
        print(resultado)
    else:
        menor, maior, dias_acima_media = resultado
        print(f"Menor faturamento: R$ {menor:.2f}")
        print(f"Maior faturamento: R$ {maior:.2f}")
        print(f"Dias acima da média: {dias_acima_media}")

def executar_programa_2():
    try:
        numero = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))
        print(is_fibonacci(numero))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

def executar_programa_5():
    try:
        palavra = input("Digite uma string para inverter: ")
        resultado = inverter_string(palavra)
        print(resultado)
    except ValueError:
        print("Por favor, digite uma string válida.")

# Menu de opções
print("Escolha uma opção:")
print("Opção 1 - Programa 2 (Sequência de Fibonacci)")
print("Opção 2 - Programa 3 (Cálculo de faturamento)")
print("Opção 3 - Programa 5 (Inverter String)")

try:
    opcao = int(input("Digite sua opção: "))
    executar_opcao(opcao)
except ValueError:
    print("Por favor, digite um número válido para a opção.")
