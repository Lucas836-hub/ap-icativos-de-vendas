# Para montar : sons ,idioma ,cidade , senha , modularizar
# marcar produtos em pagar
#  refazer o banco , e ativar a contagem
# SENHA { se tiver ao iniciar bloqueia , esqueceu a senha , trocar a senhar , talvez bloquear a tela

#cidades =  nome , mes/ano , qunt_produtos

#  senha desenvolvedor
#  backup
#  verificar email
#  dados cidade + novo banco de dados


# VERSAO COMPLETA 0.9


from tkinter import *
import tkinter as tk
from datetime import datetime
from random import *
import sqlite3
import pygame
import platform
from PIL import Image, ImageTk
import os
import recortar_imagem

#  			BD

banco = sqlite3.connect("database/save_dados.db")
cursor = banco.cursor()

#banco_cit = sqlite3.connect("database/cidades.db")
#cursor_cit = banco_cit.cursor()

#try:
#	cursor_cit.execute()

try:
    cursor.execute("CREATE TABLE clientes(nome char NOT NULL , lugar char , telefone char,bairro char,local char,id char PRIMARY KEY)")

    banco.commit()

    #cursor.execute("CREATE TABLE produtos(id char , charque integer , margarina integer , fosforo integer , cream_crack integer , sete_capa integer , suica integer , amanteigada integer , praeira integer , pasta integer , sabonete integer, oleo integer)")

    #banco.commit()

    cursor.execute("CREATE TABLE mais(id char,devendo char , data_criacao char , data_receber char, valor_total real)")

        #   PREÇOS

    cursor.execute("CREATE TABLE preço(nome char, n_tabela char ,valor real) ")
    #prodito=[["Charque","Margarina","Fósforo", "Cream Crack","Sete Capa","Bolacha Suíca", "Bolacha Amanteigada", "Bolacha Praeira", "Pasta de Dente" , "Sabonete de arueira", "Oléo"] , ["charque","margarina","fosforo", "cream_crack","sete_capa","suica", "amanteigada", "praeira", "pasta" , "sabonete", "oleo"],[80,80,50,50,3,3,3,3,15,15,70]]

    #for a1 in range(0,len(prodito[0])):
    	#cursor.execute(f"INSERT INTO preço('nome','n_tabela',valor) VALUES (?,?,?)",(prodito[0][a1],prodito[1][a1],prodito[2][a1]))
    	banco.commit()



except:
	pass

try:
	cursor.execute("CREATE TABLE senha(pw_active char,pw char,pw_2 char,recuperar_conexao char,gmail char ,nome char,id char)")

	id_app="plataforma : "+str(platform.system())+" distribuição : "+platform.platform()+" id "+ f"${platform.node()} : {choice('abcdefghijklmnopqrstuvwxyz')}{choice('abcdefghijklmnopqrstuvwxyz')}{choice('abcdefghijklmnopqrstuvwxyz')}{randint(0,999)}{choice('abcdefghijklmnopqrstuvwxyz')}{choice('abcdefghijklmnopqrstuvwxyz')}{randint(0,999)}"

	cursor.execute(f"INSERT INTO senha(pw_active , pw , pw_2 ,recuperar_conexao,gmail,nome,id) VALUES(?,?,?,?,?,?,?)",('False','','','','','',id_app))

	banco.commit()

	cursor.execute("CREATE TABLE cidades(cidade char, id char)")
	banco.commit()

#	banco_cit.commit()


	cit=["Vitória","Bombos","Bonaça","Escada","Gloria"]

	for ggy in cit:
	    	id=f"{ggy}_{choice('abcdefghijklmnopqrstuvwxyz')}{randint(0,999)}{choice('abcdefghijklmnopqrstuvwxyz')}{choice('abcdefghijklmnopqrstuvwxyz')}{randint(0,999)}"

	    	cursor.execute(f'INSERT INTO cidades("cidade","id") VALUES (?,?)',(ggy,id,))
	    	banco.commit()

except:
	pass

banco_2 = sqlite3.connect("database/save_config.db")
cursor_2 = banco_2.cursor()

try:
	cursor_2.execute("CREATE TABLE dados(bg integer,idioma integer)")

	cursor_2.execute(f"INSERT INTO dados(bg , idioma ) VALUES (0,0)")
	banco_2.commit()

	cursor_2.execute("CREATE TABLE sons(toque char,erro char,resultado char)")

	cursor_2.execute(f"INSERT INTO sons(toque , erro ,resultado ) VALUES ('True','True','True')")

except:
	pass

#cursor.execute("SELECT * FROM cidades")
#kfdff=cursor.fetchall()
#
#for hdhh in range(0,len(kfdff)):
#	cursor_2.execute(f"CREATE TABLE {kfdff[hdhh][1]} (data char,charque integer , margarina integer , fosforo integer , cream_crack integer , sete_capa integer , suica integer , amanteigada integer , praeira integer , pasta integer , sabonete integer, oleo integer)")
#
#	cursor_2.execute('INSERT INTO {kfdff[hdhh][1]} ("data" ,"margarina","fosforo", "cream_crack","sete_capa","suica", "amanteigada", "praeira", "pasta" , "sabonete", "oleo") VALUES (?,"",0,0,0,0,0,0,0,0,0,0,0)')
#	banco_2.commit()



def dat_hor():
	data_e_hora_atuais = datetime.now()
	data_atual =data_e_hora_atuais.strftime("%d/%m/%Y")
	hora_atual = data_e_hora_atuais.strftime("%H:%M:%S")
	return str(f"{data_atual} {hora_atual}")

#         ESCOPOS GLOBAIS
produtos2=[]
produto_run=0
produto_nome=""
produto_quant=0
produto_preco=""
selec_produto=[]
select_cit=0
self2=tk
master2=tk
dados_cliente=["VAZIO","VAZIO","VAZIO","VAZIO","VAZIO","VAZIO"]
mais_global=["VAZIO","VAZIO","VAZIO","VAZIO","VAZIO"]
entry_dados=[0,0,0,0,0]
init_deven=0
tds_hj= True
caminho_image_exibida_galeria=""

dados_novo_clientes_temporario=[]
dados_produto_temporario=[]

init_play=True

gambiarra_sistema=list(os.getcwd())
gambiarra=""
for cvbnn in range(0,5):
    gambiarra+=gambiarra_sistema[cvbnn]

if gambiarra == "/home":
	del gambiarra_sistema[0]
	cade_barra = gambiarra_sistema.index("/")
	gambiarra="/"
	for cvbnn in range(0,cade_barra):
		gambiarra+=gambiarra_sistema[0]
		del gambiarra_sistema[0]

	gambiarra += "/"
	del gambiarra_sistema[0]
	cade_barra = gambiarra_sistema.index("/")
	for cvbnn in range(0, cade_barra):
		gambiarra += gambiarra_sistema[0]
		del gambiarra_sistema[0]
	gambiarra+="/"
	print(f"str montada {gambiarra}")
	loc_diretorio = gambiarra
	diretorio_pilha = [gambiarra]

else:
	loc_diretorio='/storage/emulated/0'
	diretorio_pilha=['/storage/emulated/0']
	print("erro entrou errado")

caminho_imagem_selecionada=''
ok=False
voltar_para_frame=tk
up_imag=False
pilha_return=[]
tamanho_do_cavas_rolavel=1280

def temporario():
	data_e_hora_atuais = datetime.now()
	hora_atual = data_e_hora_atuais.strftime("%H")
	hjsjs=[["black","white","black","green"],["white","black","gray","light green"],["white","gray","black","light green"]]
	#hora_atual=18
	if(int(hora_atual)>=6 and int(hora_atual)<=11):
		return hjsjs[0]
	if(int(hora_atual)>=12 and int(hora_atual)<=17):
		return hjsjs[2]
	if(int(hora_atual)>=18 or int(hora_atual)<=5):
		return hjsjs[1]

bg_geral=[["black","white","black","green"],["white","black","gray","light green"],["white","gray","black","light green"],temporario()]

cursor_2.execute("SELECT * FROM dados")
variavel_comando=cursor_2.fetchall()


def clean_produtos2():
	global produtos2
	try:
		for c in range(0,len(produtos2)):
			del produtos2[0]
	except:
		pass


def new_cliente(master):
	global cursor , banco,ok
	n=""
	try:
		cursor.execute("SELECT * FROM clientes")
		n=str(len(cursor.fetchall()))
	except:
		n="0"
	try:
		id=f"${n} : {choice('abcdefghijklmnopqrstuvwxyz')}{choice('abcdefghijklmnopqrstuvwxyz')}{choice('abcdefghijklmnopqrstuvwxyz')}{randint(0,999)}{choice('abcdefghijklmnopqrstuvwxyz')}{choice('abcdefghijklmnopqrstuvwxyz')}{randint(0,999)}"

		cursor.execute(f"INSERT INTO clientes('nome','lugar','telefone','bairro','local','id') VALUES (?,?,?,?,?,?)",(entry_dados[0].title(),entry_dados[1],entry_dados[2],entry_dados[3],entry_dados[4],id))

		# MAIS

		if(ok):
			output_dir=os.getcwd()
			output_dir+="/imagens"
			recortar_imagem.reduzir_tamanho_imagens(caminho_imagem_selecionada, output_dir,id)
			ok=False

		cursor.execute(f"INSERT INTO mais('id','devendo','data_criacao','data_receber',valor_total) VALUES (?,'false','00/00/0000 00:00:00','00/00/0000',0.0)",(id,))

		# CRIAR PRODUTOS
		cursor.execute(f"INSERT INTO produtos('id') VALUES (?)",(id,))
		banco.commit()

		cursor.execute('PRAGMA table_info(produtos)')

		colunas = [tupla[1] for tupla in cursor.fetchall()]
		for lg in range(0,len(colunas)-1):
			cursor.execute(f"UPDATE produtos SET {colunas[lg+1]} = 0 WHERE id = ?",(id,))
			banco.commit()

		master.switch_frame(StartPage)
	except:
		master.switch_frame(StartPage)


def run_mais():
	global banco , cursor
	try:
		cursor.execute("SELECT * FROM mais")
		lista=[]
		for c in cursor.fetchall():
			lista.append(c)

		return lista
	except:
		pass


def numb_valor(g):
	g=str(g).replace(".",",").strip()
	g.replace(" ","").replace("  ","")
	if(g ==""):
		return 0
	else:
		if(len(g)-1 - g.find(",") <2):
			g+="0"

		m=0
		if(len(g)-3 > 3):
			m=len(g)-3
			l=list(g)
			while (m > 2):
				m-=3
				l.insert(m," ")
			r=""
			for kl in range(0,len(l)):
				r+=str(l[kl])
			g=r
		return g


def run_clientes():
	global banco , cursor
	try:
		cursor.execute("SELECT * FROM clientes")
		lista=[]
		for c in cursor.fetchall():
			lista.append(c)

		return lista
	except:
		pass


def listbox_troca(self,master):
	master.switch_frame(Encomenda)


def v(t):
    i = tk.StringVar()
    i.set(t)
    return i

class SampleApp(tk.Tk):
    def __init__(self):
        global init_play ,cursor

        cursor.execute("SELECT * FROM senha")
        dados_senha=cursor.fetchall()

        tk.Tk.__init__(self)
        self._frame = None
        if (init_play and dados_senha[0][0] == "True"):
        	self.switch_frame(bloqueada)
        else:
        	self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


def add_frame(frame):
	global pilha_return
	try:
		if(frame not in pilha_return):
			pilha_return.append(frame)
		if(pilha_return[-2] == frame):
			del pilha_return[-1]
	except:
		pilha_return.append(frame)


class StartPage(tk.Frame):
    def __init__(self, master):
        global self2,master2 , dados_cliente , mais_global , produto_run,init_deven,variavel_comando,init_play,caminho_imagem_selecionada,up_imag,dados_novo_clientes_temporario,dados_produto_temporario

        caminho_imagem_selecionada=''
        add_frame(configuracao)
        add_frame(StartPage)

        dados_novo_clientes_temporario=[]
        dados_produto_temporario=[]

        if(not init_play):
        	som_save()

        init_play=False
        up_imag=False
        init_deven =0
        self2=self
        master2=master
        produto_run = 0
        clean_produtos2()

        init_deven =0
        master2=master
        produto_run = 0
        clean_produtos2()

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master["bg"]=bg=bg_geral[variavel_comando[0][0]][1]
        tk.Button(self,relief="flat", text="",width=8,bg="light gray").grid(row=0,column=0,sticky="nw")

        tk.Button(self, text=f"Adicionar novos clientes",relief="flat",bg="light gray",
                  command=lambda: master.switch_frame(PageOne)).grid(row=0,column=1)


        self.l=tk.Button(self, text="Devendo  ",width=36,relief="flat",bg="light gray",
                  command=lambda: master.switch_frame(devendo)).grid(row=1,column=0,columnspan=5)

        try:
             tam=[88,60]
             self.image = Image.open(os.getcwd()+'/imagens/imagem_app/images (1)_1.png')
             self.photo = ImageTk.PhotoImage(self.image.resize((tam[0],tam[1])))
             self.imagem = tk.Button(self, text="?",relief="flat",bg="light gray",image = self.photo,command=lambda: master.switch_frame(configuracao))
             self.imagem.image = self.photo
             self.imagem.grid(row=0,column=2)

        except:
        	tk.Button(self, text="?",relief="flat",bg="light gray",
                  command=lambda: master.switch_frame(configuracao)).grid(row=0,column=2)


        self.frame = JanelaRolavel(self)
        self.frame.grid(row=2,column=0,columnspan=3,sticky="w")

        self.data = sorted(run_clientes())

        #for i in range(30):
