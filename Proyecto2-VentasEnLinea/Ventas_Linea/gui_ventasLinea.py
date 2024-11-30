import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel
from PIL import Image, ImageTk
from db_config import conectar
from CRUD_productos import agregar_producto, ver_productos, actualizar_producto, eliminar_producto
from CRUD_clientes import registrar_cliente, ver_clientes, actualizar_cliente
from CRUD_ordenes import modificar_ordenes_para_cantidad_maxima, mostrar_ordenes_por_cliente
from CRUD_busquedas_avanzadas import buscar_producto, buscar_cliente
from CRUD_reportes import productos_mas_vendidos

# Configuración de la conexión
def obtener_conexion():
    return conectar(host="127.0.0.1", user="root", password="43972099", database="sistema_ventas")


# Función para salir de la aplicación
def salir():
    respuesta = messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir?")
    if respuesta:
        root.destroy() 

# --------------------------------------------------
# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Ventas en Línea")
root.geometry("600x400")
root.configure(bg="#FFF8DC")  # Fondo en tono pastel amarillo claro

# Estilo global
fuente_titulo = ("Helvetica", 18, "bold")
fuente_boton = ("Helvetica", 12)
color_boton = "#FFD700"
color_hover = "#FFEC8B"

# Título principal
titulo = tk.Label(root, text="Sistema de Ventas en Línea", font=fuente_titulo, bg="#FFF8DC", fg="#8B4513")
titulo.grid(row=0, column=0, columnspan=2, pady=20)

# Crear contenedor para los botones
contenedor_botones = tk.Frame(root, bg="#FFF8DC")
contenedor_botones.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

# Crear un botón decorado
def crear_boton(contenedor, texto, comando):
    boton = tk.Button(
        contenedor,
        text=texto,
        font=fuente_boton,
        bg=color_boton,
        fg="#000",
        activebackground=color_hover,
        activeforeground="#000",
        relief="flat",
        padx=10,
        command=comando
    )
    boton.grid(pady=10, sticky="ew") 
    return boton

