use Expendio;

INSERT INTO Sucursal (RFC_suc, Correo_suc, Telefono_suc, Direccion_suc) VALUES
('RFC001234567', 'sucursal1@ejemplo.com', '5551234567', 'Calle 123, Ciudad A'),
('RFC002345678', 'sucursal2@ejemplo.com', '5552345678', 'Avenida Siempre Viva 456, Ciudad B'),
('RFC003456789', 'sucursal3@ejemplo.com', '5553456789', 'Boulevard de los Sueños Rotos 789, Ciudad C');
select * from Sucursal;

INSERT INTO Empleado (
    RFC_emp, Nombres, Apellido_P, Apellido_M, Puesto, Correo_emp, Telefono_emp, Direccion_emp, 
    Fecha_nacimiento, Contraseña_emp, Fecha_ingreso, Fecha_baja, RFC_suc
) VALUES
('ABC123456789', 'Juan', 'Pérez', 'García', 'E', 'juan.perez@example.com', '5551234567', 'Calle Sol 123', 
 '1985-05-15', 'Juan150585', '2023-05-12', NULL, 'RFC001234567'),
('DEF987654321', 'María', 'López', 'Hernández', 'T', 'maria.lopez@example.com', '5557654321', 'Avenida Siempre Viva 742', 
 '1990-08-22', 'Maria220890', '2022-11-10', NULL, 'RFC001234567'),
('GHI456789012', 'Carlos', 'Martínez', 'Sánchez', 'T', 'carlos.martinez@example.com', '5552345678', 'Boulevard de los Sueños 456', 
 '1988-12-30', 'Carlos301288', '2023-03-15', NULL, 'RFC001234567'),
('JKL321654987', 'Ana', 'Gómez', 'Torres', 'S', 'ana.gomez@example.com', '5558765432', 'Calle de la Amistad 789', 
 '1995-03-10', 'Ana100395', '2021-09-22', NULL, 'RFC002345678'),
('MNO654321098', 'Luis', 'Ramírez', 'Vázquez', 'T', 'luis.ramirez@example.com', '5553456789', 'Calle del Sol 101', 
 '1982-11-05', 'Luis051182', '2022-06-30', NULL, 'RFC002345678'),
('PQR987123456', 'Sofía', 'Reyes', 'Molina', 'T', 'sofia.reyes@example.com', '5554567890', 'Calle de la Luna 202', 
 '1993-07-19', 'Sofia190793', '2023-01-25', NULL, 'RFC002345678'),
('STU123456789', 'Diego', 'Hernández', 'Pérez', 'E', 'diego.hernandez@example.com', '5555678901', 'Calle del Río 303', 
 '1980-02-14', 'Diego140280', '2021-11-03', NULL, 'RFC003456789'),
('VWX456789123', 'Valeria', 'Cruz', 'Jiménez', 'T', 'valeria.cruz@example.com', '5556789012', 'Calle de la Paz 404', 
 '1992-09-25', 'Valeria250992', '2023-07-18', NULL, 'RFC003456789'),
('YZA789123456', 'Fernando', 'Morales', 'Salazar', 'T', 'fernando.morales@example.com', '5557890123', 'Calle del Mar 505', 
 '1987-04-18', 'Fernand180487', '2022-04-12', NULL, 'RFC003456789');

select * from Empleado;

INSERT INTO Proveedor (RFC_prov, Correo_prov, Telefono_prov, Direccion_prov) VALUES
('RFCPROV001', 'proveedor1@ejemplo.com', '5556667788', 'Calle Proveedor 1, Ciudad A'),
('RFCPROV002', 'proveedor2@ejemplo.com', '5557778899', 'Avenida Proveedor 2, Ciudad B'),
('RFCPROV003', 'proveedor3@ejemplo.com', '5558889900', 'Boulevard Proveedor 3, Ciudad C'),
('RFCPROV004', 'proveedor4@ejemplo.com', '5559990011', 'Plaza Proveedor 4, Ciudad D'),
('RFCPROV005', 'proveedor5@ejemplo.com', '5560001122', 'Camino Proveedor 5, Ciudad E');
select * from Proveedor;