#             tk.Button(self.frame.conteudo,text="Botão {}".format(i)).pack(fill=tk.BOTH)
        self.var = IntVar()
        try:
           for c in range(0,len(self.data)):
           	cljpcy=os.getcwd()
           	cljpcy+="/imagens/"+self.data[c][5]+".jpeg"
           	if(os.path.exists(cljpcy)):
           		self.image = Image.open(cljpcy)
           		self.photo = ImageTk.PhotoImage(self.image.resize((180,180)))
           		imagem=tk.Label(self.frame.conteudo,image = self.photo)
           		imagem.image=self.photo
           		imagem.grid(row=c,column=0)
           	else:
           		self.image = Image.open("imagens/imagem_app/perfil.png")
           		self.photo = ImageTk.PhotoImage(self.image.resize((180,180)))
           		imagem=tk.Label(self.frame.conteudo,image = self.photo)
           		imagem.image=self.photo
           		imagem.grid(row=c,column=0)
           	tk.Radiobutton(self.frame.conteudo,text=f"{self.data[c][0]} de {self.data[c][1]}",relief="flat",width=23,height=5,value=c,justify="right",variable=self.var,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=self.go).grid(row=c,column=1)

        except:
           	pass
        master.title("Vendas")
        self.bind_all('<KeyPress>', self.controles)

    def go(self):
        global cursor,mais_global,master2
        i=self.var.get()
        for k in range(0,6):
              try:
                    dados_cliente.insert(k,self.data[i][k])
              except:
              	  dados_cliente.insert(k,"vazio")
        cursor.execute("SELECT * FROM mais WHERE id == ?",(dados_cliente[5],))
        masi=[]
        for c in cursor.fetchall():
              masi.append(c)
        for v in range(0,4):
             mais_global.insert(v,masi[0][v])
        listbox_troca(self2,master2)


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   del pilha_return[-1]
    	   master2.switch_frame(pilha_return[-1])





class JanelaRolavel(tk.Frame):
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)
        global tamanho_do_cavas_rolavel

        self["bg"]=bg_geral[variavel_comando[0][0]][1]
        # cria um canvas e uma barra de rolagem para rolá-lo:
        rolagem = tk.Scrollbar(self, orient=tk.VERTICAL)
        rolagem.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        self.canvas = tk.Canvas(self, bd=0,bg=bg_geral[variavel_comando[0][0]][1], highlightthickness=0,height=tamanho_do_cavas_rolavel,
                        yscrollcommand=rolagem.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        rolagem.config(command=self.canvas.yview)

        # reseta a visão:
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # cria um frame dentro do canvas
        # para que seja rolado junto com ele:
        self.conteudo =  tk.Frame(self.canvas,bg=bg_geral[variavel_comando[0][0]][1])
        self.id_conteudo = self.canvas.create_window(
            0, 0, window=self.conteudo, anchor=tk.NW)

        # cria eventos para detectar mudanças no canvas
        # e sincronizar com a barra de rolagem:
        self.conteudo.bind('<Configure>', self._configurar_conteudo)
        self.canvas.bind('<Configure>', self._configurar_canvas)


    def _configurar_conteudo(self, evento):
            # atualiza a barra de rolagem para o tamanho do frame de conteudo:
            tamanho = (
                self.conteudo.winfo_reqwidth(),
                self.conteudo.winfo_reqheight()
            )
            self.canvas.config(scrollregion="0 0 %s %s" % tamanho)
            if self.conteudo.winfo_reqwidth() != self.canvas.winfo_width():
                # atualizar tambem a largura do canvas para caber o conteudo:
                self.canvas.config(width=self.conteudo.winfo_reqwidth())

    def _configurar_canvas(self, evento):
        if self.conteudo.winfo_reqwidth() != self.canvas.winfo_width():
            # atualizar tambem a largura do conteudo para preencher o canvas:
            self.canvas.itemconfigure(
                self.id_conteudo, width=self.canvas.winfo_width())


# ADICIONA UM NOVO CLIENTE
class PageOne(tk.Frame):
    def __init__(self, master,*args, **kwargs):
        tk.Frame.__init__(self, master ,  *args, **kwargs)
        som_save()
        master.title("Vendas/Novo cliente")
        add_frame(PageOne)

        global entry_dados ,master2,variavel_comando,loc_diretorio,diretorio_pilha,caminho_imagem_selecionada,ok,voltar_para_frame,dados_novo_clientes_temporario,gambiarra

        voltar_para_frame=PageOne
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        loc_diretorio=gambiarra
        for ff in range(0,len(diretorio_pilha)):
        	del diretorio_pilha[0]
        diretorio_pilha.append(loc_diretorio)
        master2=master
        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(StartPage)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=19).grid(row=0,column=1)

        tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0,columnspan=3)


        try:
             tam=[500,500]
             self.image = Image.open(caminho_imagem_selecionada)
             self.photo = ImageTk.PhotoImage(self.image.resize((tam[0],tam[1])))
             self.imagem = tk.Button(self,text="teste imagem",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=500,height=500,command=lambda: master.switch_frame(modo_de_procura))
             self.imagem.image = self.photo
             self.imagem.grid(row=2,column=0,columnspan=3)
             ok=True

        except:
        	tk.Button(self,width=23,height=12,relief="flat",text="",command=lambda: master.switch_frame(modo_de_procura)).grid(row=2,column=0,columnspan=3)
        	ok=False


        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=3,column=0,ipady=6)

        #   Label

        tk.Label(self,text="Nome :",font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=4,column=0,stick="w",ipady=6)

        tk.Label(self,text="Cidade :",font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=5,column=0,stick="w",ipady=6)

        tk.Label(self,text="Telefone  :",font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=6,column=0,stick="w",ipady=6)

        tk.Label(self,text="Bairro  :",font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=7,column=0,stick="w",ipady=6)

        tk.Label(self,text="Local  :",font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=8,column=0,stick="w",ipady=6)

        #    Entry

        if (len(dados_novo_clientes_temporario)>0):
        	self.nome =tk.Entry(self,font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],textvariable=v(dados_novo_clientes_temporario[0]))
        	self.nome.grid(row=4,column=1,stick="w",ipady=6)

        	self.telefone=tk.Entry(self,font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],textvariable=v(dados_novo_clientes_temporario[1]))
        	self.telefone.grid(row=6,column=1,stick="w",ipady=6)

        	self.bairro=tk.Entry(self,font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],textvariable=v(dados_novo_clientes_temporario[2]))
        	self.bairro.grid(row=7,column=1,stick="w",ipady=6)

        	self.local=tk.Entry(self,font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],textvariable=v(dados_novo_clientes_temporario[3]))
        	self.local.grid(row=8,column=1,stick="w",ipady=6)

        else:
        	self.nome =tk.Entry(self,font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        	self.nome.grid(row=4,column=1,stick="w",ipady=6)

        	self.telefone=tk.Entry(self,font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        	self.telefone.grid(row=6,column=1,stick="w",ipady=6)

        	self.bairro=tk.Entry(self,font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        	self.bairro.grid(row=7,column=1,stick="w",ipady=6)

        	self.local=tk.Entry(self,font=('arial', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        	self.local.grid(row=8,column=1,stick="w",ipady=6)



        cursor.execute("SELECT * FROM cidades")
        self.nome_cidades=cursor.fetchall()

        try:
	        self.mb=  tk.Menubutton ( self, text=self.nome_cidades[0][0], relief=RAISED,width=21 )
	        self.mb.grid(row=5,column=1,stick="w",pady=6)
	        self.mb.menu =  Menu ( self.mb, tearoff = 0 )
	        self.mb["menu"] =  self.mb.menu

	        self.local_cit = IntVar()

	        for fct in range(0,len(self.nome_cidades)):
	        	self.mb.menu.add_radiobutton ( label=self.nome_cidades[fct][0],variable=self.local_cit, value=fct,command=self.cidade_selecionada )

        except:
        	pass

        #mb.pack()

        tk.Button(self,relief="flat", text="Salvar",
                  command=self.getando).grid(row=0,column=2)

        self.erro=tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1],font=("arial",10),text="",fg="red")
        self.erro.grid(row=10,column=0,columnspan=3,pady=50)

        self.sec=0
        self.substituir=False

        self.time=tk.Label(self)
        self.tick()
        self.bind_all('<KeyPress>', self.controles)


    def cidade_selecionada(self):
    	 self.mb["text"]=self.nome_cidades[self.local_cit.get()][0]

    def getando(self):
          try:
          	entry_dados[1]=self.nome_cidades[self.local_cit.get()][0]
          except:
          	self.erro["text"]="ERRO Não existe cidade"
          	som_erro()

          if(self.telefone.get() == ""):
          	entry_dados[2]="vazio"
          else:
          	entry_dados[2]=self.telefone.get()

          if(self.bairro.get() == ""):
          	entry_dados[3]="vazio"
          else:
          	entry_dados[3]=self.bairro.get()

          if(self.local.get() == ""):
          	entry_dados[4]="vazio"
          else:
          	entry_dados[4]=self.local.get()
          if(self.nome.get().strip() == ""):
          	self.erro["text"]="ERRO O CLIENTE ESTÁ SEM NOME"
          	som_erro()

          else:
          	entry_dados[0]=str(self.nome.get()).title()
          	new_cliente(master2)

    def controles(self,event):
        global pilha_return,master2,dados_novo_clientes_temporario
        if(event.keysym == "BackSpace"):
        	pass
        else:
         	try:
	         	if(list(self.telefone.get())[0] != "("):
	         		self.telefone.insert(0,"(")
	         	if(list(self.telefone.get())[3] != ")"):
	         		self.telefone.insert(3,")")
	         	if(list(self.telefone.get())[4] != " "):
	         		self.telefone.insert(4," ")
	         	if(list(self.telefone.get())[5] != "9"):
	         		self.telefone.insert(5,"9")
	         	if(list(self.telefone.get())[6] != " "):
	         		self.telefone.insert(6," ")

	         	if(list(self.telefone.get())[11] != " "):
	         		self.telefone.insert(11," ")
	         	if(list(self.telefone.get())[12] != "-"):
	         		self.telefone.insert(12,"-")
	         	if(list(self.telefone.get())[13] != " "):
	         		self.telefone.insert(13," ")
         	except:
	         	pass

        if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	del pilha_return[-1]
    	   	master2.switch_frame(pilha_return[-1])


    def tick(self):
    	global dados_novo_clientes_temporario

    	dados_novo_clientes_temporario=[self.nome.get(),self.telefone.get(),self.bairro.get(),self.local.get()]

    	self.sec = self.sec +1
    	self.time['text'] = self.sec
    	self.time.after(10, self.tick)


# Mostra uma lista com imagens igual uma galeria
class imagem_galeria(tk.Frame):
    def __init__(self, master):
        som_save()
        global self2,master2 , dados_cliente , mais_global , produto_run,init_deven,variavel_comando,init_play,caminho_imagem_selecionada,up_imag,dados_novo_clientes_temporario,dados_produto_temporario,caminho_image_exibida_galeria

        self2=self
        master2=master
        self.sec=0

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master["bg"]=bg=bg_geral[variavel_comando[0][0]][1]

        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(modo_de_procura)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)



        self.frame = JanelaRolavel(self)
        self.frame.grid(row=2,column=0,columnspan=3,sticky="w")


        #for i in range(30):
#             tk.Button(self.frame.conteudo,text="Botão {}".format(i)).pack(fill=tk.BOTH)
        self.var = IntVar()
        self.imagens_de_la=os.listdir(caminho_image_exibida_galeria)
        coluna_imagem=0
        self.linha_imagem=0
        try:
           for self.c in range(0,len(self.imagens_de_la)):
           	cljpcy=caminho_image_exibida_galeria+"/"+self.imagens_de_la[self.c]

           	if(cljpcy.endswith('png') or cljpcy.endswith('jpg') or cljpcy.endswith('jpeg')):
           		try:
           			self.image = Image.open(cljpcy)
           		except:
           			pass
           		else:
           			self.photo = ImageTk.PhotoImage(self.image.resize((218,218)))

           			imagem=tk.Button(self.frame.conteudo,image = self.photo)
           			imagem.image=self.photo
           			imagem.grid(row=self.linha_imagem,column=coluna_imagem)
           			coluna_imagem+=1
           			if(coluna_imagem ==3):
           				coluna_imagem=0
           				self.linha_imagem+=1
           				if(self.linha_imagem >= 6):
           					break
        except:
           	pass
        master.title("Vendas/Galeria")
        self.bind_all('<KeyPress>', self.controles)
        self.time = tk.Label(self, fg='green')
        self.mais_coluna=0

        self.tick()


    def go(self):
        global cursor,mais_global,master2
        i=self.var.get()
        for k in range(0,6):
              try:
                    dados_cliente.insert(k,self.data[i][k])
              except:
              	  dados_cliente.insert(k,"vazio")
        cursor.execute("SELECT * FROM mais WHERE id == ?",(dados_cliente[5],))
        masi=[]
        for c in cursor.fetchall():
              masi.append(c)
        for v in range(0,4):
             mais_global.insert(v,masi[0][v])
        listbox_troca(self2,master2)


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   del pilha_return[-1]
    	   master2.switch_frame(pilha_return[-1])


    def tick(self):
        global caminho_image_exibida_galeria
        self.sec +=1
        if(self.sec >= 3 and self.c <= len(self.imagens_de_la)):
        	try:
        		while True:
        			self.c+=1
        			if(self.c >= len(self.imagens_de_la)):
        				break

        			cljpcy=caminho_image_exibida_galeria+"/"+self.imagens_de_la[self.c]
        			if(cljpcy.endswith('png') or cljpcy.endswith('jpg') or cljpcy.endswith('jpeg')):
        				try:
        					self.image = Image.open(cljpcy)
        				except:
        					pass
	        			else:
	        				self.photo = ImageTk.PhotoImage(self.image.resize((218,218)))
	        				imagem=tk.Label(self.frame.conteudo,image = self.photo)
	        				imagem.image=self.photo
	        				imagem.grid(row=self.linha_imagem,column=self.mais_coluna)
	        				self.mais_coluna+=1
	        				if(self.mais_coluna>=3):
	        					self.linha_imagem+=1
	        					self.mais_coluna=0
	        				break
        	except:
        		pass
        self.time.after(10, self.tick)




# escolher modo de procura
class modo_de_procura(tk.Frame):
    def __init__(self, master):
        som_save()
        global master2,loc_diretorio,diretorio_pilha,voltar_para_frame

        master.title("Vendas/Modo de Procura")

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master["bg"]=bg=bg_geral[variavel_comando[0][0]][1]

        produto_run = 1
        master2=master
        add_frame(selection_image)

        tk.Button(self, text="Cancelar",relief="flat",
                  command=lambda: master.switch_frame(voltar_para_frame)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)

        tk.Label(self,height=1,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        tk.Button(self,width=28,text="Câmera",command=self.Câmera).grid(row=2,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Downloads",command=self.Downloads).grid(row=3,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Whatsapp",command=self.Whatsapp).grid(row=4,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Instagram",command=self.Instagram).grid(row=5,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Captura de Tela",command=self.screen).grid(row=6,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Facebook",command=self.Facebook).grid(row=7,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Gerenciador de Arquivos",command=lambda:master.switch_frame(selection_image)).grid(row=8,column=0,columnspan=3,pady=20)


        self.bind_all('<KeyPress>', self.controles)

        #caminho_image_exibida_galeria
    def Câmera(self):
    	global caminho_image_exibida_galeria,master2,gambiarra
    	caminho_image_exibida_galeria=gambiarra+"Camera"
    	master2.switch_frame(imagem_galeria)

    def Downloads(self):
    	global caminho_image_exibida_galeria,master2,gambiarra
    	caminho_image_exibida_galeria=gambiarra+"Download"
    	master2.switch_frame(imagem_galeria)


    def Whatsapp(self):
    	global caminho_image_exibida_galeria,gambiarra
    	caminho_image_exibida_galeria=gambiarra+"WhatsApp/Media/WhatsApp Images"
    	master2.switch_frame(imagem_galeria)


    def Instagram(self):
    	global caminho_image_exibida_galeria,master2,gambiarra
    	caminho_image_exibida_galeria=gambiarra+"Pictures/Instagram"
    	master2.switch_frame(imagem_galeria)


    def Facebook(self):
    	global caminho_image_exibida_galeria,master2,gambiarra
    	caminho_image_exibida_galeria=gambiarra+"Pictures/Messenger"
    	master2.switch_frame(imagem_galeria)


    def screen(self):
    	global caminho_image_exibida_galeria,master2,gambiarra
    	caminho_image_exibida_galeria=gambiarra+"Pictures/Screenshots"
    	master2.switch_frame(imagem_galeria)

    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		event.keysym= None
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])


    def voltar(self):
	    global master2,loc_diretorio,diretorio_pilha
	    try:
		    if(len(diretorio_pilha) > 1):
			    loc_diretorio=diretorio_pilha[-1]
			    del diretorio_pilha[-1]
			    master2.switch_frame(selection_image)
	    except:
	          som_erro_2()



#  DIRETORIOS

class selection_image(tk.Frame):
    def __init__(self, master):
        som_save()
        global master2,loc_diretorio,diretorio_pilha,voltar_para_frame

        master.title("Vendas/Selecionador de arquivos")

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master["bg"]=bg=bg_geral[variavel_comando[0][0]][1]

        produto_run = 1
        master2=master
        add_frame(selection_image)

        tk.Button(self, text="Cancelar",relief="flat",
                  command=lambda: master.switch_frame(voltar_para_frame)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)

        tk.Label(self,height=1,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        tk.Button(self, text="<-",relief="flat",
                  command=self.voltar).grid(row=1,column=0)


        scrollbar = tk.Scrollbar(self,bg="white")

        self.mylist = tk.Listbox(self,width=32,height=26,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=("arial",10),yscrollcommand = scrollbar.set )

        self.diretorios=os.listdir(loc_diretorio)

        for c in range(0,len(self.diretorios)):
            self.mylist.insert(c,self.diretorios[c])

        self.mylist.grid(row=3,column=0,columnspan=3,sticky="w")

        scrollbar.config( command = self.mylist.yview)

        self.mylist.bind("<<ListboxSelect>>", self.on_listbox_select)
        self.bind_all('<KeyPress>', self.controles)

        self.test_lab=tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],text=loc_diretorio,width=28).grid(row=1,column=1,columnspan=3)

    def on_listbox_select(self,event):
	    global master2,loc_diretorio,diretorio_pilha
	    try:
		    i = self.mylist.curselection()[0]
		    text = self.mylist.get(i)
		    diretorio_pilha.append(loc_diretorio)
		    loc_diretorio=loc_diretorio+'/'+text
		    if(self.diretorios[i].endswith('png') or self.diretorios[i].endswith('jpg') or self.diretorios[i].endswith('jpeg')):
		    	master2.switch_frame(image_confirmar)
		    else:
		    	master2.switch_frame(selection_image)
	    except:
	    	#pass
	    	som_erro_2()
	    	loc_diretorio=diretorio_pilha[-1]
	    	del diretorio_pilha[-1]


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])
    	if event.keysym == 'Left':
    		self.voltar()#yview_scroll (número, o quê)


    def voltar(self):
	    global master2,loc_diretorio,diretorio_pilha
	    try:
		    if(len(diretorio_pilha) > 1):
			    loc_diretorio=diretorio_pilha[-1]
			    del diretorio_pilha[-1]
			    master2.switch_frame(selection_image)
	    except:
	          som_erro_2()


