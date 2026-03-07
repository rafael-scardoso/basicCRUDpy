import os

nomeProduto=dict() #dicionário nome do produto:ID
unidadeProduto=dict() #dicionário nome do produto: unidade de medida
estoqueProduto=dict() #dicionário nome do produto: estoque


def novoProduto(produto,idProduto,unidade,quantidade): #função para adicionar um novo produto
        nomeProduto[produto]=(idProduto)
        unidadeProduto[produto]=(unidade)
        estoqueProduto[produto]=(quantidade)
def adicionarProduto(produto,quantidade): #função para adicionar produtos ao estoque
     estoqueProduto[produto]=estoqueProduto[produto]+quantidade

def removerProduto(produto): 
            
        estoqueProduto[produto]=estoqueProduto[produto]-quantidade

def pesquisarProduto(produto):
            for chave, valor in nomeProduto:
                if produto in chave:
                    print(nomeProduto[chave])
                
          

menu=10 #inicialização da váriavel de controle de looping
idProduto=0 #inicialização da váriavel de controle de ID

print("Bem vindo ao cadastro de produtos!")


while menu!=0:
        
        if menu != 10:
            print('Lista de produtos:')
            print('---------------------------------------------------------------------------------\n')
        for chave,valor in nomeProduto.items():
            if chave is None:
                continue     
            else: 
                 print(f'ID: {idProduto} | Nome do produto: {chave} | Unidade de medida: {unidadeProduto[chave]} | Quantidade: {estoqueProduto[chave]:.2f}')
        
        
        print("\nDigite a opção desejada:\n")
        print("1 - Adicionar novo produto")
        print("2 - Adicionar produto ao estoque")
        print("3 - Remover produto do estoque")
        print("4 - Pesquisar produto")
        print("0 - Sair do programa")
        menu=int(input())
              

        match menu:

            case 1: 
                os.system('cls')
                print("Entrou na função adicionar novo produtos\n")
                produto=input('Digite o nome do produto:\n')
                unidade=input('Digite a unidade de medida:\n')
                idProduto=idProduto+1
                quantidade=float(input('Digite a quantidade:\n'))
                novoProduto(produto,idProduto,unidade,quantidade)
                print('Produto adicionado\n')
                
            case 2:
               os.system('cls')
               print("Entrou na função adicionar produtos ao estoque\n") 
               produto=input('Digite o nome do produto:\n')
               encontrado = False
               for chave in nomeProduto: #permite escrever o nome parcialmente e filtra caso não encontro nada
                    if produto in chave:
                        produto=chave
                        encontrado = True
               if not encontrado:
                    print('Produto não encontrado! Tente novamente.\n')
               
               quantidade=float(input('Digite a quantidade de produtos para adicionar ao estoque:\n'))
               adicionarProduto(produto,quantidade)
               print(f'O valor em estoque de {produto} é de {estoqueProduto[produto]:.2f}')      
            
            
            case 3: 
                os.system('cls')
                print("Entrou na função remover produtos do estoque\n")
                produto=input('Digite o produto que a ser removido\n')
                encontrado = False
                for chave in nomeProduto: #permite escrever o nome parcialmente e filtra caso não encontro nada
                    if produto in chave:
                        produto=chave
                        encontrado = True
                if not encontrado:
                    print('Produto não encontrado! Tente novamente.\n')
                quantidade=float(input('Digite a quantidade de produtos a serem removida:\n'))        
                removerProduto(produto)
                print(f'Produto removido. Nova quantidade é de {estoqueProduto[produto]:2f}')


            case 4: 
                os.system('cls')
                print("Entrou na função pesquisar produtos\n")
                produto = input('Digite o produto que deseja pesquisar:\n')
                encontrado = False

                for chave in nomeProduto: #permite escrever o nome parcialmente e filtra caso não encontro nada
                    if produto in chave:
                     print("Produto:", chave)
                     print("ID:", nomeProduto[chave])
                     print("Unidade:", unidadeProduto[chave])
                     encontrado = True
                if not encontrado:
                 print("Produto não encontrado! Tente Novamente.\n")
                


            case 0: 
                print("Programa encerrado\n")
                menu=0
