class Proyecto:
  def __init__(self, titulo):
    self.titulo = titulo
    self.equipo = []
  
  def agregarEquipo(self, desarrollador):
    self.equipo.append(desarrollador)
    print(f"Miembro del equipo {desarrollador.nombre} agregado")
    
    
  def ejecutar(self):
    print(f"Trabajando en {self.titulo}")
    for miembro in self.equipo:
      miembro.trabajar()