class image_confirmar(tk.Frame):
    def __init__(self, master):
        som_save()
        global master2,loc_diretorio,diretorio_pilha

        master.title("Vendas/Selecionador de arquivos")

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master["bg"]=bg=bg_geral[variavel_comando[0][0]][1]

        produto_run = 1
        master2=master
        add_frame(image_confirmar)

        tk.Button(self, text="Cancelar",relief="flat",
                  command=self.voltar).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=12).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="Selecionar",command=self.salvar).grid(row=0,column=2)

        tk.Label(self,height=2,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        try:
             self.image = Image.open(loc_diretorio)
             self.photo = ImageTk.PhotoImage(self.image.resize((690,690)))
             self.imagem = tk.Button(self,text="teste imagem",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=690,command=lambda: master.switch_frame(selection_image))
             self.imagem.image = self.photo
             self.imagem.grid(row=2,column=0,columnspan=3)

        except:
        	tk.Button(self,width=23,height=12,relief="flat",text="",command=lambda: master.switch_frame(selection_image)).grid(row=2,column=0,columnspan=3)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=3,column=0)

        tk.Button(self,text="<- Anterior",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=self.anterior).grid(row=4,column=0,columnspan=2,padx=20)

        tk.Button(self,text="Proximo ->",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=self.proximo).grid(row=4,column=1,columnspan=2)


        self.imagens_local=[]
        carr=os.listdir(diretorio_pilha[-1])
        for bdj in range(0,len(carr)):
        	if(recortar_imagem.eh_imagem(carr[bdj]) == True):
        		self.imagens_local.append(diretorio_pilha[-1]+"/"+carr[bdj])
        	else:
        		pass
        self.bind_all('<KeyPress>', self.controles)

        #self.bdj=Label(self,text=f"{diretorio_pilha[-1]}\n{diretorio_pilha[-2]}")
       # self.bdj.grid(row=5,column=0,columnspan=3)

    def anterior(self):
	    global master2,loc_diretorio,diretorio_pilha
	    try:
	     	#self.bdj["text"]=f"{self.imagens_local}"
	     	p=self.imagens_local.index(loc_diretorio)
	     	loc_diretorio=self.imagens_local[p-1]
	     	#loc_diretorio=diretorio_pilha[-1]
	     	master2.switch_frame(image_confirmar)
	    except:
	          pass


    def proximo(self):
	    global master2,loc_diretorio,diretorio_pilha
	    try:
	     	#self.bdj["text"]=f"{self.imagens_local}"
	     	p=self.imagens_local.index(loc_diretorio)
	     	if(p+1 >= len(self.imagens_local) ):
	     		loc_diretorio=self.imagens_local[0]
	     	else:
	     		loc_diretorio=self.imagens_local[p+1]
	     	#loc_diretorio=diretorio_pilha[-1]
	     	master2.switch_frame(image_confirmar)
	    except:
	          pass

    def voltar(self):
	    global master2,loc_diretorio,diretorio_pilha,up_imag
	    up_imag=False
	    try:
		    if(len(diretorio_pilha) > 1):
			    loc_diretorio=diretorio_pilha[-1]
			    del diretorio_pilha[-1]
			    master2.switch_frame(selection_image)
	    except:
	          pass


    def salvar(self):
	    global master2,loc_diretorio,diretorio_pilha,caminho_imagem_selecionada,voltar_para_frame,up_imag
	    try:
	    	caminho_imagem_selecionada= loc_diretorio
	    	up_imag=True
	    	master2.switch_frame(voltar_para_frame)
	    except:
	          pass


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])
    	if event.keysym == 'Right':
    		self.proximo()
    	if event.keysym == 'Left':
    		self.anterior()

class quantdade_de_produtos(tk.Frame):
    def __init__(self, master):
        som_save()
        global produto_run , produto_nome , produto_quant, master2,produto_preco,variavel_comando,cursor

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master["bg"]=bg=bg_geral[variavel_comando[0][0]][1]

        master.title("Vendas/Quantidade do produto")

        produto_run = 1
        master2=master
        add_frame(quantdade_de_produtos)

        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(Encomenda)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)

        tk.Label(self,height=1,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        cursor.execute("SELECT * FROM preço WHERE nome == ?",(produto_nome,))
        vshs=cursor.fetchall()

        cljpcy=os.getcwd()
        cljpcy+="/imagens/"+vshs[0][1]+".jpeg"

        try:
             if True :
             	self.image = Image.open(cljpcy)

             self.photo = ImageTk.PhotoImage(self.image.resize((500,500)))
             self.imagem = tk.Button(self,text="teste imagem",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=500,height=500,command=lambda: master.switch_frame(selection_image))
             self.imagem.image = self.photo
             self.imagem.grid(row=2,column=0,columnspan=3)
             #ok=True
        except:
        	tk.Button(self,width=23,height=12,relief="flat",text="").grid(row=2,column=0,columnspan=3)

        tk.Label(self,height=1,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=3,column=0)

        tk.Label(self,text=f"Nome :",font=("arial",10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=4,column=0)

        tk.Label(self,text="Preço :",font=("arial",10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=5,column=0)

        tk.Label(self,text="Quantidade : ",font=("arial",10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=6,column=0,columnspan=2,stick="w",pady=10,padx=28)

        tk.Label(self,text="Valor total : ",font=("arial",10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=7,column=0,columnspan=2,stick="w",pady=10,padx=28)

        tk.Label(self,text=produto_nome,font=("arial",10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=4,column=1,columnspan=2,stick="w")

        tk.Label(self,text=produto_preco,font=("arial",10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=5,column=1,columnspan=2,stick="w")

        self.q=tk.Spinbox(self,font=("arial",10),from_ = 0,to = 999999,width=8,textvariable=v(produtos2[int(produto_quant)]),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=self.teste)
        self.q.grid(row=6,column=1,pady=10)

        self.valor_tt=tk.Label(self,text="0,00",font=("arial",10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        self.valor_tt.grid(row=7,column=1,stick="w",padx=50)

        tk.Button(self,text="OK",font=("arial",10),fg="blue",command=self.conf).grid(row=8,column=1,pady=50)

        self.erro=tk.Label(self,fg="red",bg=bg_geral[variavel_comando[0][0]][1])
        self.erro.grid(row=9,column=0,columnspan=2,pady=30)
        self.teste()
        self.bind_all('<KeyPress>', self.controles)

    def teste(self):
    	global produto_run , produto_nome , produto_quant,produto_preco
    	try:
    		self.erro["text"]=""
    		m=num(produto_preco)[0]
    		n=m * int(self.q.get())
    		n=numb_valor(f"{n:.2f}")
    		self.valor_tt["text"]=f"{n}"
    	except:
    		self.erro["text"]="OCORREU UM ERRO :("
    		som_erro()

    def conf(self):
          global produto_run , produto_nome , produto_quant, master2,produtos2
          try:
          	del produtos2[int(produto_quant)]
          	produtos2.insert(int(produto_quant),int(self.q.get()))
          	master2.switch_frame(Encomenda)
          except:
              self.erro["text"]="OCORREU UM ERRO :("
              som_erro()

    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])


class Encomenda(tk.Frame):
    def __init__(self, master):
        som_save()
        global dados_cliente , cursor , banco ,mais_global , produtos2 ,produto_run,master2,variavel_comando,tamanho_do_cavas_rolavel

        master["bg"]=bg=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master2=master

        master.title("Vendas/Encomenda")
        add_frame(Encomenda)
        tamanho_do_cavas_rolavel=1280

        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(StartPage)).grid(row=0,column=0)


        tk.Button(self,bg="light gray",relief="flat",width=5).grid(row=0,column=1,stick="w")

        tk.Button(self,bg="light gray",relief="flat",width=4).grid(row=0,column=3,stick="w")


        try:
             if(mais_global[1] == 'false'):
                  tk.Button(self,relief="flat", text="Paga divida",
                  command=lambda: master.switch_frame(pagar)).grid(row=0,column=4)
             else:
             	tk.Button(self,fg="red",relief="flat", text="Paga divida",
                  command=lambda: master.switch_frame(pagar)).grid(row=0,column=4)

        except:
             tk.Button(self,relief="flat", text="Paga divida",
                  command=lambda: master.switch_frame(pagar)).grid(row=0,column=4)

        tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1],height=1).grid(row=1,column=0)

        cljpcy=os.getcwd()
        cljpcy+="/imagens/"+mais_global[0]+".jpeg"

        try:
        	self.image = Image.open(cljpcy)
        	self.photo = ImageTk.PhotoImage(self.image.resize((300,300)))
        	self.imagem = tk.Button(self,text="",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=300,height=300)
        	self.imagem.image = self.photo
        	self.imagem.grid(row=2,column=0,columnspan=2,stick="n")
        except:
        	#   "imagens/imagem_app/perfil.png"
        	self.image = Image.open("imagens/imagem_app/perfil.png")
        	self.photo = ImageTk.PhotoImage(self.image.resize((300,300)))
        	self.imagem = tk.Button(self,text="",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=300,height=300)
        	self.imagem.image = self.photo
        	self.imagem.grid(row=2,column=0,columnspan=2,stick="n")


        tk.Label(self,width=19,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Nome : {dados_cliente[0]}",anchor="w").grid(row=2,column=2,stick="n",columnspan=5)

        tk.Label(self,width=19,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Lugar : {dados_cliente[1]}",anchor="w").grid(row=2,column=2,stick="s",columnspan=3)

        tk.Label(self,width=19,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Telefone :  {dados_cliente[2]}",anchor="w").grid(row=2,column=2,columnspan=3,pady=40)

        tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1]).grid(row =3,column=0)

        tk.Button(self,text="Adicionar nova divida",bg="light blue",command=lambda:master.switch_frame(confirmar_divida)).grid(row=5,column=1,columnspan=4,pady=20)

        tk.Button(self,text="Update",command=lambda: master.switch_frame(conf_cliente1)).grid(row=5,column=0,columnspan=3)

        scrollbar = tk.Scrollbar(self,bg=bg_geral[variavel_comando[0][0]][1])

        self.mylist = tk.Listbox(self,width=32,height=14,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=("arial",10),yscrollcommand = scrollbar.set )

        cursor.execute("SELECT * FROM preço")
        self.lista=[]
        for c in sorted(cursor.fetchall()):
        	self.lista.append(c)

        try:
           if(produto_run == 0 and len(produtos2) >1 ):
           	for c in range(0,len(produtos2)):
           		del produtos2[0]
           else:
              for c in range(0,len(self.lista)):
                    if(produto_run == 0):
                       produtos2.append(0)
                       self.mylist.insert(c,f"{produtos2[c]}   {self.lista[c][0]}")
                    if(produto_run == 1):
                    	self.mylist.insert(c,f"{produtos2[c]}   {self.lista[c][0]}")

        except:
        	pass

        self.mylist.grid(row=4,column=0,columnspan=6,sticky="w")

        scrollbar.config( command = self.mylist.yview )

        self.mylist.bind("<<ListboxSelect>>", self.on_listbox_select)
        self.bind_all('<KeyPress>', self.controles)

    def on_listbox_select(self,event):
            global cursor,mais_global,produto_nome,produto_quant,produto_preco
            i = self.mylist.curselection()[0]
            text = self.mylist.get(i)
            produto_quant = int(i)
            produto_nome = self.lista[i][0]
            produto_preco = numb_valor(self.lista[i][2])
            self.mylist.insert("end",f"new value : {text}")
            master2.switch_frame(quantdade_de_produtos)
    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])



#PERMITE O PAGAMENTO DE UM DEBITO
class pagar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        som_save()
        global dados_cliente , banco ,cursor,produto_run,master2,variavel_comando,tamanho_do_cavas_rolavel

        tamanho_do_cavas_rolavel=278

        produto_run = 1
        master2=master
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master["bg"]=bg=bg_geral[variavel_comando[0][0]][1]

        master.title("Vendas/Pagamento da divida")
        add_frame(pagar)

        if(init_deven == 0):
                  tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(Encomenda)).grid(row=0,column=0)
        else:
                tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(devendo)).grid(row=0,column=0)
        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="Salvar  ",command=self.save).grid(row=0,column=2)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text="Produtos : ").grid(row=1,column=0,pady=50)

        self.frame = JanelaRolavel(self)
        self.frame.grid(row=1,column=1,columnspan=3,sticky="w")

        cursor.execute("SELECT * FROM preço")
        lista=cursor.fetchall()
        cursor.execute("SELECT * FROM produtos WHERE id = ?",(dados_cliente[5],))
        self.quantidade_produtos=cursor.fetchall()

        self.valores=[]
        self.marcou=False
        self.produtos_aceitos=[]
        self.precos_aceitos=[]
        self.colunas_marcadas=[]
        if True:#try:
             for self.c in range(0,len(lista)):

                    if(self.quantidade_produtos[0][self.c+1] >0):
                    	self.colunas_marcadas.append(lista[self.c][1])
                    	self.valores.append(IntVar())
                    	tk.Checkbutton(self.frame.conteudo, variable = self.valores[-1] ,onvalue = 1, offvalue = 0,font=('Helvetica', 8), text=f"{self.quantidade_produtos[0][self.c+1]} {lista[self.c][0]}",fg=bg_geral[variavel_comando[0][0]][2],bg=bg_geral[variavel_comando[0][0]][1],command=self.marcado).grid(row=self.c,column=0,stick="w")
                    	self.produtos_aceitos.append(self.quantidade_produtos[0][self.c+1])
                    	self.precos_aceitos.append(lista[self.c][2])

        #except:
