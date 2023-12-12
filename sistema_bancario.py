class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.saques_realizados = 0
        self.saques_disponiveis = 3

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')

    def saque(self, valor):
        if self.saques_realizados < self.saques_disponiveis:
            if valor <= 500 and valor > 0 and self.saldo >= valor:
                self.saldo -= valor
                self.saques_realizados += 1
                print(f'Saque de R${valor} realizado com sucesso.')
            else:
                print('Valor de saque inválido ou saldo insuficiente.')
        else:
            print('Limite de saques diários atingido.')

    def extrato(self):
        print(f'Seu saldo atual é de R${self.saldo}')

def main():
    banco = SistemaBancario()

    while True:
        print("\n### MENU ###")
        print("1. Visualizar extrato")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            banco.extrato()
        elif opcao == '2':
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            banco.deposito(valor_deposito)
        elif opcao == '3':
            valor_saque = float(input("Digite o valor a ser sacado: "))
            banco.saque(valor_saque)
        elif opcao == '4':
            print("Saindo do sistema bancário. Até logo!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
