import csv
import os

# Obtiene automáticamente la carpeta donde está guardado este script
carpeta_actual = os.path.dirname(os.path.abspath(__file__))

# Definimos los nombres y rutas de los archivos dentro de esa misma carpeta
archivo_csv = os.path.join(carpeta_actual, 'employees.csv')
archivo_reporte = os.path.join(carpeta_actual, 'report.txt')

# Función inicial: comprueba si el CSV existe; si no existe, lo crea con datos de prueba
def create_sample_csv(csv_file_location):
    if not os.path.exists(csv_file_location):
        datos_empleados = [
            ["Full Name", "Username", "Department"],
            ["Audrey Miller", "audrey", "Development"],
            ["Arden Garcia", "ardeng", "Sales"],
            ["Bailey Thomas", "baileyt", "Human Resources"],
            ["Blake Sousa", "sousa", "IT infrastructure"],
            ["Cameron Nguyen", "nguyen", "Marketing"],
            ["Charlie Grey", "greyc", "Development"],
            ["Chris Black", "chrisb", "User Experience Research"],
            ["Courtney Silva", "silva", "IT infrastructure"],
            ["Darcy Johnson", "darcy", "IT infrastructure"],
            ["Elliot Lamb", "elliotl", "Development"]
        ]
        with open(csv_file_location, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(datos_empleados)
        print("Archivo 'employees.csv' creado por primera vez.")
    else:
        print("El archivo 'employees.csv' ya existe. Se usarán los datos actuales.")

# 1. Función para leer el archivo CSV y convertirlo en una lista de diccionarios
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    with open(csv_file_location, mode='r', encoding='utf-8') as f:
        employee_file = csv.DictReader(f, dialect='empDialect')
        employee_list = []
        for data in employee_file:
            employee_list.append(dict(data))
    return employee_list

# 2. Función para contar cuántos empleados hay por departamento
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

# 3. Función para escribir el reporte final ordenado alfabéticamente en report.txt
def write_report(dictionary, report_file):
    with open(report_file, mode="w+", encoding='utf-8') as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')

# --- Ejecución principal del programa ---
create_sample_csv(archivo_csv)               # Verifica o crea 'employees.csv'
employee_list = read_employees(archivo_csv)  # Lee los datos del CSV
dictionary = process_data(employee_list)     # Cuenta los empleados por departamento
write_report(dictionary, archivo_reporte)    # Crea o actualiza 'report.txt'

print("¡Reporte generado con éxito en:", archivo_reporte)
