from dataclasses import dataclass
from datetime import date

@dataclass
class Venda:
  id_produto: int
  quantidade: int
  data_feita: date
  id : str  = None