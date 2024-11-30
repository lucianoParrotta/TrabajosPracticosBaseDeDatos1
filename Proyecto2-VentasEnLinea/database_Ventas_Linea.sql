
DROP DATABASE IF EXISTS sistema_ventas;
CREATE DATABASE sistema_ventas;
USE sistema_ventas;

-- Crear tabla de Productos
CREATE TABLE Productos (
    id INT AUTO_INCREMENT PRIMARY KEY,          
    nombre VARCHAR(50) NOT NULL,                
    categoria VARCHAR(50),                      
    precio DECIMAL(10, 2) NOT NULL,             
    stock INT NOT NULL                          
);

-- Crear índices para las columnas nombre y categoria
CREATE INDEX idx_nombre_producto ON Productos(nombre);
CREATE INDEX idx_categoria_producto ON Productos(categoria);
CREATE INDEX idx_nombre_categoria_producto ON Productos(nombre, categoria);

-- Crear tabla de Clientes
CREATE TABLE Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,          
    nombre VARCHAR(100) NOT NULL,               
    correo VARCHAR(100) UNIQUE NOT NULL,        
    telefono VARCHAR(15)                        
);

-- Crear tabla de Órdenes
CREATE TABLE Ordenes (
    id INT AUTO_INCREMENT PRIMARY KEY,         
    cliente_id INT NOT NULL,                    
    producto_id INT NOT NULL,                   
    cantidad INT NOT NULL,                      
    fecha DATE NOT NULL,                        
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES Productos(id) ON DELETE CASCADE
);

-- Insertar datos iniciales en Productos
INSERT INTO Productos (nombre, categoria, precio, stock) VALUES
('Producto A', 'Categoría 1', 100.00, 50),
('Producto B', 'Categoría 2', 200.00, 30),
('Producto C', 'Categoría 3', 300.00, 20),
('Producto D', 'Categoría 4', 150.00, 40),
('Producto E', 'Categoría 1', 120.00, 25),
('Producto F', 'Categoría 2', 250.00, 15),
('Producto G', 'Categoría 3', 350.00, 10),
('Producto H', 'Categoría 4', 175.00, 35),
('Producto I', 'Categoría 1', 80.00, 60),
('Producto J', 'Categoría 2', 90.00, 45);

-- Insertar datos iniciales en Clientes
INSERT INTO Clientes (nombre, correo, telefono) VALUES
('Juan Pérez', 'juan@example.com', '123456789'),
('María López', 'maria@example.com', '987654321'),
('Carlos Gómez', 'carlos@example.com', '555123456'),
('Ana Torres', 'ana@example.com', '444987654'),
('Pedro Díaz', 'pedro@example.com', '333456789'),
('Luisa Méndez', 'luisa@example.com', '222123456'),
('Fernando Castro', 'fernando@example.com', '111987654'),
('Laura Vega', 'laura@example.com', '666456789'),
('Sofía Morales', 'sofia@example.com', '777123456'),
('David Ramírez', 'david@example.com', '888987654');

-- Insertar datos iniciales en Órdenes
INSERT INTO Ordenes (cliente_id, producto_id, cantidad, fecha) VALUES
-- Órdenes del Cliente 1
(1, 1, 2, '2024-11-01'), (1, 2, 3, '2024-11-02'), (1, 3, 4, '2024-11-03'),
(1, 4, 5, '2024-11-04'), (1, 5, 6, '2024-11-05'), (1, 6, 2, '2024-11-06'),
(1, 7, 3, '2024-11-07'), (1, 8, 4, '2024-11-08'), (1, 9, 1, '2024-11-09'),
(1, 10, 2, '2024-11-10'),

-- Órdenes del Cliente 2
(2, 1, 1, '2024-11-11'), (2, 2, 2, '2024-11-12'), (2, 3, 3, '2024-11-13'),
(2, 4, 4, '2024-11-14'), (2, 5, 5, '2024-11-15'), (2, 6, 1, '2024-11-16'),
(2, 7, 2, '2024-11-17'), (2, 8, 3, '2024-11-18'), (2, 9, 4, '2024-11-19'),
(2, 10, 5, '2024-11-20'),