#               pass

        #self.mylist.grid(row=1,column=1,columnspan=4,sticky="w",pady=40)

     #   scrollbar.config( command = self.mylist.yview )
        tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=2,column=0)
        try:
           cursor.execute("SELECT * FROM mais WHERE id == ?",(dados_cliente[5],))
           self.dados_n=cursor.fetchall()
        except:
            pass

        cljpcy=os.getcwd()
        cljpcy+="/imagens/"+mais_global[0]+".jpeg"

        try:
        	self.image = Image.open(cljpcy)
        	self.photo = ImageTk.PhotoImage(self.image.resize((270,270)))
        	self.imagem = tk.Button(self,text="",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1])
        	self.imagem.image = self.photo
        	self.imagem.grid(row=3,column=0,columnspan=2,stick="w")
        except:
        	#   "imagens/imagem_app/perfil.png"
        	self.image = Image.open("imagens/imagem_app/perfil.png")
        	self.photo = ImageTk.PhotoImage(self.image.resize((270,270)))
        	self.imagem = tk.Button(self,text="",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1])
        	self.imagem.image = self.photo
        	self.imagem.grid(row=3,column=0,columnspan=2,stick="w")

        scrollbar = tk.Scrollbar(self,bg=bg_geral[variavel_comando[0][0]][1])

        self.mylist_38= tk.Listbox(self,height=6,width=19,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=("arial",9),yscrollcommand = scrollbar.set )

        self.mylist_38.insert(0,f"Cliente : {dados_cliente[0]}")
        self.mylist_38.insert(1,f"Fone : {dados_cliente[2]}")
        self.mylist_38.insert(2,f"Lugar : {dados_cliente[1]}")
        self.mylist_38.insert(3,f"Bairro : {dados_cliente[3]}")
        self.mylist_38.insert(4,f"Local : {dados_cliente[4]}")

        self.mylist_38.grid(row=3,column=1,columnspan=4,padx=90,ipady=10)


 #       tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Cliente : {dados_cliente[0]}").grid(row=3,column=0,columnspan=2,stick="w")
#
#        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Lugar : {dados_cliente[1]}").grid(row=4,column=0,columnspan=2,stick="w")
#
#        tk.Label(self,anchor="w",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Telefone : {dados_cliente[2]}").grid(row=3,column=1,columnspan=2,sticky="w")
#
#        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Bairro : {dados_cliente[3]}").grid(row=6,column=0,columnspan=2,stick="w")
#
#        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Local : {dados_cliente[4]}").grid(row=7,column=0,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=8,column=0)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Valor total R$ : {numb_valor(self.dados_n[0][4])}").grid(row=9,column=0,columnspan=2,stick="w")

        tk.Label(self,text=f"Dia : {self.dados_n[0][2]}",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=10,column=0,columnspan=2,stick="w")

        tk.Label(self,text=f"Receber : {self.dados_n[0][3]}",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=11,column=0,columnspan=3,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text="Valor pago R$ :").grid(row=12,column=0,columnspan=3,stick="w")

        self.pg=tk.Entry(self,width=11,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        self.pg.grid(row=12,column=1,columnspan=3,stick="w",padx=30)

        self.marc=tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text="Valor Marcado R$ : 0,00")
        self.marc.grid(row=13,column=0,columnspan=3,stick="w")

        self.troco=tk.Button(self,text="Troco R$ : 0,00",relief="flat",bg="light gray",command=self.print_troco)
        self.troco.grid(row=14,column=0,columnspan=3,pady=20)

        self.erro=tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1],fg="red")
        self.erro.grid(row=15,column=0,columnspan=3,pady=30)
        self.bind_all('<KeyPress>', self.controles)

    def  marcado(self):
        global banco,cursor,dados_cliente
        self.valor_tot=0
        self.marcou=False
        for t in range(0,len(self.precos_aceitos)):
        	if(self.valores[t].get() == 1):
        		self.valor_tot+=self.precos_aceitos[t] * self.produtos_aceitos[t]
        		self.marcou=True

        fyhhf=numb_valor(f"{self.valor_tot:.2f}")
        self.marc["text"]=f"Valor Marcado R$ : {fyhhf}"


    def print_troco(self):
    	try:
    		self.erro["text"]=""
    		if(self.dados_n[0][4] - num(self.pg.get())[0] < 0):
    			if(self.marcou == False):
    				str_cjcvh=self.dados_n[0][4] - num(self.pg.get())[0]
    				stshwh=f"{str_cjcvh:.2f}"
    				self.troco["text"]=f"Troco R$ : {numb_valor(stshwh.replace('-',''))}"
    				#oooookkooooo
    			else:
    				str_cjcvh=self.valor_tot - num(self.pg.get())[0]
    				stshwh=f"{str_cjcvh:.2f}"
    				self.troco["text"]=f"Troco R$ : {numb_valor(stshwh.replace('-',''))}"

    		else:
    			#oooooooooooooo
    			if(self.marcou == True):
    				str_cjcvh=self.valor_tot - num(self.pg.get())[0]
    				if(str_cjcvh<0):
    					stshwh=f"{str_cjcvh:.2f}"
    					self.troco["text"]=f"Troco R$ : {numb_valor(stshwh.replace('-',''))}"
    			else:
    				self.troco["text"]=f"Troco R$ : 0,00"
    	except:
    		self.troco["text"]=f"Troco R$ : 0,00"
    		self.erro["text"]="VALOR INVÁLIDO !"
    		som_erro()


    def  save(self):
        global banco,cursor,dados_cliente,master2
        try:
        	self.erro["text"]=""
        	if(num(self.pg.get())[1] == "true"):
        		if(self.dados_n[0][4] - num(self.pg.get())[0] > 0):

        			if(self.marcou == True):
        				str_cjcvh=self.dados_n[0][4] - num(self.pg.get())[0]
        				stshwh=f"{str_cjcvh:.2f}"
        				self.troco["text"]=f"Troco R$ : {numb_valor(stshwh.replace('-',''))}"
	        			cursor.execute("UPDATE mais SET data_criacao = ? ,valor_total = ? WHERE id == ?",(dat_hor(),stshwh,dados_cliente[5],))
	        			preco_fghg=num(self.pg.get())[0]
	        			valor_ffgggg=0
	        			for zxxs in range(0,len(self.colunas_marcadas)):
	        				if(self.valores[zxxs].get() == 1):
	        					fhb=preco_fghg // self.precos_aceitos[zxxs]
	        					valor_ffgggg=fhb
	        					if(fhb <= self.produtos_aceitos[zxxs]):
	        						preco_fghg=0
	        					else:
	        						preco_fghg=preco_fghg-valor_ffgggg
	        					cursor.execute(f"UPDATE produtos SET {self.colunas_marcadas[zxxs]} = ? WHERE id = ?",(self.produtos_aceitos[zxxs]-fhb,dados_cliente[5],))
	        			self.erro["text"]=f"{fhb}"
	        			som_erro()

# valor pago / valor do produto if
# self.precos_aceitos[t] * self.produtos_aceitos[t]

	        			#	banco.commit()

	        			#master2.switch_frame(StartPage)

        		else:

        			str_cjcvh=self.dados_n[0][4] - num(self.pg.get())[0]
        			stshwh=f"{str_cjcvh:.2f}"
        			self.troco["text"]=f"Troco R$ : {numb_valor(stshwh.replace('-',''))}"

        			cursor.execute("UPDATE mais SET devendo = ? ,data_criacao = ? ,data_receber = ? , valor_total = ? WHERE id == ?",("false","00/00/0000 00:00:00","00/00/0000",0,dados_cliente[5],))
        			cursor.execute('PRAGMA table_info(produtos)')
        			colunas = [tupla[1] for tupla in cursor.fetchall()]
        			for lg in range(0,len(colunas)-1):
        				cursor.execute(f"UPDATE produtos SET {colunas[lg+1]} = 0 WHERE id = ?",(dados_cliente[5],))
        				banco.commit()
        			master2.switch_frame(StartPage)

        	else:
        		self.erro["text"]="VALOR INVÁLIDO !"
        		som_erro()

        except:
        	self.erro["text"]="OCORREU UM ERRO !"
        	som_erro()


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])



#PEDE A CONFIMACAO DA DIVIDA

