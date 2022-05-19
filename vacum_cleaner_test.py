import copy

# A matriz representa o pisos
# Os 1 são as paredes e 0 os caminhos possiveis e o s representa a sujeira
m=[[0,1,2,1,0,0,0,0],
   [0,1,2,1,0,1,1,0],
   [0,0,0,0,0,1,1,0],]

inicio=(0,0) # Marca o inicio
fim   =(2,7) # Marco o fim

# A função pisos em volta explora todos os pisos da matriz em volta de um piso.
# Por isso ele deve retorna todos os possiveis posições

def pisosEmVolta(piso, matriz):                          # salvando as posições possiveis em volta do piso atual
   pisos=[]                                             # inicializando lista de pisos
   x,y=piso                                             # extraindo posição do piso atual
   xm=len(matriz)                                       # extraindo dimensão da matriz
   ym=len(matriz[0])                                    # extraindo dimensão da matriz
   if(x+1 <xm and matriz[x+1][y]!=1):                   # se m[x+1][y] for possivel
      pisos.append((x+1,y))                             # então adicione a posição na lista de piso em volta
   if(y+1 <ym and matriz[x][y+1]!=1):                   # se m[x][y+1] for possivel
      pisos.append((x,y+1))                             # então adicione a posição na lista de piso em volta
   if(x-1 >=0 and matriz[x-1][y]!=1):                   # se m[x-1][y] for possivel
      pisos.append((x-1,y))                             # então adicione a posição na lista de piso em volta
   if(y-1 >= 0 and matriz[x][y-1]!=1):                  # se m[x][y-1] for possivel
      pisos.append((x,y-1))                             # então adicione a posição na lista de piso em volta
   return pisos                                         # retornar pisos possiveis

# A função paraString, é usado dentro da função busca_em_largura()
# com o objetivo de retornar string para ser utilizada como indice.
def paraString(proximopiso):
   return f'{proximopiso[0]}, {proximopiso[1]}'

def limpar_piso(piso):
    pass

def piso_sujo(piso, matriz):
    pass


def busca_em_largura(inicio, fim, matriz):
   counter  = 0                                        # contador somente para visualizar o numero de passos
   fila     = [inicio]                                 # fila com a posição inicial
   visitados= [inicio]                                 # fila de visitados incluindo a posição inicial

   caminhos = dict()                                    # dicionario para salvar o caminho final

   while(len(fila)>0):                                 # A condição de parada
      print(f'O que tem na fila: {fila}')
      piso=fila[0]                                     # escolhendo o piso da fila como piso atual
      print("Piso explorado:", piso)
      del fila[0]                                      # deletando o piso da fila para não repetir
      pisos_em_volta = pisosEmVolta(piso, matriz)
      print(f'Pisos possiveis em volta do piso na fila: {pisos_em_volta} ')

      for proximopiso in pisos_em_volta:               # um laço que percorre por todas as posições em volta
                                                       # [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
         pintarMatriz(matriz,piso,'x')                 # função de printar com o caracter x os pisos visitados
         if proximopiso not in visitados:              # se o proximo piso não estiver na lista de visitados

            visitados.append(proximopiso)              # adicione ele na lista de visitados

            caminhos[paraString(proximopiso)] = piso   # adicione no dicionario de caminhos,onde o proximo piso vai
                                                       # ser um indice para o piso anterior
            print(f'Caminho: {caminhos}')

            if proximopiso == fim:
                                                       # se o proximo piso for o final,então encontrou. exemplo (2,2)==(2,2)
               caminho=[]                              # inicializa fila caminho
               passo=proximopiso                       # adiciona o proximopiso em um passo do caminho
               pintarMatriz(matriz,passo,'FIM')
               print(f'PRITANDO A SOLUÇÃO ENCONTRADA!')
               #pintarMatriz(matriz,passo,'s')
               while(passo!=inicio):                   # percorre passo a passo do final até o inicio
                  caminho.append(passo)                # adiciona passo na lista de caminho
                  passo=caminhos[paraString(passo)]    # adiciona o proximo passo, baseando se no indice de caminhos definidos
                  # print("Modo Reverso",end='\n\n')     #
                  #pintarMatriz(matriz,passo,'s')       # printar a solução com 's',passo a passo em modo reverso,
               caminho.append(inicio)                  # adicionando a posição inicial no caminho
               caminho.reverse()                       # revertendo a lista
               return caminho                          # retorna lista do caminho encontrado
            else:                                      # se não for o final
               fila.append(proximopiso)                # adicione o proximo piso na lista de pisos a serem percorridos
            print(f"Passo {counter}")
            counter+=1                                 # somando no contador de passos do algoritmo
   return "Caminho não encontrado"                     # retorne uma string caso não encontre

def pintarMatriz(matriz, passo, caminho):
   x, y = passo                        # extraindo posição do piso atual
   xm=len(matriz)                      # extraindo dimensão da matriz
   ym=len(matriz[0])                   # extraindo dimensão da matriz
   m2=matriz.copy()                    # copiando a matriz para uma auxiliar
   m2[x][y]=caminho                    # pintando matriz com o caracter escolhido


   for i in range (0,xm):
      for j in range (0,ym):
         print(m2[i][j],end=' ')       # printando a matriz pintada
      print()
   print()


caminho = busca_em_largura(inicio,fim,m)

print(f"Caminho Encontrado: {caminho}")
