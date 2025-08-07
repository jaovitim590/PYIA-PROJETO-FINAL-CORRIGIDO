from dataclasses import dataclass

@dataclass
class Produto:
  nome: str
  descricao: str
  preco: float
  quantidade: int
  id : str =  None