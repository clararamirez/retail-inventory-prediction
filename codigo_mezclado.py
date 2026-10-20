# codigo_mezclado.py
DB_USER = "admin_prod"
DB_PASS = "12345_super_secreta"

def extraer_datos():
    print(f"Conectando a BD con {DB_USER}")
    return "datos crudos"

def entrenar_modelo(datos):
    print("Entrenando modelo sin limpiar datos...")
    return "Modelo 50% preciso"