class confirmar_divida(tk.Frame):
    def __init__(self, master):
        som_save()
        global data_atual , hora_atual,produto_run,master2,variavel_comando
        master2=master
        produto_run=1

        master["bg"]=bg=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])

        master.title("Vendas/Finalizar encomenda")
        add_frame(confirmar_divida)

        valor=0

        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(Encomenda)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="Salvar",command=self.save).grid(row=0,column=2)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text="Produtos : ").grid(row=1,column=0,pady=50)

        scrollbar = tk.Scrollbar(self,bg="white")

        mylist = tk.Listbox(self,width=27,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],height=6,yscrollcommand = scrollbar.set )

        cursor.execute("SELECT * FROM preço")
        self.lista=[]
        for c in sorted(cursor.fetchall()):
        	self.lista.append(c)

        self.dev_y=0
        try:
           if(produto_run == 0 and len(produtos2) >1 ):
           	for c in range(0,len(produtos2)):
           		del produtos2[0]
           else:
              for c in range(0,len(self.lista)):
                    if(produto_run == 0):
                       produtos2.append(0)
                       mylist.insert(c,f"{produtos2[c]}   {self.lista[c][0]}")
                    if(produto_run == 1):
                    	if(int(produtos2[c]) >0):
                    		mylist.insert(c,f"{produtos2[c]}   {self.lista[c][0]}")
                    		self.dev_y+=1
                    		valor+=int(produtos2[c]) * float(self.lista[c][2])

        except:
        	pass

        mylist.grid(row=1,column=1,columnspan=4,sticky="w",pady=40)

        scrollbar.config( command = mylist.yview )

        tk.Label(self,text="Valor total R$ : ",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=2,column=0,columnspan=2,stick="w")

        data_e_hora_atuais = datetime.now()
        data_e_hora_atuais.strftime("%d/%m/%Y")

        self.e =tk.Entry(self,width=10,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1], textvariable=v(numb_valor(f"{valor:.2f}")))
        self.e.grid(row=2,column=0,columnspan=2,stick="n")

        tk.Label(self,text=f"Dia : {dat_hor()}",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=3,column=0,columnspan=2,stick="w",pady=20)

        tk.Label(self,text="Receber :",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=4,column=0,stick="w")

        self.dia=tk.Spinbox(self,from_=1, to=31,textvariable=v(data_e_hora_atuais.strftime("%d")),width=3,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        self.dia.grid(row=4,column=0,columnspan=5,stick="w",padx=140)

        tk.Label(self,text="/",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=4,column=0,stick="w",columnspan=4,padx=230)

        self.mes=tk.Spinbox(self,from_=1, to=12,textvariable=v(data_e_hora_atuais.strftime("%m")),width=3,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        self.mes.grid(row=4,column=0,columnspan=5,stick="w",padx=250)

        tk.Label(self,text="/",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=4,column=1,stick="w",padx=160,columnspan=4)

        self.ano=tk.Spinbox(self,from_=2020, to=3000, width=4,textvariable=v(data_e_hora_atuais.strftime("%Y")),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        self.ano.grid(row=4,column=1,columnspan=3,stick="w",padx=190)

        self.help=tk.Label(self,text="",fg="red",bg=bg_geral[variavel_comando[0][0]][1])
        self.help.grid(row=6,column=0,columnspan=3,pady=30)
        self.bind_all('<KeyPress>', self.controles)

        tk.Button(self,text="Pagar Agora",relief="flat").grid(row=7,column=0,columnspan=3,pady=30)

    def save(self):
    	global cursor,banco,master2,dados_cliente
    	try:
    		if(self.dev_y >0):
    			if(len(self.dia.get()) == 1):
    				dia = f"0{self.dia.get()}"
    			else:
    				dia = self.dia.get()

    			if(len(self.mes.get()) == 1):
    				mes = f"0{self.mes.get()}"
    			else:
    				mes = self.mes.get()

	    		cursor.execute("UPDATE mais SET devendo = ? ,data_criacao = ? ,data_receber = ?  WHERE id == ?",("true",dat_hor(),str(f"{dia}/{mes}/{self.ano.get()}"),dados_cliente[5],))
	    		cursor.execute("SELECT * FROM mais WHERE id == ?",(dados_cliente[5],))
	    		new_p=cursor.fetchall()
	    		cursor.execute("UPDATE mais SET valor_total =? WHERE id == ?",(num(self.e.get())[0]+new_p[0][4],dados_cliente[5],))
	    		cursor.execute("SELECT * FROM produtos WHERE id == ?",(dados_cliente[5],))
	    		nup=cursor.fetchall()
	    		for c in range(0,len(self.lista)):
	    			try:
	    				cursor.execute(f"UPDATE produtos SET {self.lista[c][1]} = ? WHERE id == ?",(int(produtos2[c]+nup[0][c+1]),dados_cliente[5],))
	    				banco.commit()
	    			except:
	    				pass
    		master2.switch_frame(StartPage)
    	except:
    		self.help["text"]="OCORREU UM ERRO"
    		som_erro()


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])


#  GERA UM FRAME QUE MOSTRA OS CLIENTES PENDENTES
class devendo(tk.Frame):
    def __init__(self, master):
        som_save()
        global dados_cliente,mais_global,init_deven,tds_hj,variavel_comando,tamanho_do_cavas_rolavel

        tamanho_do_cavas_rolavel=1280

        master["bg"]=bg=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])

        master.title("Vendas/Pendentes")
        add_frame(devendo)

        self2=self
        master2=master
        init_deven=1

        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(StartPage)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)

        if(tds_hj == True):
                  tk.Button(self, text="Todas dividas",relief="flat",width=16,bg="gray",
                  command=self.on).grid(row=2,column=0,columnspan=2,stick="w")

                  tk.Button(self, text="Para cobrar",relief="flat",width=16,
                  command=self.off).grid(row=2,column=1,columnspan=2,stick="e")

        if(tds_hj == False):
                  tk.Button(self, text="Todas dividas",relief="flat",width=16,
                  command=self.on).grid(row=2,column=0,columnspan=2,stick="w")

                  tk.Button(self, text="Para cobrar",relief="flat",width=16,bg="gray",
                  command=self.off).grid(row=2,column=1,columnspan=2,stick="e")

#        # LISTBOX

        scrollbar = tk.Scrollbar(self,bg="white")

        self.mylist = tk.Listbox(self,width=32,height=27,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=("arial",10),yscrollcommand = scrollbar.set )

        self.data = run_clientes()
        mais_divida=run_mais()
        self.id_selec=[]
        self.cliente=[]
        try:
           if(tds_hj == True):
	           for c in range(0,len(self.data)):
	           	if(mais_divida[c][1]== "true"):
	           		self.mylist.insert(c,self.data[c][0]+"  de  "+self.data[c][1])
	           		self.id_selec.append(self.data[c][5])
	           		self.cliente.append(self.data[c])

           if(tds_hj == False):
           	for c in range(0,len(self.data)):
	           	if(mais_divida[c][1]== "true"):
	           		if(passagem_tempo(mais_divida[c][3],0) == "true"):
	           			self.mylist.insert(c,self.data[c][0]+"  de  "+self.data[c][1])
	           			self.id_selec.append(self.data[c][5])
	           			self.cliente.append(self.data[c])
        except:
        	pass

        self.mylist.grid(row=3,column=0,columnspan=3,sticky="w")

        scrollbar.config( command = self.mylist.yview )

        self.mylist.bind("<<ListboxSelect>>", self.on_listbox_select)
        self.bind_all('<KeyPress>', self.controles)

    def on_listbox_select(self,event):
            try:
	            global cursor,mais_global,master2
	            i = self.mylist.curselection()[0]
	            text = self.mylist.get(i)
	            self.mylist.insert("end",f"new value : {text} {self.data[i]}")#{self.data[i]}")
	            for k in range(0,6):
	                try:
	                     dados_cliente.insert(k,self.cliente[i][k])
	                except:
	                	 dados_cliente.insert(k,"vazio")
	            cursor.execute("SELECT * FROM mais WHERE id == ?",(self.id_selec[i],))
	            masi=[]
	            for c in cursor.fetchall():
	            	masi.append(c)
	            self.mylist.insert("end",f"{len(masi[0])}")
	            for v in range(0,4):
	            	mais_global.insert(v,masi[0][v])
	            master2.switch_frame(pagar)
            except:
            	pass

    def on(self):
     	global master2 , tds_hj
     	tds_hj = True
     	master2.switch_frame(devendo)

    def off(self):
     	global master2 , tds_hj
     	tds_hj = False
     	master2.switch_frame(devendo)


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])


def passagem_tempo(a,c):
	data_e_hora_atuais = datetime.now()
	data=list(a)
	data_atual=list(data_e_hora_atuais.strftime("%d/%m/%Y"))

	num=[int(data[0]+data[1]),int(data[3]+data[4]),int(data[6]+data[7]+data[8]+data[9])]

	num2=[int(data_atual[0]+data_atual[1]),int(data_atual[3]+data_atual[4]),int(data_atual[6]+data_atual[7]+data_atual[8]+data_atual[9])]

	resp=[num[0]-num2[0],num[1]-num2[1],num[2]-num2[2]]

	if(resp[0] <= c and resp[1] <= 0 and resp[2] <= 0):
		return 'true'

	if(resp[1] < 0 and resp[2] <= 0):
		return 'true'

	if(resp[2] < 0):
		return 'true'

	else:
		return 'false'


# PERMITE O UPDATE DE DADOS DOS CLIENTES
class conf_cliente1(tk.Frame):
    def __init__(self, master):
        som_save()
        global data_cliente , master2,produto_run,variavel_comando,cursor,voltar_para_frame,caminho_imagem_selecionada,up_imag,loc_diretorio,diretorio_pilha,gambiarra

        master.title("Vendas/Up cliente")
        add_frame(conf_cliente1)

        voltar_para_frame=conf_cliente1

        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])

        loc_diretorio=gambiarra
        for ff in range(0,len(diretorio_pilha)):
        	del diretorio_pilha[0]
        diretorio_pilha.append(loc_diretorio)

        produto_run=1
        master2 = master
        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(Encomenda)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="Salvar",command=self.save).grid(row=0,column=2)

        tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        cljpcy=os.getcwd()
        cljpcy+="/imagens/"+mais_global[0]+".jpeg"
        try:
             if(up_imag == False):
             	self.image = Image.open(cljpcy)
             else:
             	self.image = Image.open(caminho_imagem_selecionada)
             self.photo = ImageTk.PhotoImage(self.image.resize((500,500)))
             self.imagem = tk.Button(self,text="teste imagem",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=500,height=500,command=lambda: master.switch_frame(modo_de_procura))
             self.imagem.image = self.photo
             self.imagem.grid(row=2,column=0,columnspan=3)
             #ok=True

        except:
        	self.image = Image.open("imagens/imagem_app/perfil.png")
        	self.photo = ImageTk.PhotoImage(self.image.resize((500,500)))
        	self.imagem = tk.Button(self,text="teste imagem",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=500,height=500,command=lambda: master.switch_frame(modo_de_procura))
        	self.imagem.image = self.photo
        	self.imagem.grid(row=2,column=0,columnspan=3)

        tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=3,column=0)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10, "bold"),text=f"Cliente :").grid(row=4,column=0,columnspan=2,stick="w")

        tk.Label(self,font=('Helvetica', 10, "bold"),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Lugar :").grid(row=5,column=0,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10, "bold"),text=f"Telefone :").grid(row=6,column=0,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10, "bold"),text=f"Bairro :").grid(row=7,column=0,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10, "bold"),text=f"Local :").grid(row=8,column=0,columnspan=2,stick="w")

        self.nome=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10),textvariable=v(dados_cliente[0]))
        self.nome.grid(row=4,column=1,columnspan=2,stick="w")

        self.cidade_final=dados_cliente[1]

        cursor.execute("SELECT * FROM cidades")
        self.nome_cidades=cursor.fetchall()

        self.mb=  tk.Menubutton ( self, text=dados_cliente[1], relief=RAISED,width=21 )

        self.mb.grid(row=5,column=1,stick="w",pady=6,columnspan=2)
        self.mb.menu =  Menu ( self.mb, tearoff = 0 )
        self.mb["menu"] =  self.mb.menu

        self.local_cit = IntVar()

        for fct in range(0,len(self.nome_cidades)):
        	self.mb.menu.add_radiobutton ( label=self.nome_cidades[fct][0],variable=self.local_cit, value=fct,command=self.cidade_selecionada )

        self.telefone=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10),textvariable=v(dados_cliente[2]))
        self.telefone.grid(row=6,column=1,columnspan=2,stick="w")

        self.bairro=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10),textvariable=v(dados_cliente[3]))
        self.bairro.grid(row=7,column=1,columnspan=2,stick="w")

        self.local=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10),textvariable=v(dados_cliente[4]))
        self.local.grid(row=8,column=1,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=9,column=0)

        tk.Button(self,bg="red",text="Excluir Cliente",command=lambda: master.switch_frame(conf_cliente2)).grid(row=10,column=0,columnspan=2)

        self.sec=0
        self.substituir=False

        self.time=tk.Label(self)
        self.bind_all('<KeyPress>', self.controles)


    def cidade_selecionada(self):
    	 self.mb["text"]=self.nome_cidades[self.local_cit.get()][0]
    	 self.cidade_final=self.nome_cidades[self.local_cit.get()][0]


    def save(self):
        global cursor , banco,up_imag,caminho_imagem_selecionada
        cursor.execute("UPDATE clientes SET nome = ? , lugar = ? , telefone = ? , bairro = ? ,local = ? WHERE id == ?",(self.nome.get().title(),self.cidade_final,self.telefone.get(),self.bairro.get(),self.local.get(),dados_cliente[5]))
        if(up_imag):
        	dir=os.getcwd()+'/imagens/'+dados_cliente[5]+".jpeg"
        	tik=os.getcwd()+'/imagens'
        	if(os.path.exists(dir)):
        		os.remove(dir)
        	recortar_imagem.reduzir_tamanho_imagens(caminho_imagem_selecionada, tik,dados_cliente[5],ext='.jpeg')

        up_imag=False
        banco.commit()
        master2.switch_frame(StartPage)

    def controles(self,event):
        global pilha_return,master2,dados_novo_clientes_temporario
        if(event.keysym == "BackSpace"):
        	pass
        else:
         	try:
	         	if(list(self.telefone.get())[0] != "("):
	         		self.telefone.insert(0,"(")
	         	if(list(self.telefone.get())[3] != ")"):
	         		self.telefone.insert(3,")")
	         	if(list(self.telefone.get())[4] != " "):
	         		self.telefone.insert(4," ")
	         	if(list(self.telefone.get())[5] != "9"):
	         		self.telefone.insert(5,"9")
	         	if(list(self.telefone.get())[6] != " "):
	         		self.telefone.insert(6," ")

	         	if(list(self.telefone.get())[11] != " "):
	         		self.telefone.insert(11," ")
	         	if(list(self.telefone.get())[12] != "-"):
	         		self.telefone.insert(12,"-")
	         	if(list(self.telefone.get())[13] != " "):
	         		self.telefone.insert(13," ")
         	except:
	         	pass

        if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	del pilha_return[-1]
    	   	master2.switch_frame(pilha_return[-1])



