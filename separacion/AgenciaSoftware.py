class AgenciaSoftware:
  def __init__(self, proyecto):
    self.proyecto = proyecto
  
  def iniciarProyecto(self):
    print("-----Agencia de Software------")
    print(f"Proyecto iniciado {proyecto.titulo}")
    self.proyecto.ejecutar()
  
  
  
  
  
if __name__ == "__main__":
  from Proyecto import Proyecto
  from DesarrolladorFrontend import DesarrolladorFrontend
  from DesarrolladorBackend import DesarrolladorBackend
  
  proyecto = Proyecto("Aplicacion Web")
  
  frontend_marco = DesarrolladorFrontend("Marco", ["HTML", "CSS", "JavaScript", "PHP"])
  backend_emily = DesarrolladorBackend("Emily", "Python")
  backend_doris = DesarrolladorBackend("Doris", "C#")
  
  proyecto.agregarEquipo(frontend_marco)
  proyecto.agregarEquipo(backend_emily)
  proyecto.agregarEquipo(backend_doris)
  
  agencia = AgenciaSoftware(proyecto)
  
  agencia.iniciarProyecto()