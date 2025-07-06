class DesarrolladorFrontend:
  def __init__(self, nombre, habilidades):
    self.nombre = nombre
    self.habilidades = habilidades
  
  def trabajar(self):
    print(f"Trabajando con {self.nombre} como desarrollador frontend con habilidades {', '.join(self.habilidades)}")
    