class conf_cliente2(tk.Frame):
    def __init__(self, master):
        som_save()
        global data_cliente , master2,produto_run,variavel_comando,cursor,voltar_para_frame,caminho_imagem_selecionada,up_imag,loc_diretorio,diretorio_pilha,gambiarra

        voltar_para_frame=conf_cliente2

        master.title("Vendas/Up cliente")
        add_frame(conf_cliente2)

        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])

        loc_diretorio=gambiarra
        for ff in range(0,len(diretorio_pilha)):
        	del diretorio_pilha[0]
        diretorio_pilha.append(loc_diretorio)

        produto_run=1
        master2 = master
        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(Encomenda)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="Salvar",command=self.save).grid(row=0,column=2)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)


        cljpcy=os.getcwd()
        cljpcy+="/imagens/"+mais_global[0]+".jpeg"
        try:
             if(up_imag == False):
             	self.image = Image.open(cljpcy)
             else:
             	self.image = Image.open(caminho_imagem_selecionada)
             self.photo = ImageTk.PhotoImage(self.image.resize((500,500)))
             self.imagem = tk.Button(self,text="teste imagem",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=500,height=500,command=lambda: master.switch_frame(modo_de_procura))
             self.imagem.image = self.photo
             self.imagem.grid(row=2,column=0,columnspan=3)
             #ok=True

        except:
        	self.image = Image.open("imagens/imagem_app/perfil.png")
        	self.photo = ImageTk.PhotoImage(self.image.resize((500,500)))
        	self.imagem = tk.Button(self,text="teste imagem",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=500,height=500,command=lambda: master.switch_frame(modo_de_procura))
        	self.imagem.image = self.photo
        	self.imagem.grid(row=2,column=0,columnspan=3)

        tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=3,column=0)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10, "bold"),text=f"Cliente :").grid(row=4,column=0,columnspan=2,stick="w")

        tk.Label(self,font=('Helvetica', 10, "bold"),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Lugar :").grid(row=5,column=0,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10, "bold"),text=f"Telefone :").grid(row=6,column=0,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10, "bold"),text=f"Bairro :").grid(row=7,column=0,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10, "bold"),text=f"Local :").grid(row=8,column=0,columnspan=2,stick="w")

        self.nome=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10),textvariable=v(dados_cliente[0]))
        self.nome.grid(row=4,column=1,columnspan=2,stick="w")

        #self.lugar=tk.Entry(self,font=('Helvetica', 10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],textvariable=v(dados_cliente[1]))
       # self.lugar.grid(row=3,column=1,columnspan=2,stick="w")

        self.telefone=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10),textvariable=v(dados_cliente[2]))
        self.telefone.grid(row=6,column=1,columnspan=2,stick="w")

        self.bairro=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10),textvariable=v(dados_cliente[3]))
        self.bairro.grid(row=7,column=1,columnspan=2,stick="w")

        self.local=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10),textvariable=v(dados_cliente[4]))
        self.local.grid(row=8,column=1,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=9,column=0)

        self.cidade_final=dados_cliente[1]

        cursor.execute("SELECT * FROM cidades")
        self.nome_cidades=cursor.fetchall()

        self.mb=  tk.Menubutton ( self, text=dados_cliente[1], relief=RAISED,width=21 )

        self.mb.grid(row=5,column=1,stick="w",pady=6,columnspan=2)
        self.mb.menu =  Menu ( self.mb, tearoff = 0 )
        self.mb["menu"] =  self.mb.menu

        self.local_cit = IntVar()

        for fct in range(0,len(self.nome_cidades)):
        	self.mb.menu.add_radiobutton ( label=self.nome_cidades[fct][0],variable=self.local_cit, value=fct,command=self.cidade_selecionada )


        cursor.execute("SELECT * FROM mais WHERE id == ?",(dados_cliente[5],))
        dehe=cursor.fetchall()


        if(dehe[0][1] == "true"):
        	tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1],fg="red",text="⚠ ATENÇÃO ⚠\nEste cliente não pode ser excluido ! ",font=("Arial",10)).grid(row=10,column=0,columnspan=3)
        else:
        	tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1],fg="red",text="⚠ ATENÇÃO ⚠\nVocê deseja mesmo excluilo ?",font=("Arial",10)).grid(row=10,column=0,columnspan=3)
        	tk.Button(self,text="NÃO",bg="light green",command=lambda: master.switch_frame(conf_cliente1)).grid(row=11,column=0,columnspan=2,pady=20)
        	tk.Button(self,text="SIM",bg="red",command=self.excluir).grid(row=11,column=1,columnspan=2,pady=20)

        self.sec=0
        self.substituir=False

        self.time=tk.Label(self)
        self.bind_all('<KeyPress>', self.controles)

    def cidade_selecionada(self):
    	 self.mb["text"]=self.nome_cidades[self.local_cit.get()][0]
    	 self.cidade_final=self.nome_cidades[self.local_cit.get()][0]

    def save(self):
        global cursor , banco,up_imag,caminho_imagem_selecionada
        cursor.execute("UPDATE clientes SET nome = ? , lugar = ? , telefone = ? , bairro = ? ,local = ? WHERE id == ?",(self.nome.get().title(),self.cidade_final,self.telefone.get(),self.bairro.get(),self.local.get(),dados_cliente[5]))
        if(up_imag):
        	dir=os.getcwd()+'/imagens/'+dados_cliente[5]+".jpeg"
        	tik=os.getcwd()+'/imagens'
        	if(os.path.exists(dir)):
        		os.remove(dir)
        	recortar_imagem.reduzir_tamanho_imagens(caminho_imagem_selecionada, tik,dados_cliente[5],ext='.jpeg')

        up_imag=False
        banco.commit()
        master2.switch_frame(StartPage)

    def excluir(self):
        global cursor , banco,dados_cliente
        cursor.execute("DELETE from clientes WHERE nome == ? ",(dados_cliente[0],))
        cursor.execute("DELETE from produtos WHERE id == ? ",(dados_cliente[5],))
        cursor.execute("DELETE from mais WHERE id == ? ",(dados_cliente[5],))
        banco.commit()
        cljpcy=os.getcwd()
        cljpcy+="/imagens/"+mais_global[0]+".jpeg"
        if(os.path.exists(cljpcy)):
        	os.remove(cljpcy)
        master2.switch_frame(StartPage)


    def controles(self,event):
        global pilha_return,master2,dados_novo_clientes_temporario
        if(event.keysym == "BackSpace"):
        	pass
        else:
         	try:
	         	if(list(self.telefone.get())[0] != "("):
	         		self.telefone.insert(0,"(")
	         	if(list(self.telefone.get())[3] != ")"):
	         		self.telefone.insert(3,")")
	         	if(list(self.telefone.get())[4] != " "):
	         		self.telefone.insert(4," ")
	         	if(list(self.telefone.get())[5] != "9"):
	         		self.telefone.insert(5,"9")
	         	if(list(self.telefone.get())[6] != " "):
	         		self.telefone.insert(6," ")

	         	if(list(self.telefone.get())[11] != " "):
	         		self.telefone.insert(11," ")
	         	if(list(self.telefone.get())[12] != "-"):
	         		self.telefone.insert(12,"-")
	         	if(list(self.telefone.get())[13] != " "):
	         		self.telefone.insert(13," ")
         	except:
	         	pass

        if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	del pilha_return[-1]
    	   	master2.switch_frame(pilha_return[-1])



#  SELECIONA OS PRODUTOS  PARA CONFIGURAR
class selecao_produto(tk.Frame):
    def __init__(self, master):
        som_save()
        global master2,variavel_comando
        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master2=master

        master.title("Vendas/Produtos")
        add_frame(selecao_produto)

        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(configuracao)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)

        scrollbar = tk.Scrollbar(self,bg="white")

        self.mylist = tk.Listbox(self,width=32,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],height=29,font=("arial",10),yscrollcommand = scrollbar.set )

        cursor.execute("SELECT * FROM preço")
        self.lista=[]
        for c in sorted(cursor.fetchall()):
        	self.lista.append(c)
        try:
        	for i in range(0,len(self.lista)):
        		self.mylist.insert(i,f"{self.lista[i][0]}")
        except:
        	pass

        self.mylist.grid(row=4,column=0,columnspan=6,sticky="w")

        scrollbar.config( command = self.mylist.yview )

        self.mylist.bind("<<ListboxSelect>>", self.on_listbox_select)
        self.bind_all('<KeyPress>', self.controles)

    def on_listbox_select(self,event):
            try:
            	global cursor,mais_global,selec_produto
            	i = self.mylist.curselection()[0]
            	text = self.mylist.get(i)
            	self.mylist.insert("end",f"new value : {i} {text} {self.lista[i]}")
            	selec_produto=(self.lista[i])
            	master2.switch_frame(conf_produtos1)
            except:
            	pass


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])


class conf_produtos1(tk.Frame):
    def __init__(self, master):
        som_save()
        global data_cliente , master2,produto_run,selec_produto,variavel_comando,voltar_para_frame,caminho_imagem_selecionada,up_imag,loc_diretorio,diretorio_pilha,gambiarra

        voltar_para_frame=conf_produtos1
        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])

        master.title("Vendas/Up produto")
        add_frame(conf_produtos1)

        loc_diretorio=gambiarra
        for ff in range(0,len(diretorio_pilha)):
        	del diretorio_pilha[0]
        diretorio_pilha.append(loc_diretorio)

        master2 = master
        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(selecao_produto)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="Salvar",command=self.save).grid(row=0,column=2)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        cljpcy=os.getcwd()
        cljpcy+="/imagens/"+selec_produto[1]+".jpeg"

        try:
             if(up_imag == False):
             	self.image = Image.open(cljpcy)
             else:
             	self.image = Image.open(caminho_imagem_selecionada)

             self.photo = ImageTk.PhotoImage(self.image.resize((500,500)))
             self.imagem = tk.Button(self,text="teste imagem",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=500,height=500,command=lambda: master.switch_frame(modo_de_procura))
             self.imagem.image = self.photo
             self.imagem.grid(row=2,column=0,columnspan=3)
             #ok=True

        except:
        	tk.Button(self,width=23,height=12,relief="flat",text="",command=lambda: master.switch_frame(modo_de_procura)).grid(row=2,column=0,columnspan=3)
        	ok=False

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=3,column=0)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10, "bold"),text=f"Nome :").grid(row=4,column=0,columnspan=2,stick="w")

        tk.Label(self,font=('Helvetica', 10, "bold"),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Preço :").grid(row=5,column=0,columnspan=2,stick="w")

        self.nome=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10),textvariable=v(selec_produto[0]))
        self.nome.grid(row=4,column=1,columnspan=2,stick="w")

        self.lugar=tk.Entry(self,font=('Helvetica', 10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],textvariable=v(numb_valor(selec_produto[2])))
        self.lugar.grid(row=5,column=1,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=7,column=0)

        self.erro =tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1],fg="red",text="",font=("Arial",10))
        self.erro.grid(row=8,column=0,columnspan=3)

        tk.Button(self,bg="red",text="Excluir Produto",command=lambda: master.switch_frame(conf_produtos2)).grid(row=9,column=0,columnspan=2)
        self.bind_all('<KeyPress>', self.controles)

    def save(self):
        global cursor , banco,up_imag,caminho_imagem_selecionada

        if(self.nome.get().strip() ==""):
        	self.erro["text"]="ERRO O PRODUTO TEM QUE TER NOME"
        	som_erro()
        else:
         	num8=num(self.lugar.get())[0]
         	try:
         		num8=float(num8)
         		cursor.execute("UPDATE preço SET nome = ?, valor = ?  WHERE n_tabela == ?",(self.nome.get().title(),num(self.lugar.get())[0],selec_produto[1]))
         		if(up_imag):
         			dir=os.getcwd()+'/imagens/'+selec_produto[1]+".jpeg"
	         		tik=os.getcwd()+'/imagens'
	         		try:
	         			os.remove(dir)
	         		except:
	         			pass
	         		recortar_imagem.reduzir_tamanho_imagens(caminho_imagem_selecionada, tik,selec_produto[1],ext='.jpeg')
	         		up_imag=False
	         	banco.commit()
         		master2.switch_frame(selecao_produto)
         	except:
         		self.erro["text"]="ERRO O VALOR NÃO VALÍDO !"
         		som_erro()

    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])


class cidade(tk.Frame):
    def __init__(self, master):
        som_save()
        global master2,variavel_comando
        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master2=master

        master.title("Vendas/Cidades")
        add_frame(cidade)

        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(configuracao)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)

        scrollbar = tk.Scrollbar(self,bg="white")

        self.mylist = tk.Listbox(self,width=32,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],height=29,font=("arial",10),yscrollcommand = scrollbar.set )

        cursor.execute("SELECT * FROM cidades")
        self.cit=cursor.fetchall()

        try:
        	for i in range(0,len(self.cit)):
        		self.mylist.insert(i,f"{self.cit[i][0]}")
        except:
        	pass

        self.mylist.grid(row=4,column=0,columnspan=6,sticky="w")

        scrollbar.config( command = self.mylist.yview )

        self.mylist.bind("<<ListboxSelect>>", self.on_listbox_select)
        self.bind_all('<KeyPress>', self.controles)

    def on_listbox_select(self,event):
          #  try:
            	global cursor,mais_global,selec_produto,select_cit
            	i = self.mylist.curselection()[0]
            	text = self.mylist.get(i)
            	#self.mylist.insert("end",f"new value : {i} {text} {self.lista[i]}")
            	select_cit=i
            	master2.switch_frame(data_cidade)
          #  except:
#            	pass

    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])


class data_cidade(tk.Frame):
    def __init__(self, master):
        som_save()
        global master2,variavel_comando,select_cit
        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master2=master

        master.title("Vendas/Vendas da cidade")
        add_frame(data_cidade)

        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(cidade)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)

        scrollbar = tk.Scrollbar(self,bg="white")

        self.mylist = tk.Listbox(self,width=32,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],height=27,font=("arial",10),yscrollcommand = scrollbar.set )

        cursor.execute("SELECT * FROM cidades")
        self.cit=cursor.fetchall()

        tk.Label(self,text=self.cit[select_cit][0],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=("arial",12)).grid(row=4,column=0,columnspan=3,pady=8)

        tk.Button(self,text="<",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=("arial",12)).grid(row=5,column=0,columnspan=3,sticky="w")

        tk.Button(self,text="GERAL",width=17,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=("arial",12)).grid(row=5,column=0,columnspan=3)

        tk.Button(self,text=">",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=("arial",12)).grid(row=5,column=0,columnspan=3,sticky="e")

        cursor.execute("SELECT * FROM preço")
        self.lista=[]
        for c in cursor.fetchall():
        	self.lista.append(c)

      #  try:
        for i in range(0,len(self.lista)):
        	rodando=porcento(self.lista[i][0],randint(0,20),20)
        	self.mylist.insert(i,f"{rodando.preencher_palavra()}{rodando.preencher_quant()} -> {rodando.porcentagem()}%")
        #except:
        #	pass
        vg="testando numero de caracteres  123456"
        self.mylist.insert("end",f"{len(vg)}")
        self.mylist.grid(row=6,column=0,columnspan=6,sticky="w")

        scrollbar.config( command = self.mylist.yview )
        self.bind_all('<KeyPress>', self.controles)

        #self.mylist.bind("<<ListboxSelect>>", self.on_listbox_select)

    #def on_listbox_select(self,event):
