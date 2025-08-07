from src.models.venda import Venda
from src.models.db import get_db
from InquirerPy import prompt

def listar_vendas() -> str:
  conn = get_db()
  cursor = conn.cursor(dictionary=True)
  cursor.execute("SELECT * FROM vendas")
  resultados = cursor.fetchall()
  conn.close
  vendas = [Venda(**linha) for linha in resultados]
  
  return '\n'.join(str(venda) for venda in vendas)