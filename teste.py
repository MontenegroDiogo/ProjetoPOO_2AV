# # Classe base Pessoa
# class Pessoa:
#     def __init__(self, nome, idade, cpf, endereco):
#         self.nome = nome
#         self.idade = idade
#         self._cpf = cpf  # CPF encapsulado
#         self.endereco = endereco

#     @property
#     def cpf(self):
#         return self._cpf

# # Classe Paciente herda de Pessoa


# class Paciente(Pessoa):
#     def __init__(self, nome, idade, cpf, historico, endereco):
#         super().__init__(nome, idade, cpf, endereco)
#         self._historico = historico  # Histórico encapsulado
#         self.prontuarios = []  # Lista de prontuários

#     def adicionar_prontuario(self, prontuario):
#         self.prontuarios.append(prontuario)

#     @property
#     def historico(self):
#         return self._historico

# # Classe Medico herda de Pessoa


# class Medico(Pessoa):
#     def __init__(self, nome, idade, cpf, especialidade, endereco):
#         super().__init__(nome, idade, cpf, endereco)
#         self.especialidade = especialidade

# # Classe Consulta


# class Consulta:
#     def __init__(self, paciente, medico, data, observacao):
#         self.paciente = paciente
#         self.medico = medico
#         self.data = data
#         self.observacao = observacao

# # Classe Prontuario


# class Prontuario:
#     def __init__(self, consulta, diagnostico):
#         self.consulta = consulta
#         self._diagnostico = diagnostico  # Diagnóstico encapsulado

#     def adicionar_observacao(self, observacao):
#         self.consulta.observacao = observacao

#     @property
#     def diagnostico(self):
#         return self._diagnostico

# # --- Exemplo de uso ---


# # Criando um paciente
# paciente1 = Paciente("João da Silva", 30, "123.456.789-00",
#                      "Histórico de hipertensão", "Rua A, 123")
# print(f"Paciente: {paciente1.nome}, Idade: {paciente1.idade}, CPF: {
#       paciente1.cpf}, Histórico: {paciente1.historico}")

# # Criando um médico
# medico1 = Medico("Dra. Maria", 45, "987.654.321-00",
#                  "Cardiologista", "Rua B, 456")
# print(f"Médico: {medico1.nome}, Especialidade: {medico1.especialidade}")

# # Agendando uma consulta
# consulta1 = Consulta(paciente1, medico1, "2024-11-05",
#                      "Paciente relatou dores no peito.")
# print(f"Consulta: {consulta1.data}, Paciente: {consulta1.paciente.nome}, Médico: {
#       consulta1.medico.nome}, Observação: {consulta1.observacao}")

# # Criando um prontuário para a consulta
# prontuario1 = Prontuario(consulta1, "Diagnóstico: Hipertensão controlada.")
# paciente1.adicionar_prontuario(prontuario1)
# print(f"Prontuário adicionado. Diagnóstico: {prontuario1.diagnostico}")

# # Adicionando uma observação no prontuário
# prontuario1.adicionar_observacao(
#     "Paciente deverá retornar em 6 meses para nova avaliação.")
# print(f"Observação atualizada: {consulta1.observacao}")
