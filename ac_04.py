class Pessoa:
    def __init__(self, nome, rg, cpf, telefone):
        self.nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.telefone = telefone

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def set_rg(self):
        self.__rg = rg
        return self.__rg


class Medico(Pessoa):
    def __init__(self, nome, rg, cpf, telefone, crm, salario, especialidade):
        super().__init__(nome, rg, cpf, telefone)
        self.crm = crm
        self.salario = salario
        self.especialidade = especialidade


class Paciente(Pessoa):
    def __init__(self, nome, rg, cpf, telefone, endereco, nascimento):
        super().__init__(nome, rg, cpf, telefone)
        self.endereco = endereco
        self.nascimento = nascimento


class Especialidade:
    def __init__(self, especialidade):
        self.especialidade = especialidade


class Quarto:
    def __init__(self, numero, andar):
        self.numero = numero
        self.andar = andar