#--------------------------------------------------------
#-----------------(Gestión de productos)-----------------
#--------------------------------------------------------
def gestion_productos():
    ventana_productos = Toplevel(root)
    ventana_productos.title("Gestión de Productos")
    ventana_productos.geometry("600x500")
    ventana_productos.configure(bg="#FFF8DC")

    titulo_productos = tk.Label(ventana_productos, text="Gestión de Productos", font=("Helvetica", 14, "bold"), bg="#FFF8DC", fg="#8B4513")
    titulo_productos.pack(pady=10)

    # Agregar Producto
    def agregar_producto_func():
        ventana_agregar = Toplevel(ventana_productos)
        ventana_agregar.title("Agregar Producto")
        ventana_agregar.geometry("400x300")
        ventana_agregar.configure(bg="#FFF8DC")

        tk.Label(ventana_agregar, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(ventana_agregar, text="Categoría:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(ventana_agregar, text="Precio:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(ventana_agregar, text="Stock:").grid(row=3, column=0, padx=10, pady=5)

        nombre = tk.Entry(ventana_agregar)
        categoria = tk.Entry(ventana_agregar)
        precio = tk.Entry(ventana_agregar)
        stock = tk.Entry(ventana_agregar)

        nombre.grid(row=0, column=1, padx=10, pady=5)
        categoria.grid(row=1, column=1, padx=10, pady=5)
        precio.grid(row=2, column=1, padx=10, pady=5)
        stock.grid(row=3, column=1, padx=10, pady=5)

        def guardar_producto():
            try:
                agregar_producto(nombre.get(), categoria.get(), float(precio.get()), int(stock.get()))
                messagebox.showinfo("Éxito", "Producto agregado exitosamente")
                ventana_agregar.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el producto: {e}")

        tk.Button(ventana_agregar, text="Guardar Producto", command=guardar_producto).grid(row=4, column=0, columnspan=2, pady=10)

    # Ver Productos
    def ver_productos_func():
        ventana_ver = Toplevel(ventana_productos)
        ventana_ver.title("Ver Productos")
        ventana_ver.geometry("600x400")
        ventana_ver.configure(bg="#FFF8DC")

        listbox = tk.Listbox(ventana_ver, width=80, height=20)
        listbox.pack(pady=10)

        try:
            productos = ver_productos()  
            listbox.delete(0, tk.END)  

            if productos:  
                for producto in productos:
                    listbox.insert(
                        tk.END,
                        f"ID: {producto['id']}, Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, "
                        f"Precio: {producto['precio']:.2f}, Stock: {producto['stock']}"
                    )
            else:
                listbox.insert(tk.END, "No se encontraron productos.")  
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la lista de productos: {e}")

    # Actualizar Producto
    def actualizar_producto_func():
        ventana_actualizar = Toplevel(ventana_productos)
        ventana_actualizar.title("Actualizar Producto")
        ventana_actualizar.geometry("400x400")
        ventana_actualizar.configure(bg="#FFF8DC")

        tk.Label(ventana_actualizar, text="ID del Producto:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(ventana_actualizar, text="Nuevo Nombre:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(ventana_actualizar, text="Nueva Categoría:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(ventana_actualizar, text="Nuevo Precio:").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(ventana_actualizar, text="Nuevo Stock:").grid(row=4, column=0, padx=10, pady=5)

        producto_id = tk.Entry(ventana_actualizar)
        nuevo_nombre = tk.Entry(ventana_actualizar)
        nueva_categoria = tk.Entry(ventana_actualizar)
        nuevo_precio = tk.Entry(ventana_actualizar)
        nuevo_stock = tk.Entry(ventana_actualizar)

        producto_id.grid(row=0, column=1, padx=10, pady=5)
        nuevo_nombre.grid(row=1, column=1, padx=10, pady=5)
        nueva_categoria.grid(row=2, column=1, padx=10, pady=5)
        nuevo_precio.grid(row=3, column=1, padx=10, pady=5)
        nuevo_stock.grid(row=4, column=1, padx=10, pady=5)

        def guardar_cambios():
            try:
                actualizar_producto(
                    int(producto_id.get()),
                    nombre=nuevo_nombre.get(),
                    categoria=nueva_categoria.get(),
                    precio=float(nuevo_precio.get()),
                    stock=int(nuevo_stock.get())
                )
                messagebox.showinfo("Éxito", "Producto actualizado exitosamente")
                ventana_actualizar.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo actualizar el producto: {e}")

        tk.Button(ventana_actualizar, text="Guardar Cambios", command=guardar_cambios).grid(row=5, column=0, columnspan=2, pady=10)

    # Eliminar Producto
    def eliminar_producto_func():
        ventana_eliminar = Toplevel(ventana_productos)
        ventana_eliminar.title("Eliminar Producto")
        ventana_eliminar.geometry("400x200")
        ventana_eliminar.configure(bg="#FFF8DC")

        tk.Label(ventana_eliminar, text="ID del Producto a Eliminar:").grid(row=0, column=0, padx=10, pady=5)
        producto_id = tk.Entry(ventana_eliminar)
        producto_id.grid(row=0, column=1, padx=10, pady=5)

        def confirmar_eliminacion():
            try:
                eliminar_producto(int(producto_id.get()))
                messagebox.showinfo("Éxito", "Producto eliminado exitosamente")
                ventana_eliminar.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el producto: {e}")

        tk.Button(ventana_eliminar, text="Eliminar Producto", command=confirmar_eliminacion).grid(row=1, column=0, columnspan=2, pady=10)

    # Botones para cada funcionalidad
    tk.Button(ventana_productos, text="Agregar Producto", command=agregar_producto_func).pack(pady=10)
    tk.Button(ventana_productos, text="Ver Productos", command=ver_productos_func).pack(pady=10)
    tk.Button(ventana_productos, text="Actualizar Producto", command=actualizar_producto_func).pack(pady=10)
    tk.Button(ventana_productos, text="Eliminar Producto", command=eliminar_producto_func).pack(pady=10)

# --------------------------------------------------------
# -----------------(Gestión de Clientes)------------------
# --------------------------------------------------------
def gestion_clientes():
    ventana_clientes = Toplevel(root)
    ventana_clientes.title("Gestión de Clientes")
    ventana_clientes.geometry("500x400")
    ventana_clientes.configure(bg="#FFF8DC")

    titulo_clientes = tk.Label(ventana_clientes, text="Gestión de Clientes", font=("Helvetica", 14, "bold"), bg="#FFF8DC", fg="#8B4513")
    titulo_clientes.pack(pady=10)

    # Registrar cliente
    def registrar_cliente_func():
        ventana_registro = Toplevel(ventana_clientes)
        ventana_registro.title("Registrar Cliente")
        ventana_registro.geometry("400x300")
        ventana_registro.configure(bg="#FFF8DC")

        tk.Label(ventana_registro, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(ventana_registro, text="Email:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(ventana_registro, text="Teléfono:").grid(row=2, column=0, padx=10, pady=5)

        nombre = tk.Entry(ventana_registro)
        email = tk.Entry(ventana_registro)
        telefono = tk.Entry(ventana_registro)

        nombre.grid(row=0, column=1, padx=10, pady=5)
        email.grid(row=1, column=1, padx=10, pady=5)
        telefono.grid(row=2, column=1, padx=10, pady=5)

        def guardar_cliente():
            try:
                registrar_cliente(nombre.get(), email.get(), telefono.get())
                messagebox.showinfo("Éxito", "Cliente registrado exitosamente")
                ventana_registro.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo registrar el cliente: {e}")

        tk.Button(ventana_registro, text="Guardar Cliente", command=guardar_cliente).grid(row=3, column=0, columnspan=2, pady=10)

    # Actualizar cliente
    def actualizar_cliente_func():
        ventana_actualizar = Toplevel(ventana_clientes)
        ventana_actualizar.title("Actualizar Cliente")
        ventana_actualizar.geometry("400x300")
        ventana_actualizar.configure(bg="#FFF8DC")

        tk.Label(ventana_actualizar, text="ID del Cliente:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(ventana_actualizar, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(ventana_actualizar, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(ventana_actualizar, text="Teléfono:").grid(row=3, column=0, padx=10, pady=5)

        id_cliente = tk.Entry(ventana_actualizar)
        nombre = tk.Entry(ventana_actualizar)
        email = tk.Entry(ventana_actualizar)
        telefono = tk.Entry(ventana_actualizar)

        id_cliente.grid(row=0, column=1, padx=10, pady=5)
        nombre.grid(row=1, column=1, padx=10, pady=5)
        email.grid(row=2, column=1, padx=10, pady=5)
        telefono.grid(row=3, column=1, padx=10, pady=5)

        def guardar_actualizacion():
            try:
                actualizar_cliente(int(id_cliente.get()), nombre.get(), email.get(), telefono.get())
                messagebox.showinfo("Éxito", "Cliente actualizado exitosamente")
                ventana_actualizar.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo actualizar el cliente: {e}")

        tk.Button(ventana_actualizar, text="Actualizar Cliente", command=guardar_actualizacion).grid(row=4, column=0, columnspan=2, pady=10)

    # Ver clientes
    def ver_clientes_func():
        ventana_ver = Toplevel(ventana_clientes)
        ventana_ver.title("Lista de Clientes")
        ventana_ver.geometry("600x400")
        ventana_ver.configure(bg="#FFF8DC")

        listbox = tk.Listbox(ventana_ver, width=80, height=20)
        listbox.pack(pady=10)

        try:
            clientes = ver_clientes()
            listbox.delete(0, tk.END)
            if clientes:
                for cliente in clientes:
                    listbox.insert(
                        tk.END,
                        f"ID: {cliente['id']}, Nombre: {cliente['nombre']}, Correo: {cliente['correo']}, Teléfono: {cliente['telefono']}"
                    )
            else:
                listbox.insert(tk.END, "No se encontraron clientes registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los clientes: {e}")

    tk.Button(ventana_clientes, text="Registrar Cliente", command=registrar_cliente_func).pack(pady=10)
    tk.Button(ventana_clientes, text="Actualizar Cliente", command=actualizar_cliente_func).pack(pady=10)
    tk.Button(ventana_clientes, text="Ver Clientes", command=ver_clientes_func).pack(pady=10)

#--------------------------------------------------------
#---------------(Procesamiento de ordenes)---------------
#--------------------------------------------------------
def procesamiento_ordenes():
    ventana_ordenes = Toplevel(root)
    ventana_ordenes.title("Procesamiento de Órdenes")
    ventana_ordenes.geometry("500x400")
    ventana_ordenes.configure(bg="#FFF8DC")

    titulo_ordenes = tk.Label(ventana_ordenes, text="Procesamiento de Órdenes", font=("Helvetica", 14, "bold"), bg="#FFF8DC", fg="#8B4513")
    titulo_ordenes.grid(row=0, column=0, columnspan=2, pady=10)

    # ver ordenes de los clientes
    def ver_ordenes_por_cliente():
        cliente_id = simpledialog.askinteger("Ver Órdenes", "Ingrese el ID del cliente:")
        if cliente_id:
            ventana_ver = Toplevel(ventana_ordenes)
            ventana_ver.title("Órdenes del Cliente")
            ventana_ver.geometry("700x300")
            ventana_ver.configure(bg="#FFF8DC")

            listbox = tk.Listbox(ventana_ver, width=70, height=15)
            listbox.grid(row=1, column=0, padx=10, pady=10)

            try:
                ordenes = mostrar_ordenes_por_cliente(cliente_id)
                if ordenes:
                    for orden in ordenes:
                        listbox.insert(
                            tk.END,
                            f"ID: {orden['orden_id']}, Producto: {orden['producto']}, "
                            f"Categoría: {orden['categoria']}, Cantidad: {orden['cantidad']}, Fecha: {orden['fecha']}"
                        )
                else:
                    messagebox.showinfo("Sin Órdenes", f"No se encontraron órdenes para el cliente con ID {cliente_id}.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudieron cargar las órdenes: {e}")

    tk.Button(ventana_ordenes, text="Ver Órdenes por Cliente", command=ver_ordenes_por_cliente).grid(row=2, column=0, pady=10, sticky="ew")

#--------------------------------------------------------
#---------------(Busqueda Avanzada)----------------------
#--------------------------------------------------------
def busquedas_avanzadas():
    ventana_busquedas = Toplevel(root)
    ventana_busquedas.title("Búsquedas Avanzadas")
    ventana_busquedas.geometry("600x400")
    ventana_busquedas.configure(bg="#FFF8DC")

    titulo_busquedas = tk.Label(ventana_busquedas, text="Búsquedas Avanzadas", font=("Helvetica", 14, "bold"), bg="#FFF8DC", fg="#8B4513")
    titulo_busquedas.grid(row=0, column=0, columnspan=2, pady=10)

    subtitulo = tk.Label(ventana_busquedas, text="Selecciona el tipo de búsqueda:", font=("Helvetica", 12), bg="#FFF8DC", fg="#8B4513")
    subtitulo.grid(row=1, column=0, columnspan=2, pady=10)

    # Buscar Producto por Nombre
    def buscar_producto_por_nombre():
        ventana_producto = Toplevel(ventana_busquedas)
        ventana_producto.title("Buscar Producto por Nombre")
        ventana_producto.geometry("600x300")
        ventana_producto.configure(bg="#FFF8DC")

        tk.Label(ventana_producto, text="Nombre del Producto:").grid(row=0, column=0, padx=10, pady=5)
        entrada_nombre = tk.Entry(ventana_producto)
        entrada_nombre.grid(row=0, column=1, padx=10, pady=5)

        listbox_resultados = tk.Listbox(ventana_producto, width=60, height=15)
        listbox_resultados.grid(row=2, column=0, columnspan=2, pady=10)

        def buscar():
            nombre = entrada_nombre.get().strip()
            try:
                resultados = buscar_producto(nombre)  
                listbox_resultados.delete(0, tk.END) 
                if resultados:
                    for producto in resultados:
                        # Inserta cada producto como un string formateado
                        listbox_resultados.insert(
                            tk.END,
                            f"ID: {producto['id']}, Nombre: {producto['nombre']}, "
                            f"Categoría: {producto['categoria']}, Precio: ${producto['precio']:.2f}, "
                            f"Stock: {producto['stock']}"
                        )
                else:
                    listbox_resultados.insert(tk.END, "No se encontraron productos.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo realizar la búsqueda: {e}")

        tk.Button(ventana_producto, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

    # Buscar Cliente
    def buscar_cliente_por_filtro():
        ventana_cliente = Toplevel(ventana_busquedas)
        ventana_cliente.title("Buscar Cliente por Nombre o correo")
        ventana_cliente.geometry("600x300")
        ventana_cliente.configure(bg="#FFF8DC")

        tk.Label(ventana_cliente, text="Nombre o correo del Cliente:").grid(row=0, column=0, padx=10, pady=5)
        entrada_cliente = tk.Entry(ventana_cliente)
        entrada_cliente.grid(row=0, column=1, padx=10, pady=5)

        listbox_resultados = tk.Listbox(ventana_cliente, width=60, height=15)
        listbox_resultados.grid(row=2, column=0, columnspan=2, pady=10)

        def buscar():
            texto = entrada_cliente.get().strip()  
            try:
                resultados = buscar_cliente(texto)  
                listbox_resultados.delete(0, tk.END)
                if resultados:
                    for cliente in resultados:
                        # Inserta cada cliente como un string formateado
                        listbox_resultados.insert(
                            tk.END,
                            f"ID: {cliente['id']}, Nombre: {cliente['nombre']}, "
                            f"Correo: {cliente['correo']}, Teléfono: {cliente['telefono'] or 'N/A'}"
                        )
                else:
                    listbox_resultados.insert(tk.END, "No se encontraron clientes.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo realizar la búsqueda: {e}")

        tk.Button(ventana_cliente, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

    tk.Button(ventana_busquedas, text="Buscar Producto por Nombre", command=buscar_producto_por_nombre).grid(row=2, column=0, pady=10, sticky="ew")
    tk.Button(ventana_busquedas, text="Buscar Cliente por Nombre o correo", command=buscar_cliente_por_filtro).grid(row=4, column=0, pady=10, sticky="ew")

#--------------------------------------------------------
#----------------------(Reporte)-------------------------
#--------------------------------------------------------
def reportes():
    ventana_reportes = Toplevel(root)
    ventana_reportes.title("Reportes")
    ventana_reportes.geometry("600x400")
    ventana_reportes.configure(bg="#FFF8DC")

    titulo_reportes = tk.Label(ventana_reportes, text="Reportes", font=("Helvetica", 14, "bold"), bg="#FFF8DC", fg="#8B4513")
    titulo_reportes.pack(pady=10)

    # Productos más vendidos
    def mostrar_productos_mas_vendidos():
        ventana_mas_vendidos = Toplevel(ventana_reportes)
        ventana_mas_vendidos.title("Productos Más Vendidos")
        ventana_mas_vendidos.geometry("600x400")
        ventana_mas_vendidos.configure(bg="#FFF8DC")

        listbox_resultados = tk.Listbox(ventana_mas_vendidos, width=70, height=15)
        listbox_resultados.pack(pady=10)

        try:
            productos = productos_mas_vendidos() 
            if productos:
                for producto in productos:
                    listbox_resultados.insert(
                        tk.END,
                        f"Producto: {producto['producto']}, Categoría: {producto['categoria']}, "
                        f"Cantidad Vendida: {producto['cantidad_vendida']}"
                    )
            else:
                listbox_resultados.insert(tk.END, "No se encontraron productos más vendidos.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los productos más vendidos: {e}")

    tk.Button(ventana_reportes, text="Mostrar Productos Más Vendidos", command=mostrar_productos_mas_vendidos).pack(pady=10)

#--------------------------------------------------------
#---------(Modificar Producto y Ajustar Órdenes)---------
#--------------------------------------------------------
def ajustar_ordenes():
    ventana_ajustar = Toplevel(root)  
    ventana_ajustar.title("Ajustar Órdenes Relacionadas")
    ventana_ajustar.geometry("400x300")
    ventana_ajustar.configure(bg="#FFF8DC")

    tk.Label(ventana_ajustar, text="ID del Producto:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(ventana_ajustar, text="Nueva Cantidad Máxima:").grid(row=1, column=0, padx=10, pady=5)

    producto_id = tk.Entry(ventana_ajustar)
    cantidad_maxima = tk.Entry(ventana_ajustar)

    producto_id.grid(row=0, column=1, padx=10, pady=5)
    cantidad_maxima.grid(row=1, column=1, padx=10, pady=5)

    def actualizar_ordenes():
        try:
            resultado = modificar_ordenes_para_cantidad_maxima(int(producto_id.get()), int(cantidad_maxima.get()))
            messagebox.showinfo("Éxito", resultado) 
            ventana_ajustar.destroy() 
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron ajustar las órdenes: {e}")

    tk.Button(ventana_ajustar, text="Ajustar Órdenes", command=actualizar_ordenes).grid(row=2, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Ajustar Órdenes Relacionadas", command=ajustar_ordenes).grid(row=2, column=0, pady=10, sticky="ew")

# Crear los botones
crear_boton(contenedor_botones, "Gestionar Productos", gestion_productos)
crear_boton(contenedor_botones, "Gestionar Clientes", gestion_clientes)
crear_boton(contenedor_botones, "Procesamiento de ordenes", procesamiento_ordenes)
crear_boton(contenedor_botones, "Busqueda Avanzada", busquedas_avanzadas)
crear_boton(contenedor_botones, "Reportes", reportes)
crear_boton(contenedor_botones, "Modificar Productos y ajustar ordenes", ajustar_ordenes)
crear_boton(contenedor_botones, "Salir", salir)

# Iniciar la GUI principal
root.mainloop()