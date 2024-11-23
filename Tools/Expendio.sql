/* drop database expendio; */
 drop database Expendio; 
create database Expendio;
use Expendio;

CREATE TABLE Sucursal(
	RFC_suc VARCHAR(13) PRIMARY KEY NOT NULL,
	Correo_suc VARCHAR(255) NOT NULL,
	Telefono_suc VARCHAR(13) NOT NULL,
	Direccion_suc VARCHAR(100)NOT NULL
);
describe Sucursal;
CREATE TABLE Proveedor (
    RFC_prov VARCHAR(13) PRIMARY KEY NOT NULL,
    Nombre_prov VARCHAR(25),
    Correo_prov VARCHAR(30) NOT NULL,
    Telefono_prov VARCHAR(13) NOT NULL,
    Direccion_prov VARCHAR(100) NOT NULL
);
describe Proveedor;
CREATE TABLE Producto (
    Id_prod VARCHAR(20) PRIMARY KEY NOT NULL,
    Existencia SMALLINT NOT NULL,
    Precio FLOAT NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Fecha_cad Date NOT NULL
);
describe Producto;

CREATE TABLE Cliente (
    Telefono_clien VARCHAR(13) PRIMARY KEY NOT NULL,
    Fecha_nacimiento  DATE NOT NULL,
    Sexo CHAR(1) NOT NULL,
    Nombres VARCHAR(30) NOT NULL,
    Apellido_p VARCHAR(30) NOT NULL,
    Apellido_m VARCHAR(30) NOT NULL,
    Fecha_ingreso DATE
);
describe Cliente;

CREATE TABLE Empleado (
    RFC_emp VARCHAR(13) PRIMARY KEY NOT NULL,
    Nombres VARCHAR(30) NOT NULL,
    Apellido_P VARCHAR(30) NOT NULL,
    Apellido_M VARCHAR(30) NOT NULL,
    Puesto CHAR(1) NOT NULL,
    Correo_emp VARCHAR(30) NOT NULL,
    Telefono_emp VARCHAR(13) NOT NULL,
    Direccion_emp VARCHAR(100) NOT NULL,
    Fecha_nacimiento  DATE NOT NULL,
    Contraseña_emp VARCHAR(15) NOT NULL,
    Fecha_ingreso DATE,
    Fecha_baja DATE,
    RFC_suc VARCHAR(13) NOT NULL,
    FOREIGN KEY (RFC_suc) REFERENCES Sucursal(RFC_suc)
);

CREATE TABLE Compra (
    Id_com VARCHAR(20) PRIMARY KEY NOT NULL,
    RFC_prov VARCHAR(13) NOT NULL,
    RFC_suc VARCHAR(13) NOT NULL,
    Fecha_Hora DATETIME NOT NULL,
    FOREIGN KEY (RFC_prov) REFERENCES Proveedor(RFC_prov),
    FOREIGN KEY (RFC_suc) REFERENCES Sucursal(RFC_suc)
);

CREATE TABLE Detalle_compra (
    Id_detalleCom VARCHAR(20) PRIMARY KEY NOT NULL,
    Id_com VARCHAR(20) NOT NULL,
    Id_prod VARCHAR(20) NOT NULL,
    Cantidad TINYINT NOT NULL,
    FOREIGN KEY (Id_com) REFERENCES Compra(Id_com),
    FOREIGN KEY (Id_prod) REFERENCES Producto(id_prod)
);

CREATE TABLE Venta (
    Id_ven VARCHAR(20) PRIMARY KEY NOT NULL,
    Telefono_clien VARCHAR(20) NOT NULL,
    RFC_emp VARCHAR(13) NOT NULL,
    Fecha_Hora DATETIME NOT NULL,
    FOREIGN KEY (Telefono_clien) REFERENCES Cliente(Telefono_clien),
    FOREIGN KEY (RFC_emp) REFERENCES Empleado(RFC_emp)
);

CREATE TABLE Detalle_venta (
    Id_detalleVen VARCHAR(20) PRIMARY KEY NOT NULL,
    Id_prod VARCHAR(20) NOT NULL,
    Id_ven VARCHAR(20) NOT NULL,
    Cantidad TINYINT NOT NULL,
    FOREIGN KEY (Id_prod) REFERENCES Producto(id_prod),
    FOREIGN KEY (Id_ven) REFERENCES Venta(Id_ven)
);
show databases;
show tables;

describe empleado;