INSERT INTO Producto (Id_prod, Existencia, Precio, Nombre, Fecha_cad) VALUES
('PAN001', 4, 20, 'Pan Blanco - Empaque de 10 unidades', '2024-12-31'),
('PAN002', 23, 25, 'Pan Integral - Empaque de 8 unidades', '2024-11-15'),
('PAN003', 2, 30, 'Pan de Centeno - Empaque de 6 unidades', '2024-10-20'),
('PAN004', 23, 22, 'Pan de Ajo - Empaque de 4 unidades', '2024-09-10'),
('PAN005', 12, 18, 'Pan de Molde - Empaque de 12 unidades', '2024-12-01'),
('PAN006', 22, 28, 'Pan de Hot Dog - Empaque de 10 unidades', '2024-11-30'),
('PAN007', 15, 15, 'Pan de Hamburguesa - Empaque de 8 unidades', '2024-10-05'),
('PAN008', 16, 27, 'Pan de Pasas - Empaque de 5 unidades', '2024-09-15'),
('PAN009', 15, 32, 'Pan de Chocolate - Individual', '2024-08-25'),
('PAN010', 26, 19, 'Pan de Semillas - Individual', '2024-11-05'),
('PAN011', 25, 26, 'Pan de Frutas - Individual', '2024-10-30'),
('PAN012', 26, 12, 'Pan de Mantequilla - Individual', '2024-09-01'),
('PAN013', 13, 15, 'Pan de Limón - Individual', '2024-10-15'),
('PAN014', 16, 18, 'Pan de Nuez - Individual', '2024-11-20'),
('PAN015', 17, 20, 'Pan de Aceitunas - Individual', '2024-12-05'),
('PAN016', 16, 22, 'Pan de Espelta - Individual', '2024-11-10'),
('PAN017', 14, 24, 'Pan de Cebolla - Individual', '2024-10-25');
select * from Producto;

INSERT INTO Cliente (Telefono_clien, Fecha_nacimiento, Sexo, Nombres, Apellido_p, Apellido_m) VALUES
('5551234567', '1999-05-15', 'M', 'Juan', 'Pérez', 'García'),
('5552345678', '1994-08-22', 'F', 'María', 'López', 'Hernández'),
('5553456789', '2001-12-30', 'M', 'Carlos', 'Martínez', 'Sánchez'),
('5554567890', '1996-03-10', 'F', 'Ana', 'Gómez', 'Torres'),
('5555678901', '1989-11-05', 'M', 'Luis', 'Ramírez', 'Vázquez'),
('5556789012', '1984-07-19', 'F', 'Sofía', 'Reyes', 'Molina'),
('5557890123', '1995-02-14', 'M', 'Diego', 'Hernández', 'Pérez'),
('5558901234', '1991-09-25', 'F', 'Valeria', 'Cruz', 'Jiménez'),
('5559012345', '1996-04-18', 'M', 'Fernando', 'Morales', 'Salazar'),
('5550123456', '1993-01-30', 'F', 'Lucía', 'Fernández', 'Díaz'),
('5551234568', '1998-10-12', 'M', 'Javier', 'Torres', 'Mendoza'),
('5552345679', '1997-06-15', 'F', 'Claudia', 'Jiménez', 'Ríos'),
('5553456790', '1986-12-20', 'M', 'Ricardo', 'García', 'López'),
('5554567891', '1982-05-25', 'F', 'Patricia', 'Sánchez', 'Moreno'),
('5555678902', '2002-03-30', 'M', 'Andrés', 'Ramírez', 'Salas'),
('5556789013', '1990-08-10', 'F', 'Teresa', 'Cruz', 'Pérez'),
('5557890124', '1995-11-22', 'M', 'Eduardo', 'Hernández', 'González'),
('5558901235', '1994-07-19', 'F', 'Marisol', 'Reyes', 'Maldonado'),
('5559012346', '2000-02-28', 'M', 'Oscar', 'Martínez', 'Cordero'),
('5550123457', '1993-09-15', 'F', 'Gabriela', 'López', 'Soto'),
('5551234569', '1995-04-05', 'M', 'Alberto', 'Pérez', 'Rojas'),
('5552345680', '1987-10-30', 'F', 'Verónica', 'González', 'Salazar'),
('5553456791', '1998-01-12', 'M', 'Hugo', 'Morales', 'Vega'),
('5554567892', '1981-06-18', 'F', 'Silvia', 'Torres', 'Cruz'),
('5555678903', '2003-03-14', 'M', 'Raúl', 'Sánchez', 'Hernández'),
('5556789014', '1992-12-01', 'F', 'Nadia', 'Reyes', 'Mendoza'),
('5557890125', '1996-05-22', 'M', 'Pablo', 'García', 'López'),
('5558901236', '1988-09-30', 'F', 'Carmen', 'Martínez', 'Salas'),
('5559012347', '1999-02-14', 'M', 'Sergio', 'Ramírez', 'Díaz'),
('5550123458', '1991-11-11', 'F', 'Elena', 'Cruz', 'Moreno'),
('5551234570', '1995-07-07', 'M', 'Felipe', 'Hernández', 'González'),
('5552345681', '1985-03-03', 'F', 'Mónica', 'López', 'Ríos'),
('5553456792', '1997-10-10', 'M', 'Jorge', 'Pérez', 'Salazar'),
('5554567893', '1980-04-25', 'F', 'Ana', 'Sánchez', 'Maldonado');
select count(*) as total from Cliente;

