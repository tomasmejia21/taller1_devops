import csv

def importarCsv():
    datos = []
    with open('estudiantes.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            row[1] = float(row[1])
            if row[1] < 0 or row[1] > 5:
                print("Las notas deben estar entre 0 y 5")
            else:
                datos.append(row)
    
    print(datos)
    return datos

def mostrarEstudiantesOrdenados(datos):
    # Ordenar estudiantes por orden alfabético
    datos.sort(key=lambda x: x[1], reverse=True)
    print("Estudiantes ordenados por nota:")
    for estudiante in datos:
        estudiantes_ordenados = sorted(datos, key=lambda e: e[0].lower())
    
    # Encabezado
    print(f"{'Nombre':<20} {'Nota':>5}")
    print("-" * 26)

    # Mostrar estudiantes
    for estudiante in estudiantes_ordenados:
        nombre = estudiante[0]
        nota = estudiante[1]
        print(f"{nombre:<20} {nota:>5.1f}")

mostrarEstudiantesOrdenados(importarCsv())