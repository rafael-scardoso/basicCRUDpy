import os

registroProduto=dict() #dicionário nome do produto:ID


def novoProduto(produto,idProduto,unidade,quantidade): #função para adicionar um novo produto
        registroProduto[idProduto]={"produto":produto,"unidade":unidade,"quantidade":quantidade}
def adicionarProduto(produto,quantidade): #função para adicionar produtos ao estoque
    for chave, dados in registroProduto.items():
        if produto.upper() == dados["produto"].upper():
            registroProduto[chave]["quantidade"] += quantidade
            break

def removerProduto(produto,quantidade): 
     for chave, dados in registroProduto.items():
        if produto.upper() == dados["produto"].upper():
            registroProduto[chave]["quantidade"] -= quantidade
            break
def pesquisarProduto(produto):
            for chave in registroProduto:
                if produto in chave:
                    print(registroProduto[chave])
                
          

menu=10 #inicialização da váriavel de controle de looping
idProduto=0 #inicialização da váriavel de controle de ID

print("Bem vindo ao cadastro de produtos!")


while menu!=0:
        
        if menu != 10:
            print('Lista de produtos:')
            print('---------------------------------------------------------------------------------\n')
        for chave,dados in registroProduto.items():
            if chave is None:
                continue     
            else: 
                 print(f'ID: {chave} | Nome do produto: {dados["produto"]} | Unidade de medida: {dados["unidade"]} | Quantidade: {dados["quantidade"]:.2f}')
        
        
        print("\nDigite a opção desejada:\n")
        print("1 - Adicionar novo produto")
        print("2 - Adicionar produto ao estoque")
        print("3 - Remover produto do estoque")
        print("4 - Pesquisar produto")
        print("0 - Sair do programa")
        menu=int(input())
              

        match menu:

            case 1: 
                #os.system('cls')
                print("Entrou na função adicionar novo produtos\n")
                produto=input('Digite o nome do produto:\n').upper()
                unidade=input('Digite a unidade de medida:\n').upper()
                idProduto=idProduto+1
                quantidade=float(input('Digite a quantidade:\n'))
                novoProduto(produto,idProduto,unidade,quantidade)
                print('Produto adicionado\n')
                
            case 2:
               #os.system('cls')
               print("Entrou na função adicionar produtos ao estoque\n") 
               produto=input('Digite o nome do produto:\n').upper()
               encontrado = False
               for chave,dados in registroProduto.items(): #permite escrever o nome parcialmente e filtra caso não encontro nada
                    if produto in dados["produto"]:
                        idProduto=chave
                        encontrado = True
                        quantidade=float(input('Digite a quantidade de produtos para adicionar ao estoque:\n'))
                        adicionarProduto(produto,quantidade)
                        print(f'O valor em estoque de {produto} é de {registroProduto[idProduto]["quantidade"]:.2f}')      
               if  encontrado==False:
                    print('Produto não encontrado! Tente novamente.\n')
               
                     
            
            
            case 3: 
               #os.system('cls')
               print("Entrou na função remover produtos ao estoque\n") 
               produto=input('Digite o nome do produto:\n').upper()
               encontrado = False
               for chave,dados in registroProduto.items(): #permite escrever o nome parcialmente e filtra caso não encontro nada
                    if produto in dados["produto"]:
                        idProduto=chave
                        encontrado = True
                        quantidade=float(input('Digite a quantidade de produtos para remover ao estoque:\n'))
                        removerProduto(produto,quantidade)
                        print(f'O valor em estoque de {produto} é de {registroProduto[idProduto]["quantidade"]:.2f}')
               if encontrado==False:
                    print('Produto não encontrado! Tente novamente.\n')
               
               


            case 4: 
                
                #os.system('cls')
                print("Entrou na função pesquisar produtos\n")
                produto = input('Digite o produto que deseja pesquisar:\n').upper()
                encontrado = False

                for chave, dados in registroProduto.items():
                    if produto in dados["produto"].upper():

                        print("ID:", chave)
                        print("Produto:", dados["produto"].upper())
                        print("Quantidade:", dados["quantidade"])
                        print("Unidade:", dados["unidade"].upper())
                        print()
                        encontrado = True

                if encontrado == False:
                     print("Produto não encontrado! Tente Novamente.\n")
                


            case 0: 
                print("Programa encerrado\n")
                menu=0
