def smithWalterman():           
        
    sequencia1='ATCGTCTTTA'
    sequencia2='GTCGTCATTT'
    linhas=len(sequencia2)+1
    colunas=len(sequencia1)+1
    matriz=espelho=[]
    gap=-2
    match=1
    mismatch=-1
    esquerda=topo=diagonal=valor=score=0
    
    def validaSequencia(sequencia):
        for i in range(len(sequencia)):
            if sequencia[i] not in ['A', 'T', 'C', 'G']:                
                return False
        
        return True

    def inicializaMatriz():            
        for i in range(linhas):
            matriz[i][0]=gap*i
        
        for j in range(colunas):
            matriz[0][j]=gap*j    

    def match(letra1,letra2):
        if(letra1==letra2):
            return True
        else:
            False

    def preencheMatriz():
        for i in range(1,linhas):      
            for j in range (1,colunas):
                if(match(sequencia1[j-1],sequencia2[i-1])==True):
                    valor=match
                else:
                    valor=mismatch
                
                diagonal=matriz[i-1][j-1]+valor
                topo=matriz[i-1][j]+gap
                esquerda=matriz[i][j-1]+gap

                matriz[i][j]=max(diagonal,topo,esquerda)
                preencheEspelho(i,j)
                
    def preencheEspelho(i,j):
        num=max(diagonal,topo,esquerda)
        
        if(num==diagonal):
            espelho[i-1][j-1]="diagonal"
        elif(num==topo):
            espelho[i-1][j-1]="topo"
        elif(num==esquerda):    
            espelho[i-1][j-1]="esquerda"

    def backtrace():
        sequencia=[]
        coluna=colunas-1
        linha=0
        
        for i  in range(linhas):
            if score <= matriz[i][coluna]:
                pontuacao=matriz[i][coluna]
                linha=i

        linha-=1
        coluna-=1

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

    def inverte(sequencia):
        str=""               

        for i in range(len(sequencia),0):
            str+=sequencia[i]
        return str   

    def imprime():
        print('>Sequencia 1 = ',sequencia1,
            '\n>Sequencia 2 = ',sequencia2)

        sequencia=backtrace()

        print('\n',sequencia[0],
            '\n',sequencia[1],
            '\nScore = ',score)
