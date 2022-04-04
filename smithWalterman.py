import numpy as np

def smithWalterman():     
    #atruindo valores as sequencias             
    sequencia1 = 'ATCGTCTTTA'
    sequencia2 = 'GTCGTCATTT'

    #definindo tamanho da matriz e da espelho
    linhas = len(sequencia2)+1
    colunas = len(sequencia1)+1

    matriz = np.zeros((linhas,colunas), dtype=np.float64)
    espelho = []


    #atribuindo valores iniciais
    gap=-2
    match=1
    mismatch=-1
    esquerda = topo = diagonal = valor = score = 0

    
    #valida se a sequencia esta correta    
    def validaSequencia(sequencia):
        for i in range(len(sequencia)):
            if sequencia[i] not in ['A', 'T', 'C', 'G']:                
                return False
            
        return True

       

    #para calcular o valor diagonal é avaliado se os caracters são iguais
    #se forem MATCH senão MISMATCH
    def match(letra1,letra2):
            if(letra1 == letra2):
                return True
            else:
                False
    #preenchendo a matriz com os valor de scores
    def preencheMatriz():
        for i in range(1,linhas):      
            for j in range (1,colunas):
                if(match(sequencia1[j-1],sequencia2[i-1]) == True):
                    valor = match
                else:
                    valor = mismatch
                    
                diagonal = matriz[i-1][j-1] + valor
                topo = matriz[i-1][j] + gap
                esquerda = matriz[i][j-1] + gap

                matriz[i][j] = max(diagonal,topo,esquerda)
                preencheEspelho(i,j)

    #preenchendo a matriz espelho com os valor de scores                
    def preencheEspelho(i,j):
        #recebe o maior numero e escreve de onde é
        num = max(diagonal,topo,esquerda)
        
        if(num == diagonal):
            espelho[i-1][j-1] = "diagonal"
        elif(num==topo):
            espelho[i-1][j-1] = "topo"
        elif(num==esquerda):    
            espelho[i-1][j-1] = "esquerda"

    #faz o caminho de volta a partir do maior valor da matriz para
    #construir o alinhamento local
    def backtrace():
        sequencia = []
        coluna = colunas-1
        linha = 0
        
        for i  in range(linhas):
            if score <= matriz[i][coluna]:
                pontuacao = matriz[i][coluna]
                linha = i

        linha-= 1
        coluna-= 1

        while(True):
            
            if(espelho[linha][coluna]=="diagonal"):
                sequencia[0]+=sequencia2[coluna]
                sequencia[1]+=sequencia1[linha]
                linha-=1
                coluna-=1
            
            elif(espelho[linha][coluna]=="topo"):
                sequencia[0]+=sequencia2[coluna]
                sequencia[1]+='-'
                coluna-=1
            
            elif(espelho[linha][coluna]=="diagonal"):    
                sequencia[0]+='-'
                sequencia[1]+=sequencia1[linha]
                linha-=1

            if((not linha and not coluna) or (not espelho[linha][coluna])):
                break                    

        sequencia[0]=inverte(sequencia[0])
        sequencia[1]=inverte(sequencia[1])

        return sequencia

    #inverte a o alinhamento local obtido
    def inverte(sequencia):
        str=""               

        for i in range(len(sequencia),0):
            str+=sequencia[i]
        return str   


    def imprime():
        print('>Sequencia 1 = ',sequencia1,
            '\n>Sequencia 2 = ',sequencia2)

        sequencia=backtrace()

        print('\nAlinhamento local',
              '\n',sequencia[0],
              '\n',sequencia[1],
              '\nScore = ',score)
    

    validaSequencia(sequencia1)
    validaSequencia(sequencia2)

    
    preencheMatriz()
    preencheEspelho()

    backtrace()
    imprime()

smithWalterman()
