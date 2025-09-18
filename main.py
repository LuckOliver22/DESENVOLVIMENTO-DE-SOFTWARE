from datetime import date

class Transacao:
    def registrar(self, conta):
        raise NotImplementedError("Método deve ser implementado pelas subclasses.")

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(self)
            return True
        return False

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero: int, agencia: str = "0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @staticmethod
    def nova_conta(cliente, numero: int, agencia: str = "0001"):
        return Conta(cliente, numero, agencia)

    def sacar(self, valor: float) -> bool:
        saque = Saque(valor)
        return saque.registrar(self)

    def depositar(self, valor: float) -> bool:
        deposito = Deposito(valor)
        deposito.registrar(self)
        return True

class ContaCorrente(Conta):
    def __init__(self, cliente, numero: int, limite: float, limite_saques: int, agencia: str = "0001"):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor: float) -> bool:
        if valor > self.limite:
            return False
        if self.saques_realizados >= self.limite_saques:
            return False
        if super().sacar(valor):
            self.saques_realizados += 1
            return True
        return False

class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

if __name__ == "__main__":
    cliente = PessoaFisica("João Silva", "12345678900", date(1990, 5, 20), "Rua A, 123")
    conta = ContaCorrente(cliente, 1, 1000.0, 3)
    cliente.adicionar_conta(conta)
    conta.depositar(500)
    conta.sacar(200)
    print("Saldo:", conta.saldo)
    print("Transações realizadas:", len(conta.historico.transacoes))