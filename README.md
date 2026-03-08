GERENCIADOR DE ESTOQUE EM PYTHON

Este e um sistema simples de gerenciamento de produtos desenvolvido em Python, utilizando dicionarios para armazenamento de dados. Objetivo é um exercício de treinamento de lógica e de versionamento

ESTRUTURA DE DADOS

O projeto utiliza um dicionario principal chamado registroProduto, onde a busca e otimizada pelo ID do produto.
Chave: idProduto (Valor unico para identificacao)
Valor: (produto, unidade, quantidade) - Armazenado como uma tupla.

FUNCIONALIDADES

- Cadastro de Produtos:
Adiciona um novo item ao dicionario atraves da funcao novoProduto(produto, idProduto, unidade, quantidade).
- Atualizacao de Estoque:
Incrementa a quantidade de um produto existente atraves da funcao adicionarUm(idProduto).
- Busca por Nome:
Permite localizar o ID de um produto filtrando pelo seu nome literal percorrendo o dicionario.

LOGICA APLICADA

O sistema utiliza o conceito de chave:valor onde o ID permite acesso instantaneo aos dados, enquanto a alteracao de estoque exige o desempacotamento da tupla para atualizar o valor da quantidade

ATUALIZAÇOES FUTURAS:
- pesquisa por ID
- maior verificação de dados 
- armazenamento de dados
