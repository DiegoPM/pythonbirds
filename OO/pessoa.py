class Pessoa:
    def __init__(self, nome = None, idade=32):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f"Olá {id(self)}"
if __name__ == '__main__':
    p = Pessoa("Cleber")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "Diego"
    print(p.nome)