INSERT INTO Compra (Id_com, RFC_prov, RFC_suc, Fecha_Hora) VALUES
('COM001', 'RFCPROV001', 'RFC003456789', '2024-10-12 10:30:00'),
('COM002', 'RFCPROV004', 'RFC001234567', '2024-10-13 11:00:00'),
('COM003', 'RFCPROV005', 'RFC002345678', '2024-10-13 12:45:00'),
('COM004', 'RFCPROV003', 'RFC002345678', '2024-10-14 09:15:00'),
('COM005', 'RFCPROV001', 'RFC003456789', '2024-10-14 14:30:00'),
('COM006', 'RFCPROV002', 'RFC001234567', '2024-10-15 16:00:00');
select * from Compra;

INSERT INTO Detalle_compra (Id_detalleCom, Id_com, Id_prod, Cantidad) VALUES 
('D001', 'COM001', 'PAN010', 20),  
('D002', 'COM001', 'PAN012', 15), 
('D003', 'COM001', 'PAN007', 13),
('D004', 'COM002', 'PAN001', 11),
('D005', 'COM002', 'PAN013', 33),
('D006', 'COM002', 'PAN015', 23),
('D007', 'COM003', 'PAN016', 33),
('D008', 'COM003', 'PAN009', 14),
('D009', 'COM003', 'PAN002', 19),
('D010', 'COM004', 'PAN017', 12),
('D011', 'COM004', 'PAN002', 21),
('D012', 'COM004', 'PAN004', 16),
('D013', 'COM005', 'PAN006', 14),
('D014', 'COM005', 'PAN009', 17),
('D015', 'COM005', 'PAN002', 18),
('D016', 'COM006', 'PAN016', 10),
('D017', 'COM006', 'PAN002', 15),
('D018', 'COM006', 'PAN004', 19);  	
SELECT * FROM Detalle_Compra;
       
