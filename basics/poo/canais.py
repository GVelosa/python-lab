class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos

    def inscrever(self, quantidade=1):
        self.inscritos +=quantidade

canal_lancode = Canal("Lan Conde", "Canal de Programação", 34000)

print(f"Quantidade e inscritos: {canal_lancode.inscritos}")
canal_lancode.inscrever(10)
print(f"Nova quantide de inscritos: {canal_lancode.inscritos}")