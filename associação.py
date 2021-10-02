 def _init_(self, nome, cnpj, media_funcionarios, media_lucro):
        self.nome = nome
        self.cnpj = cnpj
        self.media_funcionarios = media_funcionarios
        self.media_lucro = media_lucro

class Prefeitura:
    def _init_(self, cidade, prefeito, empresas):
        self.cidade = cidade
        self.prefeito = prefeito
        self.empresas = empresas
    
    def calcular_impostos(self):
        total_impostos = 0
        total_lucro = 0
        qtde_empresas = 0
        for i in range(0,len(self.empresas)):
            total_lucro += self.empresas[i].media_lucro
            qtde_empresas += 1
        total_impostos = 1.6/100*total_lucro
        print()
        print('###  Resume de  Receita da  Preitura ##')
        print('Prefeitura de ', self.cidade, 'sob a administração do prefeito ', self.prefeito)
        print((f'O total de lucro apurado no mês foi de R$ {total_lucro: .2f}').replace('.',',').replace('','.'))
        print((f'O total de impostos recolhido no mês foi de R$ {total_impostos: .2f}').replace('.',',').replace('','.'))
        print('A quantidade de empresas a recolher imposto no mês é de : ', qtde_empresas)
        print('#### Fim do Relatorio  ######')
        print()
class Prefeito:
    def _init_(self, prefeito, cpf, formacao):
        self.prefeito = prefeito
        self.cpf = cpf
        self.formacao = formacao

# MAIN
mm = Empresa("cacau show", 42108, 170, 15000)
tpc = Empresa("TPC", 421054, 250, 30000)
kaiser = Empresa("Kaiser", 45874, 500, 80000)
nestle = Empresa("Nestle", 821054, 350, 55000)
servebem = Empresa("ServeBem", 821054, 350, 8000)
conti = Empresa("Continental", 854054, 1000, 150000)
empresas_ssa = [mm, tpc]
empresas_gbi = [kaiser, nestle, servebem]
empresas_vdc = [conti]
pref_ssa = Prefeito("Bruno Reis", 1234, "administração")
pref_gbi = Prefeito("Nilo Coelho", 4584, "contabilidade")
pref_vdc = Prefeito("Herzem Gusmão", 4584, "engenharia")
ssa = Prefeitura("Salvador", pref_ssa.prefeito, empresas_ssa)
gbi = Prefeitura("Guanambi", pref_gbi.prefeito, empresas_gbi)
vdc = Prefeitura("Vitoria da Conquista ", pref_vdc.prefeito, empresas_vdc)
ssa.calcular_impostos()
gbi.calcular_impostos()
vdc.calcular_impostos()

