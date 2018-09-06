#Aluno: José Eduardo Pereira de Albuquerque RA:1801166
#AC03

class Pessoa:
    def __init__(self, Nome, dtNascimento, CPF, Telefone):

        self.Nome = Nome
        self.dtNascimento = dtNascimento
        self.CPF = CPF
        self.Telefone = Telefone


class Aluno(Pessoa):
    def __init__ (self, Nome, dtNascimento, CPF, Telefone, RA, turma, notas = {}):
        Pessoa.__init__(self, Nome, dtNascimento, CPF, Telefone)
        self.RA = RA
        self.turma = turma
        self.notas = {}
        
    def Desempenho(self):

        Qnt_Semestres = int(input("Quantos semestres o aluno cursou? -> "))
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        while Qnt_Semestres not in s :
            Qnt_Semestres = int(input("Quantos semestres o aluno cursou? -> "))
        
        for i in range (0, Qnt_Semestres):

            semestre = input ("Semestre: ")
            nota = int(input("Média: "))
            self.notas[semestre] = nota
        
        print(self.notas)

            
    def Dados_de_cadastro(self):
        print("Nome do Aluno: {} " .format(self.Nome))
        print ("Data de nascimento: {} " .format(self.dtNascimento))
        print("CPF: {} " .format(self.CPF))
        print("Telefone: {} " .format(self.Telefone))
        print("RA: {} " .format(self.RA))
        print("Turma: {} " .format(self.turma))


class AlunoRepetente(Aluno):
    def __init__(self, Nome, dtNascimento, CPF, Telefone, RA, turma, data_reprova, motivo_reprova, MateriasReprovadas = {}):
        Aluno.__init__(self, Nome, dtNascimento, CPF, Telefone, RA, turma, notas = {})
        self.data_reprova = data_reprova
        self.motivo_reprova = motivo_reprova.lower()
        self.MateriasReprovadas = {}

    def InformarMateriasReprovadas(self):

        if self.motivo_reprova == "nota":

            materia = input("Materia em que reprovou: ")
            nota = int(input("Nota da materia reprovada: "))
            self.MateriasReprovadas[materia] = nota

        elif self.motivo_reprova == "Falta":

            materia = input("Materia em que reprovou: ")
            falta = int(input("Qtd de faltas na materia reprovada: "))
            self.MateriasReprovadas[materia] = falta

    def dados_reprovado(self):
        self.Dados_de_cadastro()
        print("Data de reprovação: {} " .format(self.data_reprova))
        print("Motivo Reprovação: {} " .format(self.motivo_reprova))
        print("Matérias Reprovadas: {} " .format(self.MateriasReprovadas))

class ExAluno(Aluno):
    def __init__(self, Nome, dtNascimento, CPF, Telefone, RA, turma, anoformacao, qtdsemestreformado, notas = {}, faltas = 0):
        Aluno.__init__(self, Nome, dtNascimento, CPF, Telefone, RA, turma, notas = {})
        self.anoformacao = anoformacao
        self.qtdsemestreformado = qtdsemestreformado

    def dados_ExAluno(self):
        self.Dados_de_cadastro()
        print("Ano de formação: {} " .format(self.anoformacao))


while 1==1:
    print("+---------------------------------+")
    print("|1 Registrar desempenho de alunos |")
    print("|2 Registrar pedências de alunos  |")
    print("|3 Consultar Ex Alunos            |")
    print("|4 Executar todas as opções       |")
    print("+---------------------------------+")
          
    print("\n"*3)
   
    o = int(input("Selecione sua opção - > "))
    op = [1, 2, 3, 4]
    while o in op:
        
        
        if o == 1:
            print("\n"*1)
            print("+------------+")
            print("|Classe Aluno|")
            print("+------------+")
            print("\n"*1)
            a = Aluno("Eduardo","05-04-1994", "045.546.587-95","(81)94516-6547", 1801166, "C")
            a.Desempenho()
            a.Dados_de_cadastro()
            print("\n"*5)
            break
        elif o == 2:
            print("\n"*1)
            print("+---------------------+")
            print("|Classe AlunoRepetente|")
            print("+---------------------+")
            print("\n"*1)
            repro = AlunoRepetente("Daniel", "14-05-1996", "046.446.887-96", "(11)95465-5486", 1706546, "D", "01-12-2019", "nota")
            repro.InformarMateriasReprovadas()
            print("\n")
            repro.dados_reprovado()
            print("\n"*5)
            break
        elif o == 3:
            print("\n"*1)
            print("+--------------+")
            print("|Classe ExAluno|")
            print("+--------------+")
            print("\n"*1)
            f = ExAluno("Renato", "23/06/1995", "064.564.598-59","(11)95425-5486", 1706489, "B", "2022", 4)
            f.dados_ExAluno()
            print("\n"*1)
            break
        elif o == 4:
            print("\n"*1)
            print("+------------+")
            print("|Classe Aluno|")
            print("+------------+")
            print("\n"*1)
            a = Aluno("Eduardo","05-04-1994", "045.546.587-95","(81)94516-6547", 1801166, "C")
            a.Desempenho()
            a.Dados_de_cadastro()
            print("\n"*5)

            print("\n"*1)
            print("+---------------------+")
            print("|Classe AlunoRepetente|")
            print("+---------------------+")
            print("\n"*1)
            repro = AlunoRepetente("Daniel", "14-05-1996", "046.446.887-96", "(11)95465-5486", 1706546, "D", "01-12-2019", "nota")
            repro.InformarMateriasReprovadas()
            print("\n")
            repro.dados_reprovado()
            print("\n"*5)

            print("\n"*1)
            print("+--------------+")
            print("|Classe ExAluno|")
            print("+--------------+")
            print("\n"*1)
            f = ExAluno("Renato", "23/06/1995", "064.564.598-59","(11)95425-5486", 1706489, "B", "2022", 4)
            f.dados_ExAluno()
            print("\n"*1)
            break
            
            
            
            

                
                
 








