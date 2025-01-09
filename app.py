##Sistema de gerenciamento de estoque

class Produto:
  def _init_(self, id, nome, categoria_id, quantidade, preco):
    self.id = id
    self.nome = nome
    self.categoria_id = categoria_id
    self.quantidade = quantidade
    self.preco = preco

class Categoria:
  def _init_(self, id, nome):
    self.id = id
    self.nome = nome

class Movimentacao:
  def _init_(self, id, produto_id, quantidade,tipo_movimentacao, data):
    self.id = id
    self.produto_id = produto_id
    self.quantidade = quantidade
    self.tipo_movimentacao = tipo_movimentacao
    self.data = data

def cadastrar_produtos(produtos,contador_produtos):
  id = contador_produtos + 1
  nome = input('Nome do produto:')
  categoria_id = int(input('Id da categoria:'))
  quantidade = int(input('Insira a quantidade:'))
  preco = float(input('Insira o preço:'))
  produtos.append(Produto(id, nome, categoria_id, quantidade, preco))
  print('Produto cadastrado com sucesso!')
  return contador_produtos + 1

def consultar_produtos_id(produtos, id):
  for produto in produtos:
    if produto.id == id:
      print(f'Id: {produto.id}, Nome: {produto.nome}, Categoria: {produto.categoria_id}, Quantidade: {produto.quantidade}, Preço: {produto.preco}')
      return 


def registrar_movimentacao(movimentos,contador_movimentos, produtos):
  id = contador_movimentos
  produto_id = int(input('Id do produto:'))
  quantidade = int(input('Quantidade:'))
  tipo_movimentacao = input('Tipo de movimentação:\nE - Entrada\nS - Saída\n '). strip().upper()
  data = input('Data (DD/MM/AAAA): ')

  produto_encontrado = next(( p for p in produtos if p.id == produto_id), None)
  if produto_encontrado:
    if tipo_movimentacao == 'E':
      produto_encontrado.quantidade += quantidade
    elif tipo_movimentacao == 'S':
      if produto_encontrado.quantidade >= quantidade:
        produto_encontrado.quantidade -= quantidade
      else:
        print('Quantidade insuficiente em estoque.')
        return contador_movimentos
    movimentos.append(Movimentacao(id, produto_id, quantidade, tipo_movimentacao, data))
    print(f'Movimentação registrada com sucesso!')
    return contador_movimentos + 1
  else:
    print('Produto não encontrado.')
    return contador_movimentos
def gerar_relatorio_estoque(produtos):
  print("Relatório de Estoque:")
  for produto in produtos:
    print(f"ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}, Preço: {produto.preco:.2f}")

def consultar_movimentacoes(movimentacoes, produto_id):
  print(f"Movimentações do produto com ID {produto_id}:")
  for movimentacao in movimentacoes:
    if movimentacao.produto_id == produto_id:
      print(f"ID: {movimentacao.id}, Quantidade: {movimentacao.quantidade}, Tipo: {movimentacao.tipo_movimentacao}, Data: {movimentacao.data}")

def menu():
  import os
  import time
   
  produtos = []
  movimentacoes = []
  contador_produtos = 0
  contador_movimentacoes = 0

  while True:
    print("Estamos iniciando...")
    time.sleep(2)
    os.system('cls') or None
    print("### Seja bem vindo ao SISCONF! ###\n")
    escolha = int(input("Escolha uma opção:\n1 - Cadastrar Produto\n2 - Consultar Produto por ID\n3 - Movimentações\n4 - Consulta movimentos\n5 - Gerar relatório de estoque\n6 - Sair:\n"))
    if escolha == 1:
      while True:
        contador_produtos = cadastrar_produtos(produtos, contador_produtos)
        retornar = int(input("Escolha uma ação:\n1 - Cadastrar novo produto\n2 - Retornar ao menu principal: "))
        if retornar == 2:
          os.system('cls') or None
          break
    elif escolha == 2:
      while True:
        point = int(input("Qual o id do produto que deseja consultar: "))
        consultar_produtos_id(produtos, point)
        retornar = int(input("Escolha uma ação:\n1 - Consultar novo produto\n2 - Retornar ao menu principal: "))
        if retornar == 2:
          os.system('cls') or None
          break
    elif escolha == 3:
      contador_movimentacoes = registrar_movimentacao(movimentacoes, contador_movimentacoes, produtos)
      retornar = input("Deseja retornar ao menu: S - Sim N - Não: ").upper()
      if retornar == "S":
        os.system('cls') or None
    elif escolha == 4:
      point_mov = int(input('Insira o id do produto:'))
      consultar_movimentacoes(movimentacoes, point_mov)
      retornar = input("Deseja retornar ao menu: S - Sim N - Não: ").upper()
      if retornar == "S":
        os.system('cls') or None
    elif escolha == 5:
      gerar_relatorio_estoque(produtos)
      retornar = input("Deseja retornar ao menu: S - Sim N - Não: ").upper()
      if retornar == "S":
        os.system('cls') or None
    else:
      print('Saindo do sistema...')
      break

menu()