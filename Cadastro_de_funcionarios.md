def cadastro(val):
	dic = {}
    
	for i in range (0, val):
		n = input("Digite o nome do funcionário: ")
		m = input("Digite a matrícula do funcionário: ")

		dic[m] = n
		print("\n")
        
	print("###LISTA DE FUNCIONÁRIOS###: ")
	print("\n")

	for x in dic.keys():
		print("Matrícula: ", x)
		print("Nome:", dic[x])
		print("\n")
		
	salvarSN = input("Deseja salvar um relatório? Y/N ")
	
	if salvarSN == "Y":
		Salva(dic)
	elif salvarSN == "N":
		print('\n')
		print("+-----------------------------------+")
		print("| Obrigado por usar o nosso sistema |")
		print("+-----------------------------------+")



def Salva(dic):
	for x in dic.keys():
		r1 = "Funcionário: " + dic[x] + "\n"
		r2 = "Matrícula: " + x + "\n"
		r3 = "------------------\n"
		file = open('Relatorio.txt', '+a')
		file.write(r1)
		file.write(r2)
		file.write(r3)
		file.close()
	
	
continua = True
while continua:
	a = input("Digite a quantidade de registro que deseja fazer: ")
	if a.isdigit() == False:
		print("Digite apenas números! Pressione <ENTER> e tente novamente!")
		input() 
	else:
		val = int(a)
		cadastro(val)
		break

