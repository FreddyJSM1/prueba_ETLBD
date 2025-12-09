CREATE VIEW vista_resumen_clientes AS
SELECT 
    c.nombre AS cliente,
    c.ciudad,
    SUM(v.cantidad * p.precio) AS total_compras,
    MAX(v.fecha_venta) AS ultima_fecha_compra
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY c.id_cliente, c.nombre, c.ciudad;


SELECT * FROM vista_resumen_clientes;