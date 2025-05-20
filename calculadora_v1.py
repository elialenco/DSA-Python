# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("Bem-vindo(a) à Calculadora da Elise.")

# Operações válidas.
operacoes_validas = ['+', '-', '*', '/']

# Função para garantir que a operação seja válida.
def ler_operacao(mensagem):
    while True:
        operacao = input(mensagem)
        if operacao in operacoes_validas:
            return operacao
        else:
            print("Operação inválida. Escolha uma das opções válidas.")
        
# Função para garantir que o número seja válido.
def ler_numero(mensagem, permitir_zero=True):
    while True:
        try:
            numero = float(input(mensagem))
            if not permitir_zero and numero == 0:
                print("Valor inválido. O divisor não pode ser zero.")
                continue
            return numero
        except ValueError:
            print("Operação Inválida. Escreva um número.")

# Função de nova operação.
def nova_operacao():
    calc_nova_operacao = input("Deseja realizar uma nova operação? \
        Escolha S para sim e N para Não: ").strip().upper()
    if calc_nova_operacao == 'S':
        calcular()
    elif calc_nova_operacao == 'N':
        print("Obrigada por usar a calculadora. Até mais!")
    else:
        print("Opção inválida, tente novamente.")
        nova_operacao()

# Função do cálculo.
def calcular():
    operacao = ler_operacao(
    "Selecione uma operação:\n" 
    "+ para soma\n" 
    "- para subtração\n"
    "* para multiplicação\n" 
    "/ para divisão\n"
    "Escolha: "
    )

    num1 = ler_numero("Insira o primeiro número: ")

# Se divisão, não permitir que o segundo número seja zero.
    if operacao == '/':
        num2 = ler_numero("Insira o segundo número: ", permitir_zero=False)
    else:
        num2 = ler_numero("Insira o segundo número: ")

# Realizar operação.
    if operacao == '+':
        resultado = num1 + num2

    elif operacao == '-':
        resultado = num1 - num2

    elif operacao == '*':
        resultado = num1 * num2

    elif operacao == '/':
        resultado = num1 / num2

# Imprimir o resultado.
    print("O resultado de", num1, operacao, num2, \
"é igual a", resultado)

    nova_operacao()

#Chamar o programa. 
calcular()