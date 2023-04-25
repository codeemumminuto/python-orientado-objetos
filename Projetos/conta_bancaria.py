# Projeto de conta bancária
# Atributos: nome, saldo
# Métodos: Mostrar saldo, sacar, depositar

# Adicionem novas funções:
# 1. histórico de despósito e saque
# 2. Taxas para saque
# 3. Limite o saque após sacar o valor X
# 4. Transferencia entre contas!!!

class ContaBancaria:
    def __init__(self, nome_titular, saldo_inicial):
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo}")

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        print(f"Valor R$ {valor_deposito} foi depositado!")
        self.exibir_saldo()

    def sacar(self, valor_saque):
        if valor_saque > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor_saque
            print(f"Valor R$ {valor_saque} foi sacado!")
            self.exibir_saldo()


conta1 = ContaBancaria("José", 50)
conta1.depositar(50)

conta1.sacar(30)