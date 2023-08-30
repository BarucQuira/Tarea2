
"""
Ejemplo de las partes de la Arquitectura de un Sistema Experto, partiendo de un identificador de serpientes venenosas
Baruc Gutiérrez Quirarte - 7F1 
Sistemas Expertos
"""

# Módulo de Adquisición de Conocimiento
def adquirir_conocimiento():
    conocimiento = {
        "Víbora de cascabel": {"patrón": "Cascabel en la cola", "venenosa": True},
        "Cobra": {"patrón": "Cuello con capucha", "venenosa": True},
        "Boa constrictor": {"patrón": "Cuerpo musculoso", "venenosa": False},
        # Agrega más información sobre otras serpientes
    }
    return conocimiento

# Módulo de Explicaciones
def explicar(resultado):
    if resultado["venenosa"]:
        return "Esta serpiente es venenosa. Ten cuidado."
    else:
        return "Esta serpiente no es venenosa. No representa peligro."

# Motor de Inferencia
def inferir(caracteristicas, conocimiento):
    for serpiente, info in conocimiento.items():
        if info["patrón"] in caracteristicas:
            return {"nombre": serpiente, "venenosa": info["venenosa"]}
    return {"nombre": "Desconocida", "venenosa": False}

# Interfaz de Usuario
def interfaz_usuario():
    print("Bienvenido al Sistema Experto de Identificación de Serpientes")
    caracteristicas = input("Ingresa las características de la serpiente: ")
    
    conocimiento = adquirir_conocimiento()
    resultado = inferir(caracteristicas, conocimiento)
    explicacion = explicar(resultado)
    
    print(f"La serpiente podría ser: {resultado['nombre']}")
    print(explicacion)

# Ejecución del Sistema
interfaz_usuario()
