import estudiantes.registro as registro

# Cargar datos de estudiantes desde un archivo CSV
datos = registro.importarCsv()

# Mostrar estudiantes ordenados alfabéticamente por nombre
registro.mostrarEstudiantesOrdenados(datos)

# Calcular y mostrar el promedio de notas
registro.CalcularPromedio(datos)