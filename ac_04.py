# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1: Raphael Sousa Silva      RA:1904217
# ALUNO 2: Diego Junior Gomes       RA:1904172
# ALUNO 3: Bruno Loures M. De Souza RA:1904113

from abc import ABC


class Pessoa(ABC):
    def __init__(self, cpf, rg,  nome, telefone):
        self.__cpf = cpf
        self.__rg = rg
        self.nome = nome
        self.telefone = telefone

    def get_rg(self):
        return self.__rg

    def get_cpf(self):
        return self.__cpf


class Medico(Pessoa):
    def __init__(self, crm, cpf, rg, nome, telefone, salario):
        super().__init__(cpf, rg, nome, telefone)
        self.__crm = crm
        self.salario = salario
        self.especialidade = None

    def get_crm(self):
        return self.__crm

    def set_especialidade(self, especialidade):
        self.especialidade = especialidade


class Paciente(Pessoa):
    def __init__(self, nome, rg, cpf, endereco, telefone, nascimento, medico):
        super().__init__(cpf, rg, nome, telefone)
        self.__endereco = endereco
        self.nascimento = nascimento
        self.medico_responsavel = medico
        self.quarto = None
        self.historico = None

    def get_endereco(self):
        return self.__endereco

    def set_historico(self, historico):
        self.historico = historico


class Quarto:
    def __init__(self, andar, numero):
        self.andar = andar
        self.numero = numero

    def exibir_quarto(self):
        print("Quarto:", self.numero)
        print("Andar:", self.andar)


class Historico:
    def __init__(self):
        self.data = None
        self.horario = None
        self.medico = None
        self.observacao = None

    def set_observacoes(self, data, horario, observacao, medico):
        self.data = data
        self.horario = horario
        self.observacao = observacao
        self.medico = medico

    def exibir_observacoes(self):
        print("Data:", self.data)
        print("Horario:", self.horario)
        print("Observação:", self.observacao)
        print("Medico:", self.medico.nome)


medico_1 = Medico('135678', '275.290.310-01', '9752417-5',
                  'Raphael Sousa', '96378-4153', 8500)
medico_1.set_especialidade('Neurologista')
print("Nome médico:", medico_1.nome)
print("Rg medico:", medico_1.get_rg())
print("Cpf medico:", medico_1.get_cpf())
print("Telefone:", medico_1.telefone)
print("CRM:", medico_1.get_crm())
print("Salário:", medico_1.salario)
print("Especialidade:", medico_1.especialidade)
print("---------------------------------")


paciente_1 = Paciente('Bruno Loures', '15276-5', '185.220.345-77',
                      'Rua São Carlos, 214', '97521-8890', '12/12/1990',
                      medico_1)
print("Paciente:", paciente_1.nome)
print("Medico responsavel:", paciente_1.medico_responsavel.nome)
print("Rg paciente:", paciente_1.get_rg())
print("Cpf paciente:", paciente_1.get_cpf())
print("Endereço:", paciente_1.get_endereco())
print("---------------------------------")


quarto_1 = Quarto(20, "2° Andar")
quarto_1.exibir_quarto()
print("---------------------------------")


historico_1 = Historico()
historico_1.set_observacoes('15/10/2020', '12:33',
                            'Paciente necessita de novos exames', medico_1)
historico_1.exibir_observacoes()
paciente_1.set_historico(historico_1)
