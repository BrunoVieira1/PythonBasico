estoque = []
idContador = 0

def adicionarProduto():
    global idContador
    
    print("\nadicionar Novo Produto")
    nome = input("nome: ")
    quantidade = int(input("quantidade: "))
    preco = float(input("preco: "))

    idContador += 1
    produto = {
        "id": idContador,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    estoque.append(produto)
    print("produto adicionado")

def listarProdutos():
    print("\nlista de produtos")
    if not estoque:
        print("o estoque esta vazio.")
    else:
        for i in estoque:
            print(f"ID: {i['id']} , Nome: {i['nome']} , Qtd: {i['quantidade']} , Preco: R$ {i['preco']:.2f}")

def atualizarProduto():
    print("\natualizar Produto")
    idAtualizacao = int(input("digite o ID do produto para atualizar: "))

    produtoRegistrado = None
    for i in estoque:
        if i["id"] == idAtualizacao:
            produtoRegistrado = i
            break
    
    if produtoRegistrado is not None:
        print(f"atualizando produto: {produtoRegistrado['nome']}")
        newNome = input(f"novo nome: ")
        newPreco = float(input(f"novo preco: "))
            
        produtoRegistrado["nome"] = newNome if newNome else produtoRegistrado["nome"]
        produtoRegistrado["preco"] = newPreco
        print("produto atualizado")
    else:
        print("produto nao encontrado.")

def deletarProduto():
    print("\ndeletar Produto")
    idDelete = int(input("digite o ID do produto para deletar: "))

    produtoRemover = None
    for i in estoque:
        if i["id"] == idDelete:
            produtoRemover = i
            break
            
    if produtoRemover is not None:
        estoque.remove(produtoRemover)
        print("produto removido")
    else:
        print("produto nao encontrado")
        
def registrarEntrada():
    print("\nregistrar entrada")

    idProduto = int(input("digite o ID do produto: "))
        
    produtoRegistrado = None
    for i in estoque:
        if i["id"] == idProduto:
            produtoRegistrado = i
            break

    if produtoRegistrado is not None:
      qttEntrada = int(input(f"quantidade de entrada para '{produtoRegistrado['nome']}': "))
      if qttEntrada <= 0:
          print("a quantidade deve ser maior que zero.")
          return
            
      produtoRegistrado["quantidade"] += qttEntrada
      print("entrada registrada. nova quantidade:", produtoRegistrado["quantidade"])
    else:
        print("produto nao encontrado.")

def registrarSaida():
    print("\nregistrar saida")

    idProduto = int(input("digite o ID do produto: "))
        
    produtoRegistrado = None
    for i in estoque:
        if i["id"] == idProduto:
            produtoRegistrado = i
            break

    if produtoRegistrado:
      quantidadeSaida = int(input(f"quantidade de saida para '{produtoRegistrado['nome']}': "))
            
      if quantidadeSaida > produtoRegistrado["quantidade"]:
          print(f"quantidade insuficiente, Em estoque: {produtoRegistrado['quantidade']}!")
          return
            
      if quantidadeSaida <= 0:
          print("a quantidade deve ser maior que zero")
          return

      produtoRegistrado["quantidade"] -= quantidadeSaida
      print("saida registrada. Nova quantidade: ", produtoRegistrado["quantidade"])
    else:
        print("produto nao encontrado.")
        
def main(): 
  while True:
      print("\nmenu de Estoque")
      print("1. adicionar Produto")
      print("2. listar Produtos")
      print("3. atualizar Produto")
      print("4. deletar Produto")
      print("5. registrar Entrada")
      print("6. registrar Saida")
      print("0. sair")
      
      option = input("escolha uma opcao: ")
      
      if option == '1':
          adicionarProduto()
      elif option == '2':
          listarProdutos()
      elif option == '3':
          atualizarProduto()
      elif option == '4':
          deletarProduto()
      elif option == '5':
          registrarEntrada()
      elif option == '6':
          registrarSaida()
      elif option == '0':
          print("saindo do programa.")
          break
      else:
          print("opcao invalida.")

if __name__ == "__main__":
    main()