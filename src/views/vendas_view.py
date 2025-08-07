def mostrar_lista_vendas(vendas):
    if not vendas:
        print("\nNenhuma venda encontrada.\n")
        return

    print("\n=== Lista de Vendas ===")
    for v in vendas:
        print(f"Venda #{v.id} | Produto ID {v.id_produto} | Quantidade: {v.quantidade} | Data: {v.data_feita}")
    print("=======================\n")