-- Órdenes del Cliente 3
(3, 1, 1, '2024-11-21'), (3, 2, 2, '2024-11-22'), (3, 3, 3, '2024-11-23'),
(3, 4, 4, '2024-11-24'), (3, 5, 5, '2024-11-25'), (3, 6, 6, '2024-11-26'),
(3, 7, 2, '2024-11-27'), (3, 8, 3, '2024-11-28'), (3, 9, 1, '2024-11-29'),
(3, 10, 2, '2024-11-30'),

-- Órdenes del Cliente 4
(4, 1, 4, '2024-12-01'), (4, 2, 3, '2024-12-02'), (4, 3, 5, '2024-12-03'),
(4, 4, 6, '2024-12-04'), (4, 5, 1, '2024-12-05'), (4, 6, 2, '2024-12-06'),
(4, 7, 3, '2024-12-07'), (4, 8, 4, '2024-12-08'), (4, 9, 1, '2024-12-09'),
(4, 10, 2, '2024-12-10'),

-- Órdenes del Cliente 5
(5, 1, 2, '2024-12-11'), (5, 2, 1, '2024-12-12'), (5, 3, 3, '2024-12-13'),
(5, 4, 4, '2024-12-14'), (5, 5, 2, '2024-12-15'), (5, 6, 3, '2024-12-16'),
(5, 7, 4, '2024-12-17'), (5, 8, 1, '2024-12-18'), (5, 9, 2, '2024-12-19'),
(5, 10, 3, '2024-12-20'),

-- Órdenes del Cliente 6
(6, 1, 2, '2024-12-21'), (6, 2, 1, '2024-12-22'), (6, 3, 3, '2024-12-23'),
(6, 4, 2, '2024-12-24'), (6, 5, 4, '2024-12-25'), (6, 6, 5, '2024-12-26'),
(6, 7, 3, '2024-12-27'), (6, 8, 2, '2024-12-28'), (6, 9, 1, '2024-12-29'),
(6, 10, 4, '2024-12-30'),

-- Órdenes del Cliente 7
(7, 1, 4, '2025-01-01'), (7, 2, 3, '2025-01-02'), (7, 3, 5, '2025-01-03'),
(7, 4, 6, '2025-01-04'), (7, 5, 1, '2025-01-05'), (7, 6, 2, '2025-01-06'),
(7, 7, 3, '2025-01-07'), (7, 8, 4, '2025-01-08'), (7, 9, 2, '2025-01-09'),
(7, 10, 5, '2025-01-10'),

-- Órdenes del Cliente 8
(8, 1, 2, '2025-01-11'), (8, 2, 1, '2025-01-12'), (8, 3, 3, '2025-01-13'),
(8, 4, 4, '2025-01-14'), (8, 5, 2, '2025-01-15'), (8, 6, 3, '2025-01-16'),
(8, 7, 4, '2025-01-17'), (8, 8, 1, '2025-01-18'), (8, 9, 2, '2025-01-19'),
(8, 10, 3, '2025-01-20'),

-- Órdenes del Cliente 9
(9, 1, 2, '2025-01-21'), (9, 2, 1, '2025-01-22'), (9, 3, 3, '2025-01-23'),
(9, 4, 4, '2025-01-24'), (9, 5, 2, '2025-01-25'), (9, 6, 3, '2025-01-26'),
(9, 7, 4, '2025-01-27'), (9, 8, 1, '2025-01-28'), (9, 9, 2, '2025-01-29'),
(9, 10, 3, '2025-01-30'),

-- Órdenes del Cliente 10
(10, 1, 4, '2025-01-31'), (10, 2, 3, '2025-02-01'), (10, 3, 5, '2025-02-02'),
(10, 4, 6, '2025-02-03'), (10, 5, 1, '2025-02-04'), (10, 6, 2, '2025-02-05'),
(10, 7, 3, '2025-02-06'), (10, 8, 4, '2025-02-07'), (10, 9, 2, '2025-02-08'),
(10, 10, 5, '2025-02-09');

SHOW TABLES;

SELECT * FROM Productos;
SELECT * FROM Clientes;
SELECT * FROM Ordenes;

-- prueba para seleccionar cliente
SELECT * FROM Ordenes WHERE cliente_id = 1;