class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
     thiago = Pessoa(nome='Sales')
     rogerio = Pessoa(thiago, nome='Falcao')
     print(Pessoa.cumprimentar(rogerio))
     print(id(rogerio))
     print(rogerio.cumprimentar())
     print(rogerio.nome)
     print(rogerio.idade)
     for filho in rogerio.filhos:
        print(filho.nome)