INSERT INTO Venta (Id_ven, Telefono_clien, RFC_emp, Fecha_Hora) VALUES
('VEN001', '5551234567', 'ABC123456789', '2024-10-05 10:30:00'),
('VEN002', '5552345678', 'DEF987654321', '2024-10-10 12:45:00'),
('VEN003', '5553456789', 'GHI456789012', '2024-10-12 15:20:00'),
('VEN004', '5554567890', 'JKL321654987', '2024-10-01 09:10:00'),
('VEN005', '5555678901', 'MNO654321098', '2024-10-14 11:15:00'),
('VEN006', '5556789012', 'PQR987123456', '2024-10-03 16:45:00'),
('VEN007', '5557890123', 'STU123456789', '2024-10-04 13:00:00'),
('VEN008', '5558901234', 'VWX456789123', '2024-10-02 14:35:00'),
('VEN009', '5559012345', 'YZA789123456', '2024-10-06 17:50:00'),
('VEN010', '5550123456', 'ABC123456789', '2024-10-08 18:20:00'),
('VEN011', '5551234568', 'DEF987654321', '2024-10-15 19:10:00'),
('VEN012', '5552345679', 'GHI456789012', '2024-10-05 12:00:00'),
('VEN013', '5553456790', 'JKL321654987', '2024-10-11 08:15:00'),
('VEN014', '5554567891', 'MNO654321098', '2024-10-13 10:45:00'),
('VEN015', '5555678902', 'PQR987123456', '2024-10-07 09:50:00'),
('VEN016', '5556789013', 'STU123456789', '2024-10-09 11:30:00'),
('VEN017', '5557890124', 'VWX456789123', '2024-10-04 16:55:00'),
('VEN018', '5558901235', 'YZA789123456', '2024-10-02 14:10:00'),
('VEN019', '5559012346', 'ABC123456789', '2024-10-12 08:05:00'),
('VEN020', '5550123457', 'DEF987654321', '2024-10-06 12:40:00'),
('VEN021', '5551234567', 'GHI456789012', '2024-10-09 10:20:00'),
('VEN022', '5552345678', 'JKL321654987', '2024-10-11 11:50:00'),
('VEN023', '5553456789', 'MNO654321098', '2024-10-15 15:35:00'),
('VEN024', '5554567890', 'PQR987123456', '2024-10-13 09:00:00'),
('VEN025', '5555678901', 'STU123456789', '2024-10-30 13:15:00'),
('VEN026', '5556789012', 'VWX456789123', '2024-10-28 14:45:00'),
('VEN027', '5557890123', 'YZA789123456', '2024-10-14 10:50:00'),
('VEN028', '5558901234', 'ABC123456789', '2024-10-18 12:10:00'),
('VEN029', '5559012345', 'DEF987654321', '2024-10-29 15:25:00'),
('VEN030', '5550123456', 'GHI456789012', '2024-10-10 12:30:00'),
('VEN031', '5551234568', 'JKL321654987', '2024-10-12 14:15:00'),
('VEN032', '5552345679', 'MNO654321098', '2024-10-03 09:30:00'),
('VEN033', '5553456790', 'PQR987123456', '2024-10-25 16:05:00'),
('VEN034', '5554567891', 'STU123456789', '2024-10-19 11:20:00'),
('VEN035', '5555678902', 'VWX456789123', '2024-10-01 17:00:00'),
('VEN036', '5556789013', 'YZA789123456', '2024-10-15 10:15:00'),
('VEN037', '5557890124', 'ABC123456789', '2024-10-05 08:45:00'),
('VEN038', '5558901235', 'DEF987654321', '2024-10-20 15:55:00'),
('VEN039', '5559012346', 'GHI456789012', '2024-10-17 12:30:00'),
('VEN040', '5550123457', 'JKL321654987', '2024-10-22 14:00:00');
SELECT * FROM Venta;
/*Venta 2*/
INSERT INTO Venta (Id_ven, Telefono_clien, RFC_emp, Fecha_Hora) VALUES
('VEN041', '5550123458', 'ABC123456789', '2024-11-17 10:00:00'),
('VEN042', '5551234569', 'DEF987654321', '2024-11-17 10:30:00'),
('VEN043', '5551234570', 'GHI456789012', '2024-11-17 11:00:00'),
('VEN044', '5552345680', 'JKL321654987', '2024-11-17 11:30:00'),
('VEN045', '5552345681', 'MNO654321098', '2024-11-17 12:00:00'),
('VEN046', '5553456791', 'PQR987123456', '2024-11-17 12:30:00'),
('VEN047', '5553456792', 'STU123456789', '2024-11-17 13:00:00'),
('VEN048', '5554567892', 'VWX456789123', '2024-11-17 13:30:00'),
('VEN049', '5554567893', 'YZA789123456', '2024-11-17 14:00:00'),
('VEN050', '5555678903', 'ABC123456789', '2024-11-17 14:30:00'),
('VEN051', '5556789014', 'DEF987654321', '2024-11-17 15:00:00'),
('VEN052', '5557890125', 'GHI456789012', '2024-11-17 15:30:00'),
('VEN053', '5558901236', 'JKL321654987', '2024-11-17 16:00:00'),
('VEN054', '5559012347', 'MNO654321098', '2024-11-17 16:30:00');
SELECT * FROM Venta;