#            try:
#            	global cursor,mais_global,selec_produto
#            	i = self.mylist.curselection()[0]
#            	text = self.mylist.get(i)
#            	self.mylist.insert("end",f"new value : {i} {text} {self.lista[i]}")
#            	selec_produto=(self.lista[i])
#            	master2.switch_frame(conf_produtos1)
#            except:
#            	pass
    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])



class porcento:
	def __init__(self,n,qp,tot_prod):
		#n=palavra / qp quantidade de produto /po porcento
		l=len(n)
		self.w = qp
		self.n = n
		self.tot_prod=tot_prod

	def preencher_palavra(self):
		if(len(self.n) < 24):
			#  -24
			o=""
			v=24-len(self.n)
			for gj in range(0,v):
				o+="."

			x =self.n + o
			return x
		if(len(self.n) > 24):
			i=list(self.n)
			np=""
			for fgv in range(0,21):
				np+=i[fgv]
			np+="..."
			return np
		else:
			return np


	def preencher_quant(self):
		o=''
		for gj in range(0,6-len(str(self.w))):
			o+=' '
		o+=str(self.w)
		return o


	def porcentagem(self):
		prc=(100*self.w)/self.tot_prod
		return prc


class conf_produtos2(tk.Frame):
    def __init__(self, master):
        som_save()
        global data_cliente , master2,produto_run,selec_produto,variavel_comando

        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])

        master.title("Vendas/Up produtos")
        add_frame(conf_produtos2)

        master2 = master
        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(selecao_produto)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="Salvar",command=self.save).grid(row=0,column=2)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10, "bold"),text=f"Nome :").grid(row=2,column=0,columnspan=2,stick="w")

        tk.Label(self,font=('Helvetica', 10, "bold"),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=f"Preço :").grid(row=3,column=0,columnspan=2,stick="w")

        self.nome=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 10),textvariable=v(selec_produto[0]))
        self.nome.grid(row=2,column=1,columnspan=2,stick="w")

        self.lugar=tk.Entry(self,font=('Helvetica', 10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],textvariable=v(numb_valor(selec_produto[2])))
        self.lugar.grid(row=3,column=1,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=7,column=0)

        self.erro =tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1],fg="red",text="",font=("Arial black",8))
        self.erro.grid(row=8,column=0,columnspan=3)

        tk.Label(self,bg=bg_geral[variavel_comando[0][0]][1],fg="red",text="⚠ ATENÇÃO ⚠\nVocê deseja mesmo excluilo ?",font=("Arial",10)).grid(row=9,column=0,columnspan=3)

        tk.Button(self,text="NÃO",bg="light green",command=lambda:master.switch_frame(conf_produtos1)).grid(row=10,column=0,columnspan=2,pady=20)

        tk.Button(self,text="SIM",bg="red",command=self.excluir).grid(row=10,column=1,columnspan=2,pady=20)
        self.bind_all('<KeyPress>', self.controles)

    def save(self):
        global cursor , banco

        if(self.nome.get().strip() ==""):
        	self.erro["text"]="ERRO O PRODUTO TEM QUE TER NOME"
        	som_erro()
        else:
         	num8=num(self.lugar.get())[0]
         	try:
         		float(num8)
         		cursor.execute("UPDATE preço SET nome = ?, valor = ?  WHERE n_tabela == ?",(self.nome.get().title(),num8,selec_produto[1]))
         		banco.commit()
         		master2.switch_frame(selecao_produto)
         	except:
         		self.erro["text"]="ERRO O VALOR NÃO VALÍDO !"
         		som_erro()


    def excluir(self):
        global cursor , banco
        novas_colunas=refazer_tabela(selec_produto[1])[1]
        novos_dados_clientes=refazer_tabela(selec_produto[1])[2]
        if(refazer_tabela(selec_produto[1])[0] == True):
        	pass
        	#  DELETA O PRODUTO EM TABLE
        	cursor.execute("DELETE from preço WHERE n_tabela == ? ",(selec_produto[1],))
        	cursor.execute(f"DROP TABLE produtos")
        	banco.commit()
        	#cria a nova tabela
        	cursor.execute("CREATE TABLE produtos(id char )")
        	banco.commit()

        	# readiciona as colunas
        	for new in range(0,len(novas_colunas)-1):
        		cursor.execute(f"ALTER TABLE produtos ADD COLUMN {novas_colunas[new+1]} integer")
        		banco.commit()

        	for new_2 in range(0,len(novos_dados_clientes)):
        		cursor.execute(f"INSERT INTO produtos('id') VALUES (?)",(novos_dados_clientes[new_2][0],))
        		banco.commit()

        	for new_3 in range(0,len(novos_dados_clientes)):
        		for new_sla in range(0,len(novos_dados_clientes[0])-1):
        			cursor.execute(f"UPDATE produtos SET {novas_colunas[new_sla+1]} = {novos_dados_clientes[new_3][new_sla+1]} WHERE id = ?",(novos_dados_clientes[new_3][0],))

        			banco.commit()

        	master2.switch_frame(selecao_produto)
        else:
        	self.erro["text"]="ERRO !\nNÃO É POSSIVEL EXCLUIR ESTE PRODUTO ."
        	som_erro()


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])

#  DÁ OPCOES ADICIONAIS PARA O USUARIO
class configuracao(tk.Frame):
    def __init__(self, master):
        som_save()
        global variavel_comando,master2,caminho_imagem_selecionada,dados_produto_temporario

        dados_produto_temporario=[]
        caminho_imagem_selecionada=''

        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        master2=master
        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(StartPage)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        master.title("Vendas/Configurações")
        add_frame(configuracao)

        tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)
        tk.Label(self,height=3,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        tk.Button(self,width=28,text="Backup").grid(row=2,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Novo Produto",command=lambda:master.switch_frame(novo_produto)).grid(row=3,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Configurar Produto",command=lambda:master.switch_frame(selecao_produto)).grid(row=4,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Sons",command=lambda:master.switch_frame(sons)).grid(row=5,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Tema",command=lambda:master.switch_frame(aparencia)).grid(row=6,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Senha",command=self.ir_senha).grid(row=7,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="Cidades",command=lambda:master.switch_frame(cidade)).grid(row=8,column=0,columnspan=3,pady=20)

        tk.Button(self,width=28,text="SAIR",command=self.sair).grid(row=9,column=0,columnspan=6,pady=20)
        self.bind_all('<KeyPress>', self.controles)

    def sair(self):
         global banco,banco_2
         banco.commit()
         banco.close()

         banco_2.commit()
         banco_2.close()
         exit()


    def ir_senha(self):
         global cursor,banco,master2
         cursor.execute("SELECT * FROM senha")
         dados_senha=cursor.fetchall()

         if(dados_senha[0][0] == "False"):
         	master2.switch_frame(init_senha)
         else:
         	master2.switch_frame(bloqueada)


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if len(pilha_return) == 1 :
    	   		global banco,banco_2
    	   		banco.commit()
    	   		banco.close()
    	   		banco_2.commit()
    	   		banco_2.close()
    	   		exit()
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])


 #  Tela de bloqueio
class bloqueada(tk.Frame):
    def __init__(self, master):
        global data_cliente , banco,cursor,master2,produto_run,selec_produto,variavel_comando,init_play

        self.tempo=0

        master.title("Vendas/Bloqueado !!!")

        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tests=tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])

        master2 = master

        caminho_imagem_fundo='imagens/imagem_app/imagen_fundo_bloqueio.jpeg'
        self.image_2 = Image.open(caminho_imagem_fundo)
        self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
        self.imagem = tk.Label(tests,image = self.photo_2)
        self.imagem.image = self.photo_2
        self.imagem.place(x=0,y=0)


        tk.Label(self,height=10,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=0,column=0)
        tk.Label(tests,text="Senha : ",font=('Helvetica', 9),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).place(x=80,y=390)

        self.senha=tk.Entry(tests,show="•",fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9))
        self.senha.place(x=220,y=390)

        tk.Button(tests,text="Confirmar",command=self.confirmar).place(x=250,y=550)

        self.erro=tk.Label(tests,text="",font=('Helvetica', 9),fg="red",bg=bg_geral[variavel_comando[0][0]][1])
        self.erro.place(x=80,y=480)

        if(init_play == False):
        	tk.Button(tests,text="<- Voltar",relief="flat",font=("'Helvetica'",5),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=lambda:master.switch_frame(configuracao)).place(x=450,y=700)

        tk.Button(tests,text="Esqueceu a senha ?",font=("'Helvetica'",5),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=lambda:master.switch_frame(recuperar)).place(x=60,y=700)

        self.bind_all('<KeyPress>', self.controles)


    def confirmar(self):
           from time import sleep
           global data_cliente , banco,cursor,master2,produto_run,selec_produto,variavel_comando,init_play

           cursor.execute("SELECT * FROM senha")
           dados_senha=cursor.fetchall()

           if(self.senha.get() != dados_senha[0][1]):
           	som_erro_2()
           	self.erro["text"]="ERRO : Senha incorreta !"
           	self.senha['textvariable']=v("")
           	self.tempo+=1
           	#if(self.tempo >= 10):
#           	     for c in range(5,0,-1):
#           	     	self.erro["text"]=f"ERRO : Senha incorreta \ntente novamente em {c}"
#           	     	sleep(1)
           else:
           	if(init_play):
           		init_play = False
           		master2.switch_frame(StartPage)
           	else:
           		master2.switch_frame(init_senha)
    def  controles(self,event):
    	if event.keysym == 'Return':
    	   	self.confirmar()

class recuperar(tk.Frame):
    def __init__(self, master):
        global data_cliente , banco,cursor,master2,produto_run,selec_produto,variavel_comando

        self.tempo=0

        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])

        master.title("Vendas/Bloqueado !!!")

        master2 = master
        tk.Label(self,height=10,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=0,column=0)
        tk.Label(self,text="Senha de recuperação : ",font=('Helvetica', 8),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        self.senha=tk.Entry(self,fg=bg_geral[variavel_comando[0][0]][0],show="•",bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9))
        self.senha.grid(row=1,column=1,columnspan=2,stick="w")

        tk.Button(self,text="Confirmar",command=self.confirmar).grid(row=2,column=1,pady=20)

        tk.Button(self,text="<- Voltar",font=("'Helvetica'",5),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=lambda:master.switch_frame(bloqueada)).grid(row=4,column=1,pady=20)


        self.erro=tk.Label(self,text="",font=('Helvetica', 9),fg="red",bg=bg_geral[variavel_comando[0][0]][1])
        self.erro.grid(row=3,column=0,columnspan=2)

        tk.Button(self,text="Pedir senha ao desenvolvedor",font=("'Helvetica'",5),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=4,column=0,pady=20)

        self.bind_all('<KeyPress>', self.controles)

    def confirmar(self):
           from time import sleep
           global data_cliente , banco,cursor,master2,produto_run,selec_produto,variavel_comando

           cursor.execute("SELECT * FROM senha")
           dados_senha=cursor.fetchall()

           if(self.senha.get() != dados_senha[0][2]):
           	som_erro_2()
           	self.erro["text"]="ERRO : Senha incorreta !"
           	self.senha['textvariable']=v("")
           	#self.tempo+=1
           	#if(self.tempo >= 10):
#           	     for c in range(5,0,-1):
#           	     	self.erro["text"]=f"ERRO : Senha incorreta \ntente novamente em {c}"
#           	     	sleep(1)
           else:
           	master2.switch_frame(init_senha)

    def  controles(self,event):
    	if event.keysym == 'Return':
    	   	self.confirmar()


class init_senha(tk.Frame):
    def __init__(self, master):
        som_save()
        global data_cliente , banco,cursor,master2,produto_run,selec_produto,variavel_comando

        master.title("Vendas/Senha")

        cursor.execute("SELECT * FROM senha")
        dados_senha=cursor.fetchall()

        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])

        master2 = master
        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(configuracao)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="Salvar",command=self.save).grid(row=0,column=2)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9),text=f"Nome :").grid(row=2,column=0,columnspan=2,stick="w")

        self.nome=tk.Entry(self,text=v(dados_senha[0][5]),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9))
        self.nome.grid(row=2,column=1,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9),text=f"Gmail :").grid(row=3,column=0,columnspan=2,stick="w")

        self.gmail=tk.Entry(self,text=v(dados_senha[0][4]),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9))
        self.gmail.grid(row=3,column=1,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9),text=f"Senha :").grid(row=4,column=0,columnspan=2,stick="w")

        self.senha=tk.Entry(self,show="•",text=v(dados_senha[0][1]),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9))
        self.senha.grid(row=4,column=1,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9),text=f"Confirmar senha :").grid(row=5,column=0,columnspan=2,stick="w")

        self.confirmar=tk.Entry(self,show="•",text=v(dados_senha[0][1]),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9))
        self.confirmar.grid(row=6,column=1,columnspan=2,stick="w")

        tk.Label(self,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9),text=f"Senha de recuperação :").grid(row=7,column=0,columnspan=2,stick="w")

        self.recuperar=tk.Entry(self,show="•",text=v(dados_senha[0][2]),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9))
        self.recuperar.grid(row=8,column=1,columnspan=2,stick="w")

        self.erro=tk.Label(self,fg="red",bg=bg_geral[variavel_comando[0][0]][1],font=('Helvetica', 9),text=f"")
        self.erro.grid(row=9,column=0,columnspan=3,stick="w")

        if(dados_senha[0][0] == 'True'):
	        tk.Button(self,text="Ativada",command=self.ativar).grid(row=10,column=0,columnspan=3,stick="w",padx=70)

	        tk.Button(self,text="Desativada",bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],command=self.ativar).grid(row=10,column=1,columnspan=3)

        else:
	        tk.Button(self,text="Ativada",bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],command=self.ativar).grid(row=10,column=0,columnspan=3,stick="w",padx=70)

	        tk.Button(self,text="Desativada",command=self.ativar).grid(row=10,column=1,columnspan=3)

    def ativar(self):
    	global banco,cursor,master2

    	cursor.execute("SELECT * FROM senha")
    	dados_senha=cursor.fetchall()

    	if(dados_senha[0][0] == "True"):
        	cursor.execute(f"UPDATE senha SET pw_active = ?",("False",))

    	else:
        	cursor.execute(f"UPDATE senha SET pw_active = ?",("True",))

    	banco.commit()
    	master2.switch_frame(init_senha)


    def save(self):
         global banco,cursor,master2
         self.erro["text"]=""
         while True:
	         if(self.nome.get().strip() == ""):
	         	self.erro["text"]="ERRO : o nome não pode ser nulo"
	         	som_erro_2()
	         	break
	         if(self.gmail.get().strip() == ""):
	         	self.erro["text"]="ERRO : o gmail não pode ser nulo"
	         	som_erro_2()
	         	break
	         if(self.senha.get().strip() == ""):
	         	self.erro["text"]="ERRO : a senha não pode ser nula"
	         	som_erro_2()
	         	break

	         if(len(self.senha.get()) <=3):
	         	self.erro["text"]="ERRO : a senha tem que ter no minino 4 caracteres"
	         	som_erro_2()
	         	break

	         if(self.senha.get() != self.confirmar.get()):
	         	self.erro["text"]="ERRO : a senha incompativel"
	         	som_erro_2()
	         	break

	         if(self.recuperar.get().strip() == ""):
	         	self.erro["text"]="ERRO : a senha de recuperação não pode ser nula"
	         	som_erro_2()
	         	break

	         if(len(self.recuperar.get()) <=3):
	         	self.erro["text"]="ERRO : a senha de recuperação tem que ter no minino 4 caracteres"
	         	som_erro_2()
	         	break

	         else:
	         	break

         cursor.execute("SELECT * FROM senha")
         dados_senha=cursor.fetchall()

         cursor.execute(f"UPDATE senha SET pw_active = ?,pw = ? ,pw_2 = ?, recuperar_conexao = ?, gmail = ? ,nome =?",("True",self.senha.get(),self.recuperar.get(),"criptografia",self.gmail.get(),self.nome.get(),))

         banco.commit()

         master2.switch_frame(configuracao)


