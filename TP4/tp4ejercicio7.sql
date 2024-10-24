DROP DATABASE IF EXISTS ConsolidacionDatos;
CREATE DATABASE ConsolidacionDatos;
USE ConsolidacionDatos;

-- creacion de la tabla Pedidos
CREATE TABLE Pedidos (
    PedidoId INT PRIMARY KEY AUTO_INCREMENT,
    ClienteId INT NOT NULL,
    ProductoId INT NOT NULL,
    Cantidad INT NOT NULL,
    PrecioUnitario DECIMAL(10,2) NOT NULL,
    FechaPedido DATE NOT NULL
);

-- creacion de la tabla consolidadoVentas
CREATE TABLE ConsolidadoVentas (
    ConsolidadoId INT PRIMARY KEY AUTO_INCREMENT,
    ClienteId INT NOT NULL,
    ProductoId INT NOT NULL,
    CantidadTotal INT NOT NULL,
    IngresoTotal DECIMAL(15,2) NOT NULL
);

-- poblacion de la tabla Pedidos
INSERT INTO Pedidos (ClienteId, ProductoId, Cantidad, PrecioUnitario, FechaPedido)
VALUES 
(1, 101, 10, 20.00, '2024-01-10'),  
(2, 102, 5, 15.00, '2024-01-11'),   
(1, 103, 8, 30.00, '2024-01-12'),   
(3, 101, 12, 20.00, '2024-01-13'),  
(2, 103, 7, 30.00, '2024-01-14'),   
(4, 104, 15, 25.00, '2024-01-15'),  
(1, 101, 6, 20.00, '2024-01-16'),   
(3, 102, 9, 15.00, '2024-01-17'),   
(4, 104, 10, 25.00, '2024-01-18'),  
(2, 105, 3, 40.00, '2024-01-19');   

DELIMITER $$

CREATE PROCEDURE ConsolidarVentas()
BEGIN
    -- Declaracion variables locales
    DECLARE v_ClienteId INT;
    DECLARE v_ProductoId INT;
    DECLARE v_Cantidad INT;
    DECLARE v_PrecioUnitario DECIMAL(10,2);
    DECLARE v_IngresoTotal DECIMAL(15,2);
    DECLARE v_CantidadTotal INT;

    -- Manejo de fin de cursor
    DECLARE done INT DEFAULT 0;

    -- Declaracion el cursor para seleccionar los pedidos
    DECLARE pedido_cursor CURSOR FOR
        SELECT ClienteId, ProductoId, Cantidad, PrecioUnitario
        FROM Pedidos;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Iniciar transacción
    START TRANSACTION;

    OPEN pedido_cursor;

    -- Ciclo para recorrer todos los pedidos
    read_loop: LOOP
        FETCH pedido_cursor INTO v_ClienteId, v_ProductoId, v_Cantidad, v_PrecioUnitario;
        
        -- Verifica si ya no hay más filas
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calcula el ingreso total del pedido actual
        SET v_IngresoTotal = v_Cantidad * v_PrecioUnitario;

        -- Verifica si ya existe un registro en ConsolidadoVentas para el par ClienteId y ProductoId
        IF EXISTS (
            SELECT 1 
            FROM ConsolidadoVentas 
            WHERE ClienteId = v_ClienteId AND ProductoId = v_ProductoId
        ) THEN
            -- Actualiza el registro existente en ConsolidadoVentas
            UPDATE ConsolidadoVentas
            SET CantidadTotal = CantidadTotal + v_Cantidad,
                IngresoTotal = IngresoTotal + v_IngresoTotal
            WHERE ClienteId = v_ClienteId AND ProductoId = v_ProductoId;
        ELSE
            -- Inserta un nuevo registro en ConsolidadoVentas
            INSERT INTO ConsolidadoVentas (ClienteId, ProductoId, CantidadTotal, IngresoTotal)
            VALUES (v_ClienteId, v_ProductoId, v_Cantidad, v_IngresoTotal);
        END IF;

    END LOOP;

    CLOSE pedido_cursor;

    -- Confirmar la transacción
    COMMIT;

END$$

DELIMITER ;

-- Ejecucion y Ver los datos consolidados de la tabla ConsolidadoVentas
CALL ConsolidarVentas();

SELECT * FROM ConsolidadoVentas;