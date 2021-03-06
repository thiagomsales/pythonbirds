class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá{id(self)}'

    @staticmethod
    def metodo_estatico ():
        return 42
    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
     thiago = Mutante(nome='Sales')
     rogerio = Homem(thiago, nome='Falcao')
     print(Pessoa.cumprimentar(rogerio))
     print(id(rogerio))
     print(rogerio.cumprimentar())
     print(rogerio.nome)
     print(rogerio.idade)
     for filho in rogerio.filhos:
        print(filho.nome)
     rogerio.sobrenome = 'Sales'
     print(rogerio.__dict__)
     print(thiago.__dict__)
     print(Pessoa.olhos)
     print(rogerio.olhos)
     print(thiago.olhos)
     print(id(Pessoa.olhos), id(rogerio.olhos), id(thiago.olhos))
     print(Pessoa.metodo_estatico(), rogerio.metodo_estatico())
     print(Pessoa.nome_e_atributos_de_classes(), rogerio.nome_e_atributos_de_classes())
     pessoa=Pessoa('Anonimo')
     print(isinstance(pessoa, Pessoa))
     print(isinstance(pessoa, Homem))
     print(isinstance(thiago.olhos))







