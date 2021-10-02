 class Pessoa:
    def _init_(self,nome,idade,endereço):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço

from Pessoa import Pessoa
class Amigos(Pessoa):
    def _init_(self, nome, idade, endereço):
        super()._init_(nome, idade, endereço)
        self.pontos = 15

from Pessoa import Pessoa
class Familia(Pessoa):
    def _init_(self, nome, idade, endereço):
        super()._init_(nome, idade, endereço)
        self.pontos = 20

from Pessoa import Pessoa
class Guia(Pessoa):
    def _init_(self, nome, idade, endereço,valor_medio):
        super()._init_(nome, idade, endereço)
        self.valor_medio = valor_medio

class Trilha:
    def _init_(self,integrantes,distancia_total,Grau_dificuldade,nome,localizacao,pontuacao_total,guia=None):
        self.integrantes = integrantes
        self.distancia_total = distancia_total
        self.Grau_dificuldade = Grau_dificuldade
        self.nome = nome
        self.localizacao = localizacao
        self.guia = guia
        self.pontuacao_total = pontuacao_total
    
    
    def adicionar_integrantes(self,* novo_integrante):
        for pessoa in novo_integrante:
            self.integrantes.append(pessoa)
    
    def gameficar(self):
        if len (self.integrantes) >= 10:
            for pessoa in self.integrantes:
                pessoa.pontos -= 10
    
        if self.guia != None:
            for pessoa in self.integrantes:
                pessoa.pontos -= 5
    
        for pessoa in self.integrantes:
            if pessoa.idade < 18:
                pessoa.pontos += 10
        x = 0
        for pessoa in self.integrantes:
            x += pessoa.pontos          
        self.pontuacao_total = x
        

from AMIGOS import Amigos
from FAMILIA import Familia
from GUIA import Guia
from TRILHA import Trilha

amigo = Amigos('Ludmila',46,'Pituba')
amigo1 = Amigos('Marcos',22,'Barra')
amigo2 = Amigos('Felipe',20,'lapa')
amigo3 = Amigos('José',45,'CaBulaIv')
amigo4 = Amigos('Marina',20,'itaigara')
familia = Familia('Lucas',37,'Avenida 7')
familia1 = Familia('Beth',30,'Ribeira')
familia2 = Familia('Julia',18,'Rio Vermelho')
familia3 = Familia('Luana',21,'Amaralina')
familia4 = Familia('Rose',45,'Ondina')

guia1 = Guia('Lucas',37,'AV7',30)
trilha1 = Trilha([],20,'Fácil','Vale do Capão','Capão',guia1)
trilha1.adicionar_integrantes(amigo,amigo1,amigo2,amigo3,amigo4,familia,familia1,familia2,familia3,familia4)
trilha1.gameficar()

print(trilha1.pontuacao_total)
