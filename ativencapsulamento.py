from datetime import datetime

class Veiculo:
    def _init_(self, tipo, placa, modelo, dh_entrada):
        self.__tipo = tipo
        self.__placa = placa
        self.__modelo = modelo
        self.__dh_entrada = dh_entrada
      
    @property
    def tipo(self):
        return self.__tipo
    
    def valor_tipo(self):
        tipo_veiculo = None
        valor_hora = 0
        while tipo_veiculo == None:
            if self.__tipo == 1:
                # tipo = moto
                valor_hora = 1.5
                tipo_veiculo = "Moto"
                print("Tipo de veículo: \t", tipo_veiculo)
            elif self.__tipo == 2:
                # tipo = carro
                valor_hora = 2.5
                tipo_veiculo = "Carro"
                print("Tipo de veículo: \t", tipo_veiculo)
            elif self.__tipo == 3:
                # tipo = caminhão
                valor_hora = 5.0
                tipo_veiculo = "Caminhão"
                print("Tipo de veículo: \t", tipo_veiculo)
            else:
                # tipo indefinido
                print("Tipo de veículo não cadastrado!!!")
                self.__tipo = int(input("Escolha novamente: \t "))
        return valor_hora
    @property
    def dh_saida(self):
        return self.__dhsaida
    
    def informar_saida(self):
        permanencia = 0
        dh_saida = datetime.strptime('07/09/1900 00:00', FMT)
        while dh_saida < self.__dh_entrada:
            dh_saidatxt = input("Informe data/hora da saída - dd/mm/aaaa hh:mm -->  ")
            dh_saida = datetime.strptime(dh_saidatxt, FMT)
            if dh_saida < self.__dh_entrada:
                print("Data/hora saida menor que data/hora de entrada!!")
        permanencia =  (dh_saida - self.__dh_entrada)
        valor_total = ((permanencia.days)*24+ceil(permanencia.seconds/3600))*self.valor_tipo()
        print()
        print("########  FECHAMENTO DE CONTA    ##############")
        print("Placa do veículo:\t", self.__placa)
        print(f'Valor da Hora: \t\t R$ {self.valor_tipo():,.2f}')
        print("Horário de entrada: \t", datetime.strftime(self.__dh_entrada,FMT))
        print("Horário de saída: \t", datetime.strftime(dh_saida,FMT)) 
        print()
        print ("O tempo total de permanencia foi de : ", permanencia)
        print ("e para efeito de cobrança, foi considerado o total de ", ((permanencia.days)*24+ceil(permanencia.seconds/3600)), " horas")
        print(f'O Valor total a pagar é de \t R$ {valor_total:,.2f}')
        print("######################   FIM DO RELATÓRIO    ######################")
        print()
        return permanencia, dh_saida
print()       
FMT = '%d/%m/%Y %H:%M'
entrada = input("Informe data/hora de entrada - dd/mm/aaaa hh:mm -->   ")
print("Escolha o tipo de veículo pelo número conforme abaixo")
print(" 1) Moto \n 2) Carro \n 3) Caminhão")
opcao = int(input("Escolha a opção: \t"))
  
veiculo1 = Veiculo(opcao,'AAA123','Corsa', datetime.strptime(entrada, FMT))
veiculo1.valor_tipo()
veiculo1.informar_saida()