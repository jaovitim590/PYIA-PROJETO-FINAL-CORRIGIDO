def mostrar_lista_produtos(produtos: list):
    if not produtos:
        print("\nNenhum produto encontrado.\n")
        return

    print("\n=== Lista de Produtos ===")
    for p in produtos:
        print(f"ID: {p.id} | Nome: {p.nome} | Preço: R${p.preco:.2f} | Quantidade: {p.quantidade}")
    print("=========================\n")


def mostrar_produto_adicionado(produto):
    print(f"\n✅ Produto '{produto.nome}' adicionado com sucesso!\n")

