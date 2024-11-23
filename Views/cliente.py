import customtkinter as ctk
import mysql.connector
from tkinter import ttk  # Importamos ttk para Treeview

def obtener_clientes():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="expendio"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT Telefono_clien, Nombres, Apellido_p, Apellido_m FROM Cliente")
        clientes = cursor.fetchall()
        return clientes
    except mysql.connector.Error as err:
        ctk.CTkMessageBox("Error", f"Error al conectar a la base de datos: {err}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def obtener_compras(telefono_cliente):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="expendio"
        )
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT V.Id_ven, V.Fecha_Hora, P.Nombre, DV.Cantidad, P.Precio, 
                   (DV.Cantidad * P.Precio) AS Total
            FROM Venta V
            JOIN Detalle_venta DV ON V.Id_ven = DV.Id_ven
            JOIN Producto P ON DV.Id_prod = P.Id_prod
            WHERE V.Telefono_clien = %s
        """, (telefono_cliente,))
        compras = cursor.fetchall()
        return compras
    except mysql.connector.Error as err:
        ctk.CTkMessageBox("Error", f"Error al conectar a la base de datos: {err}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def ventana_editar_cliente(cliente):
    def guardar_cambios():
        nuevo_telefono = entry_telefono.get()
        nuevo_nombre = entry_nombre.get()
        nuevo_apellido_p = entry_apellido_p.get()
        nuevo_apellido_m = entry_apellido_m.get()

        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="expendio"
            )
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE Cliente
                SET Telefono_clien = %s, Nombres = %s, Apellido_p = %s, Apellido_m = %s
                WHERE Telefono_clien = %s
            """, (nuevo_telefono, nuevo_nombre, nuevo_apellido_p, nuevo_apellido_m, cliente[0]))
            conexion.commit()
            ctk.CTkMessageBox("Éxito", "Datos del cliente actualizados correctamente.")
            ventana_editar.destroy()
        except mysql.connector.Error as err:
            ctk.CTkMessageBox("Error", f"Error al actualizar los datos: {err}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    ventana_editar = ctk.CTkToplevel()
    ventana_editar.title("Editar Cliente")
    ventana_editar.geometry("400x300")
    ventana_editar.configure(bg="#f5f6fa")  # Fondo blanco perla para esta ventana

    ctk.CTkLabel(ventana_editar, text="Editar Cliente", font=("Arial", 16)).pack(pady=10)

    ctk.CTkLabel(ventana_editar, text="Teléfono:").pack(anchor="w", padx=20, pady=5)
    entry_telefono = ctk.CTkEntry(ventana_editar)
    entry_telefono.insert(0, cliente[0])
    entry_telefono.pack(fill="x", padx=20)

    ctk.CTkLabel(ventana_editar, text="Nombre:").pack(anchor="w", padx=20, pady=5)
    entry_nombre = ctk.CTkEntry(ventana_editar)
    entry_nombre.insert(0, cliente[1])
    entry_nombre.pack(fill="x", padx=20)

    ctk.CTkLabel(ventana_editar, text="Apellido Paterno:").pack(anchor="w", padx=20, pady=5)
    entry_apellido_p = ctk.CTkEntry(ventana_editar)
    entry_apellido_p.insert(0, cliente[2])
    entry_apellido_p.pack(fill="x", padx=20)

    ctk.CTkLabel(ventana_editar, text="Apellido Materno:").pack(anchor="w", padx=20, pady=5)
    entry_apellido_m = ctk.CTkEntry(ventana_editar)
    entry_apellido_m.insert(0, cliente[3])
    entry_apellido_m.pack(fill="x", padx=20)

    btn_guardar = ctk.CTkButton(ventana_editar, text="Guardar Cambios", command=guardar_cambios)
    btn_guardar.pack(pady=20)

def ventana_cliente():
    def cargar_compras(event):
        seleccion = lista_clientes.selection()
        if seleccion:
            telefono_cliente = lista_clientes.item(seleccion[0], "values")[0]
            compras = obtener_compras(telefono_cliente)
            for item in lista_compras.get_children():
                lista_compras.delete(item)
            for idx, compra in enumerate(compras):
                tag = "evenrow" if idx % 2 == 0 else "oddrow"
                lista_compras.insert("", "end", values=compra, tags=(tag,))

    def abrir_editar_cliente(event):
        item = lista_clientes.identify_row(event.y)  # Detectar la fila en la que se hizo clic
        if item:
            valores = lista_clientes.item(item, "values")
            columna = lista_clientes.identify_column(event.x)  # Obtener la columna clickeada
            if columna == "#5":  # Si se hizo clic en la columna "Editar" (columna 5, la de los "...")
                ventana_editar_cliente(valores[:-1])  # Pasamos los datos del cliente (sin el '...')
            else:
                telefono_cliente = valores[0]
                compras = obtener_compras(telefono_cliente)
                for item in lista_compras.get_children():
                    lista_compras.delete(item)
                for idx, compra in enumerate(compras):
                    tag = "evenrow" if idx % 2 == 0 else "oddrow"
                    lista_compras.insert("", "end", values=compra, tags=(tag,))

    ventana = ctk.CTk()
    ctk.set_appearance_mode("light")
    ventana.title("Clientes")
    ventana.geometry("800x600")
    ventana.configure(bg="#f5f6fa")  # Fondo blanco perla para esta ventana

    ctk.CTkLabel(ventana, text="Clientes", font=("Arial", 18)).pack(pady=10)

    frame_clientes = ctk.CTkFrame(ventana)
    frame_clientes.pack(fill=ctk.BOTH, padx=20, pady=10)

    scrollbar_clientes = ctk.CTkScrollbar(frame_clientes)
    scrollbar_clientes.pack(side=ctk.RIGHT, fill=ctk.Y)

    columnas_clientes = ("Teléfono", "Nombre", "Apellido Paterno", "Apellido Materno", "Editar")
    lista_clientes = ttk.Treeview(frame_clientes, columns=columnas_clientes, show="headings", height=10, yscrollcommand=scrollbar_clientes.set)
    for col in columnas_clientes:
        lista_clientes.heading(col, text=col)
    lista_clientes.pack(fill=ctk.BOTH, expand=True)
    scrollbar_clientes.configure(command=lista_clientes.yview)

    lista_clientes.tag_configure("evenrow", background="#f0f8ff")  # Azul claro
    lista_clientes.tag_configure("oddrow", background="#ffffff")   # Blanco

    clientes = obtener_clientes()
    for idx, cliente in enumerate(clientes):
        tag = "evenrow" if idx % 2 == 0 else "oddrow"
        lista_clientes.insert("", "end", values=cliente + ("...",), tags=(tag,))

    lista_clientes.bind("<ButtonRelease-1>", abrir_editar_cliente)

    frame_compras = ctk.CTkFrame(ventana)
    frame_compras.pack(fill=ctk.BOTH, padx=20, pady=10)

    scrollbar_compras = ctk.CTkScrollbar(frame_compras)
    scrollbar_compras.pack(side=ctk.RIGHT, fill=ctk.Y)

    columnas_compras = ("ID Venta", "Fecha", "Producto", "Cantidad", "Precio por pieza", "Total")
    lista_compras = ttk.Treeview(frame_compras, columns=columnas_compras, show="headings", height=10, yscrollcommand=scrollbar_compras.set)
    for col in columnas_compras:
        lista_compras.heading(col, text=col)
    lista_compras.pack(fill=ctk.BOTH, expand=True)
    scrollbar_compras.configure(command=lista_compras.yview)

    lista_compras.tag_configure("evenrow", background="#f0f8ff")
    lista_compras.tag_configure("oddrow", background="#ffffff")

    ventana.mainloop()

if __name__ == "__main__":
    ventana_cliente()
