class Atletas:
    def _init_(self,nome,idade,pontuacao):
        self.nome = nome
        self.idade = idade
        self.pontuacao = pontuacao


class Amador(Atletas):
    def _init_(self, nome, idade, pontuacao):
        super()._init_(nome, idade, pontuacao)
        self.amador = True
        self.profissional = False
        self.lenda = False


class Profissional(Atletas):
    def _init_(self, nome, idade, pontuacao):
        super()._init_(nome, idade, pontuacao)
        self.amador = True
        self.profissional = True
        self.lenda = False



class Lenda(Atletas):
    def _init_(self, nome, idade, pontuacao):
        super()._init_(nome, idade, pontuacao)
        self.amador = True
        self.profissional = True
        self.lenda = True

class Patrocinadores:
    def _init_(self,nome,valor):
        self.nome = nome
        self.valor = valor

class Campeonato:
    def _init_(self,nome,local,premiacao,patrocinadores,atletas):
        self.nome = nome
        self.local = local
        self.premiacao = premiacao
        self.patrocinadores = patrocinadores
        self.atletas = atletas
        

    def adicionar_atletas(self,*novo_atleta):
        for atleta in novo_atleta:
            self.atletas.append(atleta)

    def adicionar_patrocinador(self,*novo_patrocionio):
        for empresa in novo_patrocionio:
            self.patrocinadores.append(empresa)

    def vencedor(self,nome_vencedor):
        for atleta in self.atletas:
            if nome_vencedor == atleta.nome:
                atleta.pontuacao += 0
        print('O atleta {} ficou com {} pontos'.format(nome_vencedor))



class CircuitoAmador(Campeonato):
    def _init_(self, nome, local, premiacao, patrocinadores, atletas):
        super()._init_(nome, local, premiacao, patrocinadores, atletas)

    
    def adicionar_patrocinador(self, *novo_patrocionio):
        return super().adicionar_patrocinador(*novo_patrocionio)

    def adicionar_atletas(self, *novo_atleta):
        return super().adicionar_atletas(*novo_atleta)

    def vencedor(self,nome_vencedor):
        for atleta in self.atletas:
            if nome_vencedor == atleta.nome:
                atleta.pontuacao += 10
                print('O atleta {} ficou com {} pontos'.format(nome_vencedor,atleta.pontuacao))



class CircuitoProfissional(Campeonato):
    def _init_(self, nome, local, premiacao, patrocinadores, atletas):
        super()._init_(nome, local, premiacao, patrocinadores, atletas)

    def adicionar_patrocinador(self, *novo_patrocionio):
        return super().adicionar_patrocinador(*novo_patrocionio)

    def adicionar_atletas(self, *novo_atleta):
        for atleta in novo_atleta:
            if atleta.profissional == True or atleta.lenda == True:
                self.atletas.append(atleta)
            else:
                return print('Está categoria não pode fazer parte deste circuito.')

    def vencedor(self,nome_vencedor):
        for atleta in self.atletas:
            if nome_vencedor == atleta.nome:
                atleta.pontuacao += 50
                print('O atleta {} ficou com {} pontos'.format(nome_vencedor,atleta.pontuacao))

     class CircuitoAmador(Campeonato):
    def _init_(self, nome, local, premiacao, patrocinadores, atletas):
        super()._init_(nome, local, premiacao, patrocinadores, atletas)

    
    def adicionar_patrocinador(self, *novo_patrocionio):
        return super().adicionar_patrocinador(*novo_patrocionio)

    def adicionar_atletas(self, *novo_atleta):
        return super().adicionar_atletas(*novo_atleta)

    def vencedor(self,nome_vencedor):
        for atleta in self.atletas:
            if nome_vencedor == atleta.nome:
                atleta.pontuacao += 10
                print('O atleta {} ficou com {} pontos'.format(nome_vencedor,atleta.pontuacao))



class CircuitoProfissional(Campeonato):
    def _init_(self, nome, local, premiacao, patrocinadores, atletas):
        super()._init_(nome, local, premiacao, patrocinadores, atletas)

    def adicionar_patrocinador(self, *novo_patrocionio):
        return super().adicionar_patrocinador(*novo_patrocionio)

    def adicionar_atletas(self, *novo_atleta):
        for atleta in novo_atleta:
            if atleta.profissional == True or atleta.lenda == True:
                self.atletas.append(atleta)
            else:
                return print('Está categoria não pode fazer parte deste circuito.')

    def vencedor(self,nome_vencedor):
        for atleta in self.atletas:
            if nome_vencedor == atleta.nome:
                atleta.pontuacao += 50
                print('O atleta {} ficou com {} pontos'.format(nome_vencedor,atleta.pontuacao))



class CircuitoLenda(Campeonato):
    def _init_(self, nome, local, premiacao, patrocinadores, atletas):
        super()._init_(nome, local, premiacao, patrocinadores, atletas)


    def adicionar_patrocinador(self, *novo_patrocionio):
        return super().adicionar_patrocinador(*novo_patrocionio)

    def adicionar_atletas(self, *novo_atleta):
        for atleta in novo_atleta:
            if atleta.lenda == True:
                self.atletas.append(atleta)
            else:
                return print('Está categoria não pode fazer parte deste circuito.')

    def vencedor(self,nome_vencedor):
        for atleta in self.atletas:
            if nome_vencedor == atleta.nome:
                atleta.pontuacao += 100
                print('O atleta {} ficou com {} pontos'.format(nome_vencedor,atleta.pontuacao))           
