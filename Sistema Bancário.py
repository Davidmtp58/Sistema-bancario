menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0.0
depositos = []
saques = []
saques_diarios = 0

def depositar(valor):
    global saldo, depositos
    if valor > 0:
        saldo += valor
        depositos.append(valor)
    else:
        print("Valor de depósito inválido")

def sacar(valor):
    global saldo, saques, saques_diarios
    if saques_diarios < 3 and valor <= 500.0 and valor <= saldo:
        saldo -= valor
        saques.append(valor)
        saques_diarios += 1
    else:
        print("Não é possível realizar o saque")

def extrato():
    global depositos, saques, saldo
    if not depositos and not saques:
        print("Nenhuma transação foi realizada")
    else:
        print("Depósitos:")
        for deposito in depositos:
            print("R$%.2f" % deposito)
        print("Saques:")
        for saque in saques:
            print("R$%.2f" % saque)
        print("Saldo atual: R$%.2f" % saldo)

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
    elif opcao == "3":
        extrato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida")