import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector

#Mira hice un ticket, si en dado caso crees que deba poner otra cosa dime y lo compongo. :)
def obtener_datos_ticket(telefono_cliente):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="expendio"
    )

    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT 
        C.Telefono_clien, 
        C.Nombres, 
        C.Apellido_p, 
        P.Nombre AS Producto, 
        P.Precio AS Precio_por_pieza, 
        DV.Cantidad, 
        (P.Precio * DV.Cantidad) AS Total_por_producto, 
        V.Fecha_Hora as Fecha, 
        E.Nombres as Nombre_empleado,  # Nombre completo del empleado
        E.Apellido_p as Apellido_empleado,  # Apellido del empleado
        E.RFC_emp as RFC
    FROM Venta V
    JOIN Cliente C ON V.Telefono_clien = C.Telefono_clien
    JOIN Detalle_venta DV ON V.Id_ven = DV.Id_ven
    JOIN Producto P ON DV.Id_prod = P.Id_prod
    JOIN Empleado E ON V.RFC_emp = E.RFC_emp
    WHERE C.Telefono_clien = %s
    ORDER BY V.Fecha_Hora DESC;
    """

    cursor.execute(consulta, (telefono_cliente,))
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    return resultados

def mostrar_ticket(telefono_cliente):
    productos = obtener_datos_ticket(telefono_cliente)

    root = tk.Tk()
    root.title("Ticket de Compra")
    root.geometry("450x600")
    root.configure(bg="white")

    root.resizable(False, False)

    canvas = tk.Canvas(root, bg="white", width=450, height=600)
    canvas.pack(fill="both", expand=True)

    img = Image.open("logo.jpg")
    img = img.resize((70, 70))
    img_tk = ImageTk.PhotoImage(img)

    root.img_tk = img_tk

    canvas.create_image(20, 10, image=img_tk, anchor="nw")
    canvas.create_text(100, 35, text="Tasso", font=("Arial", 16, "bold"), anchor="w")

    canvas.create_line(20, 80, 430, 80, fill="black", width=2)

    y_offset = 100
    cliente_telefono = productos[0]["Telefono_clien"]
    canvas.create_text(225, y_offset, text=f"Bienvenido: {cliente_telefono}", font=("Arial", 12, "bold"), anchor="center")

    y_offset += 40

    canvas.create_text(20, y_offset, text="Producto", font=("Arial", 10, "bold"), anchor="nw")
    canvas.create_text(200, y_offset, text="Cantidad", font=("Arial", 10, "bold"), anchor="nw")
    canvas.create_text(300, y_offset, text="Precio", font=("Arial", 10, "bold"), anchor="nw")
    canvas.create_text(400, y_offset, text="Total", font=("Arial", 10, "bold"), anchor="nw")

    y_offset += 20

    for producto in productos:
        nombre_producto = producto["Producto"]
        max_length = 20
        nombre_lineas = [nombre_producto[i:i + max_length] for i in range(0, len(nombre_producto), max_length)]

        for linea in nombre_lineas:
            canvas.create_text(20, y_offset, text=linea, font=("Arial", 10), anchor="nw")
            y_offset += 15
        y_offset -= 15 * len(nombre_lineas)
        canvas.create_text(200, y_offset, text=str(producto["Cantidad"]), font=("Arial", 10), anchor="nw")
        canvas.create_text(300, y_offset, text=str(producto["Precio_por_pieza"]), font=("Arial", 10), anchor="nw")
        canvas.create_text(400, y_offset, text=str(producto["Total_por_producto"]), font=("Arial", 10), anchor="nw")
        y_offset += 20 + (15 * (len(nombre_lineas) - 1))
    total_final = sum([producto["Total_por_producto"] for producto in productos])

    canvas.create_line(20, y_offset, 430, y_offset, fill="black", width=2)
    y_offset += 20
    canvas.create_text(300, y_offset, text="Total: $", font=("Arial", 12, "bold"), anchor="nw")
    canvas.create_text(400, y_offset, text=str(total_final), font=("Arial", 12, "bold"), anchor="nw")

    empleado_nombre = productos[0]["Nombre_empleado"] + " " + productos[0]["Apellido_empleado"]
    empleado_rfc = productos[0]["RFC"]
    y_offset += 40
    canvas.create_text(20, y_offset, text="Empleado: " + empleado_nombre, font=("Arial", 10), anchor="nw")
    y_offset += 20
    canvas.create_text(20, y_offset, text="RFC: " + empleado_rfc, font=("Arial", 10), anchor="nw")

    fecha = productos[0]["Fecha"].strftime("%Y-%m-%d %H:%M:%S")
    y_offset += 20
    canvas.create_text(20, y_offset, text="Fecha: " + fecha, font=("Arial", 10), anchor="nw")

    y_offset += 40
    canvas.create_text(225, y_offset, text="Gracias por su compra", font=("Arial", 12, "bold"), anchor="center")
    y_offset += 20
    canvas.create_text(225, y_offset, text="Vuelva pronto", font=("Arial", 12, "bold"), anchor="center")

    root.mainloop()
mostrar_ticket('5554567890')
