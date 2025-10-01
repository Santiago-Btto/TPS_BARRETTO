# Biblioteca escolar - Case insensitive en búsquedas y duplicados
# Restricciones: solo listas paralelas, sin funciones, sin diccionarios, sin clases
# Menú con match - case

titulos = []
ejemplares = []

while True:
    print("\n=== MENÚ BIBLIOTECA ESCOLAR ===")
    print("1. Ingresar lista de títulos")
    print("2. Ingresar lista de ejemplares disponibles")
    print("3. Mostrar catálogo con stock")
    print("4. Consultar disponibilidad de un título")
    print("5. Ver títulos agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Ver catálogo completo")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if not opcion.isdigit():
        print("⚠️ Error: Debe ingresar un número válido.")
        continue

    opcion = int(opcion)

    match opcion:
        case 1:  # Ingresar títulos
            cantidad = input("¿Cuántos títulos desea ingresar?: ")
            if not cantidad.isdigit():
                print("⚠️ Error: Ingrese un número válido.")
                continue
            cantidad = int(cantidad)

            for i in range(cantidad):
                while True:
                    titulo = input(f"Ingrese el título {i+1}: ").strip()
                    if titulo == "":
                        print("⚠️ Error: El título no puede estar vacío. Intente de nuevo.")
                        continue
                    # comprobación de duplicado
                    existe = False
                    for t in titulos:
                        if t.lower() == titulo.lower():
                            existe = True
                            break
                    if existe:
                        print("⚠️ Error: El título ya existe en el catálogo (incluso si difiere en mayúsculas). Intente otro.")
                        continue
                    # si ok, agregar
                    titulos.append(titulo)
                    ejemplares.append(0)
                    break

        case 2:  # Ingresar ejemplares
            if not titulos:
                print("⚠️ Primero debe ingresar títulos.")
                continue
            for i in range(len(titulos)):
                while True:
                    cantidad = input(f"Ingrese ejemplares para '{titulos[i]}': ")
                    if not cantidad.isdigit():
                        print("⚠️ Error: Debe ingresar un número entero no negativo. Intente de nuevo.")
                        continue
                    ejemplares[i] = int(cantidad)
                    break

        case 3:  # Mostrar catálogo con stock
            if not titulos:
                print("⚠️ No hay títulos cargados.")
            else:
                print("\n--- Catálogo con stock ---")
                for i in range(len(titulos)):
                    print(f"{titulos[i]}: {ejemplares[i]} copias")

        case 4:  # Consultar disponibilidad
            if not titulos:
                print("⚠️ No hay títulos cargados.")
                continue
            buscar = input("Ingrese el título a consultar: ").strip()
            if buscar == "":
                print("⚠️ Error: título vacío.")
                continue
            idx = -1
            for j, t in enumerate(titulos): #Recorre pares (indice, elemento)
                if t.lower() == buscar.lower():
                    idx = j
                    break
            if idx == -1:
                print("⚠️ Ese título no se encuentra en el catálogo.")
            else:
                print(f"'{titulos[idx]}' tiene {ejemplares[idx]} copias disponibles.")

        case 5:  # Ver títulos agotados
            if not titulos:
                print("⚠️ No hay títulos cargados.")
                continue
            agotado_flag = False
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f"Agotado: {titulos[i]}")
                    agotado_flag = True
            if not agotado_flag:
                print("✅ No hay títulos agotados.")

        case 6:  # Agregar título
            nuevo = input("Ingrese el nuevo título: ").strip()
            if nuevo == "":
                print("⚠️ Error: El título no puede estar vacío.")
                continue
            existe = False
            for t in titulos:
                if t.lower() == nuevo.lower():
                    existe = True
                    break
            if existe:
                print("⚠️ Error: El título ya existe.")
                continue
            cant = input("Ingrese la cantidad de ejemplares: ")
            if not cant.isdigit():
                print("⚠️ Error: Ingrese un número válido.")
                continue
            titulos.append(nuevo)
            ejemplares.append(int(cant))
            print(f"✅ Título '{nuevo}' agregado con {cant} copias.")

        case 7:  # Actualizar ejemplares (préstamo o devolución)
            if not titulos:
                print("⚠️ No hay títulos cargados.")
                continue
            libro = input("Ingrese el título: ").strip()
            if libro == "":
                print("⚠️ Error: título vacío.")
                continue
            idx = -1
            for j, t in enumerate(titulos):
                if t.lower() == libro.lower():
                    idx = j
                    break
            if idx == -1:
                print("⚠️ Ese título no existe en el catálogo.")
                continue

            print("1. Préstamo")
            print("2. Devolución")
            accion = input("Seleccione una opción: ")

            if accion == "1":
                cant = input("Ingrese cantidad a prestar: ")
                if not cant.isdigit():
                    print("⚠️ Error: Ingrese un número válido.")
                    continue
                cant = int(cant)
                if cant <= 0:
                    print("⚠️ Error: Debe prestar al menos 1 libro.")
                elif cant > ejemplares[idx]:
                    print("⚠️ No hay suficientes ejemplares disponibles.")
                else:
                    ejemplares[idx] -= cant
                    print(f"✅ Préstamo registrado. Ahora quedan {ejemplares[idx]} copias de '{titulos[idx]}'.")

            elif accion == "2":
                cant = input("Ingrese cantidad a devolver: ")
                if not cant.isdigit():
                    print("⚠️ Error: Ingrese un número válido.")
                    continue
                cant = int(cant)
                if cant < 1:
                    print("⚠️ Error: Debe devolver al menos 1 libro.")
                else:
                    ejemplares[idx] += cant
                    print(f"✅ Devolución registrada. Ahora hay {ejemplares[idx]} copias de '{titulos[idx]}'.")

            else:
                print("⚠️ Opción inválida.")

        case 8:  # Ver catálogo completo (igual que opción 3)
            if not titulos:
                print("⚠️ No hay títulos cargados.")
            else:
                print("\n--- Catálogo completo ---")
                for i in range(len(titulos)):
                    print(f"{titulos[i]}: {ejemplares[i]} copias")

        case 9:  # Salir
            print("👋 Gracias por usar el sistema de biblioteca. ¡Hasta pronto!")
            break

        case _:  # Opción inválida
            print("⚠️ Opción inválida. Intente de nuevo.")
