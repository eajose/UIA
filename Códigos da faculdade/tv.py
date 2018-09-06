class tv:
    def __init__(self, polegadas, marca):
        self.polegadas = polegadas
        self.marca = marca
        self.estado = ""
        self.canais = {}
        self.volumemaximo = 10
        self.volumeminimo = 0
        self.volumeatual = 4
        self.canalatual = 2

    def ligar(self):
        self.estado = "TV Ligada"
    
    def desligar(self):
        self.estado = "TV Desligada"
    

    def aumentarvolume(self):
        if (self.volumeatual < self.volumemaximo):
            self.volumeatual += 1
        else:
            print("A TV está já está no volume máximo")

    def diminuirvolume(self):
        if (self.volumeatual > 0):
            self.volumeatual -= 1
        elif (self.volumeatual == 0):
            print("Mudo")


    def sincronizarcanais (self):
        l = int(input("Digite a quantidade de canais que deseja registrar: "))
        for x in range(0, l):
            c = input("Digite o canal: ")
            n = input("Digite o nome do canal: ")
            self.canais[n] = c
        
        for i in self.canais.keys():
            print("Canal: ",self.canais[i], i)

    
    def avançarcanal (self):
        self.canalatual += 1


       
t = tv("40", "Toshiba")

while(1==1):
    print("1 LIGAR TV" )
    print("2 DESLIGAR TV")
    print("3 SINTONIZAR CANAIS")
    print("4 AUMENTAR VOLUME")
    print("5 BAIXAR VOLUME")
    print('\n')
    print("--------------------")
    a = int(input("Digite a acao: "))
    print('\n')
    if (a == 1):
        t.ligar()
        print(t.estado)
        print('\n')
    elif (a == 2):
        t.desligar()
        print(t.estado)
        print('\n')
    elif (a == 3):
        t.sincronizarcanais()
        print(t.canais)
        print('\n')
    elif (a == 4):
        t.aumentarvolume()
        print(t.volumeatual)
        print('\n')
    elif (a == 5):
        t.diminuirvolume()
        print(t.volumeatual)
        print('\n')
  



