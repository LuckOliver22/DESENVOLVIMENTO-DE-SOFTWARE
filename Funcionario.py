class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        return f"{self.__class__.__name__} - Nome: {self.nome}, Matrícula: {self.matricula}, Salário: R${self.calcular_salario():.2f}"


class Administrativo(Funcionario):
    def __init__(self, nome, matricula, salario_base, adicional_insalubridade=0):
        super().__init__(nome, matricula, salario_base)
        self.adicional_insalubridade = adicional_insalubridade

    def calcular_salario(self):
        return self.salario_base + self.adicional_insalubridade


class Professor(Funcionario):
    def __init__(self, nome, matricula, salario_base, horas_aula, valor_hora):
        super().__init__(nome, matricula, salario_base)
        self.horas_aula = horas_aula
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.salario_base + (self.horas_aula * self.valor_hora)


class Tecnico(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus=0):
        super().__init__(nome, matricula, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus


# --- Testando o sistema ---
if __name__ == "__main__":
    funcionarios = []

    funcionarios.append(Administrativo("Maria", "A001", 3000, adicional_insalubridade=500))
    funcionarios.append(Professor("João", "P101", 2500, horas_aula=20, valor_hora=100))
    funcionarios.append(Tecnico("Ana", "T202", 2800, bonus=700))

    for f in funcionarios:
        print(f)