class aparencia(tk.Frame):
	def __init__(self, master):
		som_save()
		global variavel_comando ,bg_geral,master2

		master.title("Vendas/Temas")
		add_frame(aparencia)

		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		master2=master

		tk.Button(self, text="<- voltar",relief="flat",command=lambda: master.switch_frame(configuracao)).grid(row=0,column=0)

		tk.Button(self,relief="flat",width=18).grid(row=0,column=1)
		tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)
		tk.Label(self,height=3,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

		self.var = IntVar()

		self.b=tk.Radiobutton(self,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text="Branco",font=('arial', 8), variable=self.var, value=0,command=self.salvar)
		self.b.grid(row=1,column=1,stick="w",columnspan=2)

		self.p=tk.Radiobutton(self,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text="Preto",font=('arial', 8), variable=self.var, value=1,command=self.salvar)
		self.p.grid(row=2,column=1,stick="w",columnspan=2)

		self.q=tk.Radiobutton(self,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text="Cinza",font=('arial', 8), variable=self.var, value=2,command=self.salvar)
		self.q.grid(row=3,column=1,pady=30,stick="w",columnspan=2)

		self.k=tk.Radiobutton(self,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text="Temporario",font=('arial', 8), variable=self.var, value=3,command=self.salvar)
		self.k.grid(row=4,column=1,stick="w",columnspan=2)

		#self.pers=tk.Radiobutton(self,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][44
	#	],font=('arial', 8), variable=self.var, value=4,command=self.salvar)
		#self.pers.grid(row=5,column=1,pady=30,stick="w",columnspan=2)

		if(variavel_comando[0][0] == 0):
			self.b.select()
		if(variavel_comando[0][0] == 1):
			self.p.select()
		if(variavel_comando[0][0] == 2):
			self.q.select()
		if(variavel_comando[0][0] == 3):
			self.k.select()
		#if(variavel_comando[0][0] == 4):
			#self.pers.select()
		self.bind_all('<KeyPress>', self.controles)

	def salvar(self):
		global cursor_2 , banco_2,variavel_comando,master2
		cursor_2.execute(f"UPDATE dados SET bg = ? ",(self.var.get(),))

		banco_2.commit()
		cursor_2.execute("SELECT * FROM dados")
		variavel_comando=cursor_2.fetchall()
		#som_save()
		master2.switch_frame(aparencia)


	def controles(self,event):
	   global pilha_return,master2
	   if event.keysym == 'Break' or event.keysym == 'Escape':
	   	 if(len(pilha_return) == 1) :
	   	   	master2.switch_frame(configuracao)
	   	 else:
	   	   	del pilha_return[-1]
	   	   	master2.switch_frame(pilha_return[-1])


class novo_produto(tk.Frame):
    def __init__(self, master):
        som_save()
        global banco , cursor,variavel_comando,caminho_imagem_selecionada,voltar_para_frame,up_imag,dados_produto_temporario,master2

        master2=master

        voltar_para_frame=novo_produto

        master.title("Vendas/Novo produtos")
        add_frame(novo_produto)

        master["bg"]=bg_geral[variavel_comando[0][0]][1]
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
        tk.Button(self, text="<- voltar",relief="flat",
                  command=lambda: master.switch_frame(configuracao)).grid(row=0,column=0)

        tk.Button(self,relief="flat",width=18).grid(row=0,column=1)

        tk.Button(self,relief="flat", text="Salvar",command=self.salvar).grid(row=0,column=2)

        tk.Label(self,height=1,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

        try:
             if(up_imag == False):
             	self.image = Image.open(cljpcy)
             else:
             	self.image = Image.open(caminho_imagem_selecionada)

             self.photo = ImageTk.PhotoImage(self.image.resize((500,500)))
             self.imagem = tk.Button(self,text="teste imagem",image = self.photo,bg=bg_geral[variavel_comando[0][0]][1],width=500,height=500,command=self.save_temporario)
             self.imagem.image = self.photo
             self.imagem.grid(row=2,column=0,columnspan=3)
             #ok=True

        except:
        	tk.Button(self,width=23,height=12,relief="flat",text="",command=self.save_temporario).grid(row=2,column=0,columnspan=3)
        	ok=False

        tk.Label(self,height=1,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=3,column=0)

        tk.Label(self,text="Nome :",font=("arial",10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=4,column=0)


        tk.Label(self,text="Preço : ",font=("arial",10),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).grid(row=5,column=0,pady=10)

        if(len(dados_produto_temporario) > 0):
        	self.nome=tk.Entry(self,font=("arial",10),width=12,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],textvariable=v(dados_produto_temporario[0]))
        	self.nome.grid(row=4,column=1,stick="w")

        	self.preco=tk.Entry(self,font=("arial",10),width=12,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],textvariable=v(dados_produto_temporario[1]))
        	self.preco.grid(row=5,column=1,stick="w",pady=10)

        else:
        	self.nome=tk.Entry(self,font=("arial",10),width=12,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        	self.nome.grid(row=4,column=1,stick="w")

        	self.preco=tk.Entry(self,font=("arial",10),width=12,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
        	self.preco.grid(row=5,column=1,stick="w",pady=10)

        self.lab=tk.Label(self,text="",fg="red",bg=bg_geral[variavel_comando[0][0]][1],font=("arial black",10))
        self.lab.grid(row=6,column=0,columnspan=3,pady=50)
        self.bind_all('<KeyPress>', self.controles)

    def salvar(self):
        	nm=str(self.nome.get()).strip()
        	if(num(self.preco.get())[1] == "true"):
        		if(nm != ""):
        			cursor.execute("SELECT * FROM preço")
        			gjc=cursor.fetchall()
        			bdndk=[]
        			for kfl in range(0,len(gjc)):
        				bdndk.append(gjc[kfl][0])
        			if(nm.title() in bdndk):
        				self.lab["text"]="ERRO O PRODUTO JÁ EXISTE"
        				som_erro()
        			else:
	        			try:
	        				cursor.execute(f"INSERT INTO preço('nome','n_tabela',valor) VALUES (?,?,?)",(nm.title(),transformar(nm),num(self.preco.get())[0]))
	        				cursor.execute(f"ALTER TABLE produtos ADD COLUMN {transformar(self.nome.get())} integer")
	        				cursor.execute(f"ALTER TABLE cidades  ADD COLUMN {transformar(self.nome.get())} integer")

	        			except:
	        				self.lab["text"]="OPS OCORREU UM ERRO"
	        				som_erro()

	        			else:
	        				banco.commit()
	        				produto_mais(transformar(nm))
	        				master2.switch_frame(configuracao)
        		else:
        			self.lab["text"]="ERRO O PRODUTO TEM QUE TER NOME"
        			som_erro()

        	else:
        	 	self.lab["text"]="ERRO O PREÇO NÃO VALIDO"
        	 	som_erro()

    def save_temporario(self):
    	global dados_produto_temporario,master2
    	dados_produto_temporario=[self.nome.get(),self.preco.get()]

    	master2.switch_frame(modo_de_procura)


    def controles(self,event):
    	global pilha_return,master2
    	if event.keysym == 'Break' or event.keysym == 'Escape':
    	   	if(len(pilha_return) == 1) :
    	   		master2.switch_frame(configuracao)
    	   	else:
    	   		del pilha_return[-1]
    	   		master2.switch_frame(pilha_return[-1])


def produto_mais(o):
	global banco,cursor
	clientes=run_clientes()
	for c in range(0,len(clientes)):
		cursor.execute(f"UPDATE produtos SET {o} = 0 WHERE id = ?",(clientes[c][5],))
		banco.commit()

#  ADAPITA PARA STR COLUNA
def transformar(o):
        novo = o.replace(" ","_").strip()
        return novo


# TRANSFORMA EM VALOR REAL
def num(o):
        t=[]
        i=str(o).replace(",",".")
        kl=list(i)
        i=""
        for c in range(0,len(kl)):
        	if(kl[c] != " "):
        		i+=kl[c]
        try:
        	p=float(i)
        except:
        	t.append(i)
        	t.append("false")
        	return t
        else:
        	t.append(float(i))
        	t.append("true")
        	return t


def refazer_tabela(p):
        global cursor,banco
        retorno=[]

        cursor.execute("SELECT * FROM produtos")
        dados_cliente_safe=cursor.fetchall()
        cursor.execute('PRAGMA table_info(produtos)')
        colunas = [tupla[1] for tupla in cursor.fetchall()]

        deletar=True

        try:
         	for v in range(0,len(dados_cliente_safe)):
         		re=[]
         		for g in range(0,len(dados_cliente_safe[v])):
         			re.append(dados_cliente_safe[v][g])
         		try:
         			if(int(re[colunas.index(p)]) >= 1):
         				deletar=False
         		except:
         			pass
         		del re[colunas.index(p)]
         		dados_cliente_safe[v]=re
        except:
         	pass
        retorno.append(deletar)
        del colunas[colunas.index(p)]
        retorno.append(colunas)
        retorno.append(dados_cliente_safe)
        return retorno

class sons(tk.Frame):
	def __init__(self, master):
		som_save()
		global variavel_comando ,bg_geral ,idiom,master2

		master.title("Vendas/Sons")
		add_frame(sons)

		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])

		master2=master
		tk.Button(self, text="<- Voltar",relief="flat",command=lambda: master.switch_frame(configuracao)).grid(row=0,column=0)

		tk.Button(self,relief="flat",width=18).grid(row=0,column=1)
		tk.Button(self,relief="flat", text="        ").grid(row=0,column=2)
		tk.Label(self,height=3,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)

		self.var_1 = StringVar()
		self.var_2= StringVar()
		self.var_3= StringVar()

		port=tk.Checkbutton(self,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text="Toque",font=('arial', 8), variable=self.var_1, onvalue = "True", offvalue = "False",command=self.salvar)#,command=sel)
		port.grid(row=1,column=1,stick="w",columnspan=2)

		ingl=tk.Checkbutton(self,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2], text="Erro",font=('arial', 8), variable=self.var_2,  onvalue = "True", offvalue = "False",command=self.salvar)#,command=sel)
		ingl.grid(row=2,column=1,stick="w",columnspan=2)

		espanhol=tk.Checkbutton(self,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2],text="Resultado",font=('arial', 8), variable=self.var_3,  onvalue = "True", offvalue = "False",command=self.salvar)#,command=sel)
		espanhol.grid(row=3,column=1,stick="w",columnspan=2,pady=20)


		cursor_2.execute("SELECT * FROM sons")
		vshjej=cursor_2.fetchall()

		if(vshjej[0][0] == "True"):
			port.select()
		if(vshjej[0][1] == "True"):
			ingl.select()
		if(vshjej[0][2] == "True"):
			espanhol.select()
		self.bind_all('<KeyPress>', self.controles)
#		if(vshjej[0][1] == True):
#			fraces.select()


	def salvar(self):
		global cursor_2 , banco_2,variavel_comando,master2
		cursor_2.execute(f"UPDATE sons SET toque = ? ,erro = ?,resultado = ?",(self.var_1.get(),self.var_2.get(),self.var_3.get(),))

		banco_2.commit()
		cursor_2.execute("SELECT * FROM dados")
		variavel_comando=cursor_2.fetchall()
		som_save()
		master2.switch_frame(sons)


	def controles(self,event):
	   global pilha_return,master2
	   if event.keysym == 'Break' or event.keysym == 'Escape':
	   	 if(len(pilha_return) == 1) :
	   	   	master2.switch_frame(configuracao)
	   	 else:
	   	   	del pilha_return[-1]
	   	   	master2.switch_frame(pilha_return[-1])


def som_erro():
	cursor_2.execute("SELECT * FROM sons")
	vshjej=cursor_2.fetchall()
	if(vshjej[0][1] == "True"):
		pygame.init()
		pygame.mixer.music.load('sons/erro.mp3')
		pygame.mixer.music.play()
		pygame.event.wait()


def som_erro_2():
	cursor_2.execute("SELECT * FROM sons")
	vshjej=cursor_2.fetchall()
	if(vshjej[0][1] == "True"):
		pygame.init()
		pygame.mixer.music.load('sons/erro.mp3')
		pygame.mixer.music.play()
		pygame.event.wait()


def som_save():
	cursor_2.execute("SELECT * FROM sons")
	vshjej=cursor_2.fetchall()
	if(vshjej[0][0] == "True"):
		pygame.init()
		pygame.mixer.music.load('sons/som_save.mp3')
		pygame.mixer.music.play()
		pygame.event.wait()


if __name__ == "__main__":

    app = SampleApp()
    app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}")
    app.title("Vendas")
    app.mainloop()
