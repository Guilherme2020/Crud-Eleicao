from consultas import consultas

def main():
	cabecalho = '\n   ****** SIS - ELEICAO  ***** \n\n'
	menu =  ''' 1 - Adicionar candidatos \n 2 - Listar por ordem de cadastro \n 3 - Remover candidatos
	\n4 - Consultas  \n 0 - Sair \n\n opcao >>> '''
	bd_candidatos = inicializar()	

	while(True):
		opcao = input(cabecalho + menu)

		if opcao == 0:
			finalizar(bd_candidatos)
			break
		elif opcao == 1:
			candidato = adicionar_candidato()
			bd_candidatos.append(candidato)
			print 'candidato cadastrado com sucesso!'	

			
		elif opcao == 2:
			listar_candidatos(bd_candidatos)
		elif opcao == 3:
			remover_candidatos(bd_candidatos)
		elif opcao == 4:
			consultas(bd_candidatos)
		else:
			print "Opcao invalida"


def inicializar():
	arquivo_candidato = open('arquivos/eleicao.txt','r')
	linhas = arquivo_candidato.readlines()
	candidatos = []
	for linha in linhas:
		candidatos.append(eval(linha))
	arquivo_candidato.close()

	return candidatos
def finalizar(lista):
	arquivo = open('arquivos/eleicao.txt', 'w')
	
	for candidato in lista:
		arquivo.write(str(candidato) + '\n')
	arquivo.close()

def adicionar_candidato():
	nome_urna = raw_input('Nome do candidato na urna:  ')
	sexo = raw_input('Sexo M-F: ')
	numero = int(input("Numero: "))
	sigla_partido = raw_input("Sigla:")
	cargo  = raw_input("Vereador|Prefeito: ")
	
	dicio =  {"Nome do candidato na urna":nome_urna,
	"Sexo":sexo,"Numero":numero,"Sigla do Partido":sigla_partido,
	"Cargo":cargo
	}

	return dicio

def listar_candidatos(bd_candidatos):
	print 'Candidatos Cadastrados (%d)' % len(bd_candidatos)
	#for item in bd_alunos:
	#	print item['nome'], item['idade'], item['sexo']
	for i in range(len(bd_candidatos)):
		print i, bd_candidatos[i]['Nome do candidato na urna'], bd_candidatos[i]['Sexo'], bd_candidatos[i]['Numero'],bd_candidatos[i]['Sigla do Partido'],bd_candidatos[i]['Cargo']

def remover_candidatos(bd_candidatos):
	listar_candidatos(bd_candidatos)
	posicao = input('Qual indice? ')
	removido = bd_candidatos.pop(posicao)
	print 'Candidato: ', removido['Nome do candidato na urna'], ' removido.'


if __name__ == '__main__':
	main()	