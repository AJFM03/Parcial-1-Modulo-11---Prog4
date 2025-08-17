import json
import os

# Archivo donde se guardarán los artículos
DATA_FILE = "articulos.json"

# Funciones de manejo de datos

def cargar_articulos():
    """Carga los artículos desde el archivo JSON."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_articulos(articulos):
    """Guarda los artículos en el archivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(articulos, f, indent=4, ensure_ascii=False)

def generar_id(articulos):
    """Genera un ID único para un nuevo artículo."""
    if not articulos:
        return 1
    return max(articulo["id"] for articulo in articulos) + 1

# Funciones CRUD

def registrar_articulo():
    articulos = cargar_articulos()
    print("\n--- Registrar Nuevo Artículo ---")
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    cantidad = input("Cantidad: ").strip()
    precio = input("Precio unitario: ").strip()
    descripcion = input("Descripción: ").strip()

    # Validaciones
    if not nombre or not categoria or not cantidad or not precio:
        print("Error: Campos obligatorios incompletos.")
        return
    try:
        cantidad = float(cantidad)
        precio = float(precio)
    except ValueError:
        print("Error: Cantidad y precio deben ser números.")
        return

    articulo = {
        "id": generar_id(articulos),
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
        "descripcion": descripcion
    }
    articulos.append(articulo)
    guardar_articulos(articulos)
    print(f"Artículo '{nombre}' registrado correctamente.\n")

def listar_articulos():
    articulos = cargar_articulos()
    if not articulos:
        print("\nNo hay artículos registrados.\n")
        return
    print("\n--- Lista de Artículos ---")
    print(f"{'ID':<5} {'Nombre':<20} {'Categoría':<15} {'Cantidad':<10} {'Precio':<10} {'Descripción'}")
    print("-"*80)
    for art in articulos:
        print(f"{art['id']:<5} {art['nombre']:<20} {art['categoria']:<15} {art['cantidad']:<10} {art['precio']:<10} {art['descripcion']}")
    print("")

def buscar_articulos():
    articulos = cargar_articulos()
    if not articulos:
        print("\nNo hay artículos registrados.\n")
        return
    criterio = input("Buscar por (nombre/categoría): ").strip().lower()
    if criterio not in ["nombre", "categoría"]:
        print("Opción inválida.")
        return
    valor = input(f"Ingrese el {criterio} a buscar: ").strip().lower()
    resultados = [art for art in articulos if art[criterio].lower() == valor]
    if resultados:
        print("\n--- Resultados de Búsqueda ---")
        for art in resultados:
            print(f"ID: {art['id']}, Nombre: {art['nombre']}, Categoría: {art['categoria']}, Cantidad: {art['cantidad']}, Precio: {art['precio']}, Descripción: {art['descripcion']}")
    else:
        print("No se encontraron artículos.\n")

def editar_articulo():
    articulos = cargar_articulos()
    if not articulos:
        print("\nNo hay artículos registrados.\n")
        return
    try:
        id_buscar = int(input("Ingrese el ID del artículo a editar: "))
    except ValueError:
        print("ID inválido.")
        return
    articulo = next((art for art in articulos if art["id"] == id_buscar), None)
    if not articulo:
        print("Artículo no encontrado.")
        return

    print(f"Editando artículo: {articulo['nombre']}")
    nombre = input(f"Nombre [{articulo['nombre']}]: ").strip() or articulo['nombre']
    categoria = input(f"Categoría [{articulo['categoria']}]: ").strip() or articulo['categoria']
    cantidad = input(f"Cantidad [{articulo['cantidad']}]: ").strip() or articulo['cantidad']
    precio = input(f"Precio [{articulo['precio']}]: ").strip() or articulo['precio']
    descripcion = input(f"Descripción [{articulo['descripcion']}]: ").strip() or articulo['descripcion']

    try:
        cantidad = float(cantidad)
        precio = float(precio)
    except ValueError:
        print("Error: Cantidad y precio deben ser números.")
        return

    articulo.update({
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
        "descripcion": descripcion
    })
    guardar_articulos(articulos)
    print("Artículo actualizado correctamente.\n")

def eliminar_articulo():
    articulos = cargar_articulos()
    if not articulos:
        print("\nNo hay artículos registrados.\n")
        return
    try:
        id_buscar = int(input("Ingrese el ID del artículo a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return
    articulo = next((art for art in articulos if art["id"] == id_buscar), None)
    if not articulo:
        print("Artículo no encontrado.")
        return
    articulos.remove(articulo)
    guardar_articulos(articulos)
    print(f"Artículo '{articulo['nombre']}' eliminado correctamente.\n")

# Menú principal

def menu():
    while True:
        print("=== Sistema de Registro de Presupuesto ===")
        print("1. Registrar artículo")
        print("2. Listar artículos")
        print("3. Buscar artículos")
        print("4. Editar artículo")
        print("5. Eliminar artículo")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            registrar_articulo()
        elif opcion == "2":
            listar_articulos()
        elif opcion == "3":
            buscar_articulos()
        elif opcion == "4":
            editar_articulo()
        elif opcion == "5":
            eliminar_articulo()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu()
