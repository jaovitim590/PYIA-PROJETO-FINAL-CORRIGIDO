from src.models.produto import Produto
from src.models.db import get_db
from InquirerPy import prompt

def criar_produto(produto: Produto):
  conn = get_db()
  cursor = conn.cursor()
  try:
    sql = """
          INSERT INTO produtos (nome, descricao, preco, quantidade)
          VALUES (%s, %s, %s, %s)
      """
    valores = (produto.nome, produto.descricao, produto.preco, produto.quantidade)

    cursor.execute(sql, valores)
    conn.commit()
    print(f"O produto foi cadastrado com sucesso!")
  except Exception as e:
     print(f"houve um erro ao criar um produto: {e}")

  finally:
     conn.close()
  

def listar_produtos() -> list[Produto]:
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    resultados = cursor.fetchall()
    conn.close()
    produtos = [Produto(**linha) for linha in resultados]
    return produtos

def remover_produto(id: int):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)  
    try:
        
        cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,))
        resultado = cursor.fetchone()

        if not resultado:
            return f"Nenhum produto encontrado com id {id}."

        produto_obj = Produto(**resultado)
        produto_info = (
            f"Produto(nome='{produto_obj.nome}', "
            f"preco={produto_obj.preco}, "
            f"quantidade={produto_obj.quantidade}, "
            f"id={produto_obj.id})"
        )

     
        cursor.execute("SELECT COUNT(*) AS total FROM vendas WHERE id_produto = %s", (id,))
        total_vendas = cursor.fetchone()["total"]

        if total_vendas > 0:
            resposta = prompt([
                {
                    "type": "confirm",
                    "message": f"{produto_info} está vinculado a {total_vendas} venda(s). Deseja deletar as vendas também?",
                    "name": "confirmacao",
                    "default": False
                }
            ])

            if not resposta["confirmacao"]:
                return "Operação cancelada pelo usuário. Nenhum dado foi excluído."

            cursor.execute("DELETE FROM vendas WHERE id_produto = %s", (id,))
            conn.commit()

    
        resposta = prompt([
            {
                "type": "confirm",
                "message": f"Deseja deletar {produto_info}?",
                "name": "confirmacao",
                "default": False
            }
        ])

        if not resposta["confirmacao"]:
            return "Operação cancelada pelo usuário. Nenhum dado foi excluído."

        cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
        conn.commit()

        return f"O produto {produto_info} e suas vendas (se existiam) foram deletados com sucesso."

    except Exception as error:
        return f"Houve um erro ao deletar o produto: {error}"

    finally:
        conn.close()

def update_produto(id: int, quant: int):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)  
    try:
          print("----- BUSCA DE PRODUTO -----")
          cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,))
          resultado = cursor.fetchone()

          if not resultado:
              return f"Nenhum produto encontrado com id {id}."

          produto_obj = Produto(**resultado)
          produto_info = (
            f"Produto(nome='{produto_obj.nome}', "
            f"preco={produto_obj.preco}, "
            f"quantidade={produto_obj.quantidade}, "
            f"id={produto_obj.id})")
          resposta = prompt([
              {
                  "type": "confirm",
                  "message": f"Produto encontrado: {produto_info}. Deseja continuar com a atualização?",
                  "name": "confirmacao",
                  "default": False
              }
          ])

          if not resposta["confirmacao"]:
              return "Operação cancelada pelo usuário. Nenhum dado foi alterado."

          cursor.execute("UPDATE produtos SET quantidade = %s WHERE id = %s", (quant, id))
          conn.commit()
          return f"Produto com id {id} atualizado com sucesso. Nova quantidade: {quant}"

    except Exception as error:
          return f"Houve um erro ao atualizar o produto: {error}"

    finally:
          conn.close()
      
