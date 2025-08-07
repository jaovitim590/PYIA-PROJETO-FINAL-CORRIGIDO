from src.controllers.produtos_controller import criar_produto, listar_produtos, remover_produto, update_produto
from src.controllers.vendas_controller import listar_vendas
from src.models.produto import Produto

from src.views.produtos_view import (
    mostrar_lista_produtos,
    mostrar_produto_adicionado
)
from src.views.vendas_view import mostrar_lista_vendas

class Estoque:
    def __init__(self):
        pass

    def adicionar_produto(self, nome: str, descricao: str, preco: float, quantidade: int):
        produto = Produto(nome, descricao, preco, quantidade)
        resultado = criar_produto(produto)

        print(resultado)
        mostrar_produto_adicionado(produto)

    def listar_produtos(self):
        produtos = listar_produtos()
        mostrar_lista_produtos(produtos)

    def remover_produto(self, id_produto: int):
        resultado = remover_produto(id_produto)
        print(resultado)

    def atualizar_produto(self, id_produto: int, nova_quantidade: int):
        resultado = update_produto(id_produto, nova_quantidade)
        print(resultado)

    def listar_vendas(self):
        vendas = listar_vendas()
        mostrar_lista_vendas(vendas)