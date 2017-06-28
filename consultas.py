
 

def consultas(bd_candidatos):
	cabecalho = "\n **** Consultas e Estatisticas **** \n"
	menu_consulta = " 1 - Busca por parte do nome  \n 2 - Listar Todos os candidatos dado uma sigla \n"\
	" 3 - Quantidade e porcentagem de candidatos por sexo \n 4 - Buscar candidatos pelo seu numero \n"\
	"\n 0 - Voltar \n opcao >>> "

	while True:
		opcao = input(cabecalho + menu_consulta)

		if opcao == 0:
			return
		elif opcao == 1:
			buscar_por_nome_do_candidato(bd_candidatos)			
		elif opcao == 2:
			listar_candidatos_sigla(bd_candidatos)
		elif opcao == 3:
			quantidade_perc_sexo(bd_candidatos)
		elif opcao == 4:
			buscar_numero(bd_candidatos)
		else:
			print 'Opcao invalida.'



def buscar_por_nome_do_candidato(bd_candidatos):
	parte_nome = raw_input('Nome do candidato: ')

	for candidato in bd_candidatos:
		if parte_nome.upper() in candidato['Nome do candidato na urna'].upper():
			print candidato
def listar_candidatos_sigla(bd_candidatos):
	cont = 0
	print 'candidatos Cadastrados (%d)' % len(bd_candidatos)
	sigla = raw_input("Sigla: ")
	for i in bd_candidatos:
		if sigla.upper() in  i["Sigla do Partido"].upper():
			print i
			cont+=1
	if cont == 0:
		print"nao existe candidato"			

def quantidade_perc_sexo(bd_candidatos):
	qtd_masculino  = 0 # contador
	qtd_feminino = 0
	percentual = 0

	for i in range(len(bd_candidatos)):
		if bd_candidatos[i]["Sexo"] == 'M':
			qtd_masculino += 1
		else:
			qtd_feminino += 1	
	
	
	total  = qtd_masculino+qtd_feminino
	
	percentual_masculino = (qtd_masculino/float(total))*100
	
	percentual_feminino = (qtd_feminino/float(total))*100
	
	print"Quantidade:Masculino >> %d ee Feminino ->> %d"%(qtd_masculino,qtd_feminino)
	print"Percentual(Masc): %.2f"%percentual_masculino
	print"Percentual(FEMIN): %.2f"%percentual_feminino


	 	
def buscar_numero(bd_candidatos):
	
	print 'candidatos Cadastrados (%d)' % len(bd_candidatos)
	
	numero_desejado = int(input("Numero: "))

	for i in bd_candidatos:
		if numero_desejado == i["Numero"]:
			print i


