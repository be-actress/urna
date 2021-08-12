from tkinter import *
from tkinter import messagebox
import mysql.connector
from threading import Timer

"""
Urna eletronica para voto de melhor escritor
serão dois numeros. não use numeros polemicos, tipo 13 ou 17
deverá haver foto do escritor.


#------------------candidatos------------------
nome: Carina Rissi
numero: 57



nome: Christina Lauren
numero: 28



nome: Kiera cass
numero: 35
#------------------candidatos------------------
"""

bg = '#D3D3D3'
bot = {"bg": "#fff", "fg": '#000', 'bd': 5, "relief": "raised",  # configuração dos botoes
       "font": "Bookman\ Old\ Style 15",
       'activebackground': '#363636', 'activeforeground': '#FFF'}

fonte = "Bookman\ Old\ Style 30"

font = "Bookman\ Old\ Style 20"

bgLab = '#808080'  

class Banco():          #Classe do banco de dados
    def __init__(self):
        self.concect()
        if self.con == True:        #se o self.con for true
            
            self.cursor = self.conecta.cursor()  #self.curso pega a função de cursor
            self.objetos()
            

    def concect(self):      #faz a conexão
        
        try:                #tenta
            self.conecta = mysql.connector.connect( 
                user = 'root',                
                database='urnaa')          #faz conexão
            print("Conectado com sucesso")
            self.con = True                     #se conseguir conectar, self.con é True
        
        except:
            print('não consegui conectar')
            self.con = False                    #se não conseguir conectar, self.con é False
    
    
    
    def objetos(self):
        try:
            self.cursor.execute('CREATE database urnaa;')
            print('Criei o Bd urnaa')
            self.cursor.execute('USE urnaa')
            print('usando urnaa')


            #------------------------ Criando Tabelas ------------------------
            self.cursor.execute('''create table candidatos(
                                num int(2),
                                nome VARCHAR(100) NOT NULL);''')
            print('Criei tabela de candidatos')

            self.cursor.execute('''CREATE TABLE voto(
                                num_candidato int(2) not null,
                                qtde int unsigned);''')
            print('criei tabela de votos')

            self.cursor.execute('''CREATE TABLE Carina(votos_Carina INT AUTO_INCREMENT PRIMARY KEY,numeroCa int(2));''')
            
            print('Criei tabela Carina')
            self.cursor.execute('''CREATE TABLE Kiera(votos_Kiera INT AUTO_INCREMENT PRIMARY KEY,numeroK int(2));''')
            print('Criei tabela Kiera')
            self.cursor.execute('''CREATE TABLE ChLauren(votos_ChLauren INT AUTO_INCREMENT PRIMARY KEY,numeroCh int(2));''')
            print('Criei tabela ChLauren')
            self.cursor.execute('''CREATE TABLE Nulo(votos_Nulo INT AUTO_INCREMENT PRIMARY KEY,numeroNulo int(2));''')
            print('Criei tabela Nulo')
            self.conecta.commit()

            #------------------------ Criando Tabelas ------------------------



            #------------------------ Inserindo valores ------------------------            
            self.cursor.execute('''insert into candidatos
                                    value(28,'Christina Lauren')''')
                                    
            print("inseri chlauren")
            self.cursor.execute('''insert into candidatos 
                                    value(35,'Kiera Cass')''')
            print("inseri Kiera")
            self.cursor.execute('''insert into candidatos 
                                    value(57,'Carina Rissi')''')
            print("inseri Carina")
            #------------------------ Inserindo valores ------------------------ 



        except:
            self.cursor.execute('USE urnaa')
            print('except: usando a urnaa')
        
    def nome(self,name):  # Label que escreve nome
        if self.labRecebe['text'] == '35' or self.labRecebe['text'] == '28' or self.labRecebe['text'] == '57':
            
            self.nome = Label(self.root, text='Nome: {}'.format(name), font=font, bg=bgLab)
            self.nome.place(relx=0.025, rely=0.25)

        else:
            self.nome = Label(self.root, text='Este candidato não existe', font=font, bg=bgLab)
            self.nome.place(relx=0.025, rely=0.25)
            naoExiste = messagebox.askquestion(title='Confirma',
                                                   message='O numero digitado é invalido. \nDeseja Votar nulo?')

            if naoExiste == 'sim':  # se sim, o usuario quer votar nulo.
                pass  # aqui deveria ter uma função para votar nulo, mas ainda n sei como fazer isso, ent deixei em branco

            else:  # se não, ele n quer votar nulo.
                self.corrige()  # apaga o numero digitado pro usuário poder votar em alguem valido
        



