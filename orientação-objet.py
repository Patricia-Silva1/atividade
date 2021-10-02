
class Computador:    
    def __init__(self,modelo,fabricante,processador,ram,tamanho_hd,espaco_ocupado_hd):                
        self.modelo = modelo                
        self.fabricante = fabricante                
        self.processador = processador                 
        self.ram = ram               
        self.tamanho_hd = tamanho_hd               
        self.espaco_ocupado_hd = espaco_ocupado_hd                
        self.ligado = False                
    def ligar(self):                
        self.ligado = True                            
    def desligar(self):                
       self.ligado = False                            
    def limpar_hd(self,liberar):               
       if self.ligado == True:                        
        if liberar <= self.espaco_ocupado_hd:               
          self.espaco_ocupado_hd -= liberar                                                                                           
    def ocupar_hd(self,ocupar):                
     if self.ligado == True:                      
      if ocupar <= self.tamanho_hd:               
       self.espaco_ocupado_hd += ocupar                                                            
     Hp=Computador('hp','Lenovo','17',2,300,0)
     Hp.ligar()
     print(Hp.ligado)
     Hp.ocupar_hd(300)
     print(Hp.espaco_ocupado_hd)
     Hp.limpar_hd(200)
     print(Hp.espaco_ocupado_hd)                                                                   