INSERT INTO Detalle_venta (Id_detalleVen, Id_prod, Id_ven, Cantidad) VALUES
('DV001', 'PAN001', 'VEN001', 2),
('DV002', 'PAN002', 'VEN002', 1),
('DV003', 'PAN003', 'VEN003', 3),
('DV004', 'PAN004', 'VEN004', 4),
('DV005', 'PAN005', 'VEN005', 2),
('DV006', 'PAN006', 'VEN006', 3),
('DV007', 'PAN007', 'VEN007', 2),
('DV008', 'PAN008', 'VEN008', 1),
('DV009', 'PAN009', 'VEN009', 2),
('DV010', 'PAN010', 'VEN010', 4),
('DV011', 'PAN011', 'VEN011', 3),
('DV012', 'PAN012', 'VEN012', 2),
('DV013', 'PAN013', 'VEN013', 1),
('DV014', 'PAN014', 'VEN014', 3),
('DV015', 'PAN015', 'VEN015', 2),
('DV016', 'PAN016', 'VEN016', 1),
('DV017', 'PAN017', 'VEN017', 2),
('DV018', 'PAN001', 'VEN018', 4),
('DV019', 'PAN002', 'VEN019', 2),
('DV020', 'PAN003', 'VEN020', 3),
('DV021', 'PAN004', 'VEN021', 1),
('DV022', 'PAN005', 'VEN022', 4),
('DV023', 'PAN006', 'VEN023', 3),
('DV024', 'PAN007', 'VEN024', 2),
('DV025', 'PAN008', 'VEN025', 1),
('DV026', 'PAN009', 'VEN026', 2),
('DV027', 'PAN010', 'VEN027', 1),
('DV028', 'PAN011', 'VEN028', 4),
('DV029', 'PAN012', 'VEN029', 3),
('DV030', 'PAN013', 'VEN030', 2),
('DV031', 'PAN014', 'VEN031', 1),
('DV032', 'PAN015', 'VEN032', 4),
('DV033', 'PAN016', 'VEN033', 3),
('DV034', 'PAN017', 'VEN034', 2),
('DV035', 'PAN001', 'VEN035', 1),
('DV036', 'PAN002', 'VEN036', 4),
('DV037', 'PAN003', 'VEN037', 3),
('DV038', 'PAN004', 'VEN038', 2),
('DV039', 'PAN005', 'VEN039', 1),
('DV040', 'PAN006', 'VEN040', 3);
select * from Detalle_Venta;
/*Detalle de venta2*/
INSERT INTO Detalle_venta (Id_detalleVen, Id_prod, Id_ven, Cantidad) VALUES
('DV041', 'PAN001', 'VEN041', 2),
('DV042', 'PAN002', 'VEN042', 1),
('DV043', 'PAN003', 'VEN043', 3),
('DV044', 'PAN004', 'VEN044', 2),
('DV045', 'PAN005', 'VEN045', 4),
('DV046', 'PAN006', 'VEN046', 3),
('DV047', 'PAN007', 'VEN047', 2),
('DV048', 'PAN008', 'VEN048', 1),
('DV049', 'PAN009', 'VEN049', 2),
('DV050', 'PAN010', 'VEN050', 3),
('DV051', 'PAN011', 'VEN051', 4),
('DV052', 'PAN012', 'VEN052', 2),
('DV053', 'PAN013', 'VEN053', 3),
('DV054', 'PAN014', 'VEN054', 1);
SELECT * FROM Detalle_venta;
UPDATE Empleado
SET Puesto = 'E'
WHERE RFC_emp = 'JKL321654987';