class Inicio():         #classe da Urna
    def __init__(self, root,cursor, conectado):
        
        self.root = root
        self.cursor = cursor
        self.conexao = conectado    
        self.tela()

    def tela(self): #função da janela
        self.janConfig(jan=self.root, t="urna")     #configurações da janela

        #------------------------------------------------Labels------------------------------------------------
        self.fundo = Label(self.root, bg=bgLab, font=fonte) # label de fundo lado esquerdo
        self.fundo.place(relx=0.025, rely=0.01, relwidth=0.55, relheight=0.95)


        self.numero = Label(self.root, bg=bgLab,text="Número:",font=font)  
        self.numero.place(relx=0.025, rely=0.32, relwidth=0.1, relheight=0.08)


        self.labRecebe = Label(self.root, bg=bgLab,bd=2, font=fonte)  # label para receber o número do voto 
        self.labRecebe.place(relx=0.12, rely=0.32, relwidth=0.07, relheight=0.079)


        self.texto = Label(self.root, text='Votação para melhor escritora', bg=bgLab, font=font)
        self.texto.place(relx=0.025, rely=0.01, relwidth=0.55)


        self.labBotoes = Label(self.root, bg='#4F4F4F')  # label de fundo lado direito
        self.labBotoes.place(relx=0.53, rely=0.01, relwidth=0.437, relheight=0.95)
        #------------------------------------------------Labels------------------------------------------------

        # --------------------------Botões--------------------------
        self.bt1 = self.bot(self.root, t=1, x=0.55, y=0.05, c=lambda: self.mostrLabel('1'))  # primeira linha
        self.bt2 = self.bot(self.root, t=2, x=0.7, y=0.05, c=lambda: self.mostrLabel('2'))  # coloquei os numeros dentro do comando em '' pra ficar mais fácil
        self.bt3 = self.bot(self.root, t=3, x=0.85, y=0.05, c=lambda: self.mostrLabel('3'))

        self.bt4 = self.bot(self.root, t=4, x=0.55, y=0.2, c=lambda: self.mostrLabel('4'))  # segunda linha
        self.bt5 = self.bot(self.root, t=5, x=0.7, y=0.2, c=lambda: self.mostrLabel('5'))
        self.bt6 = self.bot(self.root, t=6, x=0.85, y=0.2, c=lambda: self.mostrLabel('6'))

        self.bt7 = self.bot(self.root, t=7, x=0.55, y=0.35, c=lambda: self.mostrLabel('7'))  # terceira linha
        self.bt8 = self.bot(self.root, t=8, x=0.7, y=0.35, c=lambda: self.mostrLabel('8'))
        self.bt9 = self.bot(self.root, t=9, x=0.85, y=0.35, c=lambda: self.mostrLabel('9'))

        self.bt0 = self.bot(self.root, t=0, x=0.7, y=0.5, c=lambda: self.mostrLabel('0'))  # ultima linha


        # ---------------------botoes de voto---------------------
        self.btbranco = self.btVoto(jan=self.root, t="Branco", x=0.55,c=self.branco)
        self.corrige = self.btVoto(jan=self.root, t="Corrige", x=0.7, b='#8B0000', c=self.corrige)
        self.confirma = self.btVoto(jan=self.root, t="Confirma", x=0.85, b='#32CD32', c=self.confirma)

        self.root.bind('<KeyPress>', self.teclado)  # conexão tela e teclado do pc
        # --------------------------Botões--------------------------


    #---------------------------------------- COMANDO DOS BOTOES ----------------------------------------
    def confirma(self):        
        num57 = '57'
        num28 = '28'
        num35 = '35'
        num00 = '00'
        if self.labRecebe['text'] == '57':
            self.cursor.execute(f'INSERT INTO Carina(numeroCa) values("{num57}");')
            print("inseri o 57")
        elif self.labRecebe['text'] == '28':
            self.cursor.execute('INSERT INTO Kiera(numeroK) values ("{num28}");')
            print("inseri o 28")
        elif self.labRecebe['text'] == '35':
            self.cursor.execute('INSERT INTO ChLauren(numeroCh) values("{num35}");')
            print("inseri o 35")
        else:            
            self.cursor.execute('INSERT INTO Nulo(numeroNulo) values("{num00}");')
            print("voto nulo")
        self.conexao.commit()

        self.label=Label(self.root,bg=bgLab,text='FIM',font=fonte)
        self.label.place(relx=0,rely=0,relheight=1,relwidth=1)
        self.tempo()

    
    def tempo(self):                    
        self.temp = Timer(5,self.tela)  #espera 5seg e dps executa a função tela
        self.temp.start()


    def corrige(self):  # apaga o número digitado
           
          self.labRecebe.config(text='')
          self.nome['text']='                                                  '
          self.lblFoto.config(image = '')# tira a imagem
        


 


    def branco(self):            
        self.cursor.execute('INSERT INTO nulo(numeroNulo) Values (00)')
        print("voto Branco")
        self.conexao.commit()

        self.label=Label(self.root,bg=bgLab,text='FIM',font=fonte)
        self.label.place(relx=0,rely=0,relheight=1,relwidth=1)    
        self.tempo()


    def teclado(self, evento):  # função para o teclado numerico aparecer
        lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for valor in lista:
            if str(evento.char) == valor:
                self.mostrLabel(valor)

    #---------------------------------------- COMANDO DOS BOTOES ----------------------------------------
    def nome(self,name):  # gambiarra pra me ajudar e n ter q criar label toda hora
        if self.labRecebe['text'] == '35' or self.labRecebe['text'] == '28' or self.labRecebe['text'] == '57':
            
            self.nome = Label(self.root, text='Nome: {}'.format(name), font=font, bg=bgLab)
            self.nome.place(relx=0.025, rely=0.25)

        else:
            self.nome = Label(self.root, text='Este candidato não existe', font=font, bg=bgLab)
            self.nome.place(relx=0.025, rely=0.25)
            naoExiste = messagebox.askquestion(title='Confirma',
                                                   message='O numero digitado é invalido. \nDeseja Votar nulo?')

            if naoExiste == 'sim':  # se sim, o usuario quer votar nulo.
                pass  # aqui deveria ter uma função para votar nulo, mas ainda n sei como fazer isso, ent deixei em branco

            else:  # se não, ele n quer votar nulo.
                self.corrige()  # apaga o numero digitado pro usuário poder votar em alguem valido


    #---------------------------------------- APARECE NA LABEL ----------------------------------------

    def mostrLabel(self, text):  # metodo para mostrar o numero na label
        self.ler = len(self.labRecebe['text'])  #conta quantos valores foram inseridos

        if self.ler <2:
            self.labRecebe['text'] += text      #adiciona um valor na label
        
        else:
            pass                                #o += é usado para caso vc adicione outro valor, ele adicona um do lado do outro

        print(self.ler)

        if self.ler >= 1:            
            if self.labRecebe['text'] == '57':

                                                      # print dados dos candidatos

                self.fotoLab('images.png')       
                self.nome('Carina Rissi') 
            
    
                            

            elif self.labRecebe['text'] == '28':

                self.fotoLab('chlauren.png')
                self.nome("Christina Lauren")
                

            elif self.labRecebe['text'] == '35':

                self.fotoLab('kiera2.png')
                self.nome("Kiera Cass")
                

            else:
                naoExiste = messagebox.askquestion(title='Confirma',
                                                   message='O numero digitado é invalido. \nDeseja Votar nulo?')

                if naoExiste == 'sim':  # se sim, o usuario quer votar nulo.
                    pass  # aqui deveria ter uma função para votar nulo, mas ainda n sei como fazer isso, ent deixei em branco

                else:  # se não, ele n quer votar nulo.
                    self.corrige()  # apaga o numero digitado pro usuário poder votar em alguem valido

            
    def nome(self,name):  # gambiarra pra me ajudar e n ter q criar label toda hora
            
            self.nome = Label(self.root, text='Nome: {}'.format(name), font=font, bg=bgLab)
            self.nome.place(relx=0.025, rely=0.25)         

    

    



    def fotoLab(self, imagem):  # só pra facilitar minha vida na hora de colocar a foto
            self.img = PhotoImage(file=imagem)
            self.lblFoto = Label(self.root, bg=bgLab, image=self.img)
            self.lblFoto.place(relx=0.3, rely=0.55, relwidth=0.2, relheight=0.35)

    #---------------------------------------- APARECE NA LABEL ----------------------------------------
        


    #--------------------------------------- Botões --------------------------------------- 

    def passa(self): 
        pass

    def bot(self, jan, t, x, y, c=passa):  # metodo botão de numero
        self.bt = Button(jan, bot, text=t, command=c)
        self.bt.place(relx=x, rely=y, relheight=0.1, relwidth=0.1)

    def btVoto(self, jan, t, x, y=0.8, b='#fff', c=passa):
        self.voto = Button(jan, bot, text=t, bg=b, command=c)
        self.voto.place(relx=x, rely=y, relheight=0.1, relwidth=0.1)




    #--------------------------------------- Botões --------------------------------------- 

    

    #--------------------------------------- Janela ---------------------------------------
    def janConfig(self, jan, t='Urna', b=bg, g='1200x600'):  # configuração da janela
        jan.geometry(g)
        jan.config(bg=b, relief='raised', bd=5)
        jan.title(t)
    #--------------------------------------- Janela ---------------------------------------



if __name__ == "__main__":
    banco = Banco()
    cursor = banco.cursor
    conexao = banco.conecta

    root = Tk()
    Inicio(root,cursor,conexao)
    root.mainloop()
