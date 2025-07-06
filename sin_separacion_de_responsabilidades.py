class AgenciaDesarrollo:
  def __init__(self):
    self.proyecto = None
    self.equipo = []
    
  def iniciarProyecto(self, titulo):
    self.proyecto = titulo
    print(f"Proyecto iniciado {titulo}")
  
  def agregarEquipo(self, nombre, rol):
    self.equipo.append({"nombre": nombre, "rol": rol})
    print(f"Equipo {nombre} agregado")
  
  def trabajar(self):
    print(f"Trabajando en {self.proyecto}")
    
    for dev in self.equipo:
      print(f"Trabajando con {dev['nombre']} como {dev['rol']}")
      

def main():
  agencia = AgenciaDesarrollo()
  
  agencia.iniciarProyecto("Proyecto 1")
  agencia.agregarEquipo("Marco", "Desarrollador Frontend")
  agencia.agregarEquipo("Emily", "Desarrollador Backend")
  agencia.agregarEquipo("Doris", "Desarrollador Backend")
  agencia.trabajar()
  
if __name__ == "__main__":
  main()