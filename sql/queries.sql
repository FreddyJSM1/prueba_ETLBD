-- ventas totales por mes y categoria
SELECT
    DATE_FORMAT(v.fecha_venta, '%Y-%m') AS mes,
    p.categoria,
    SUM(v.cantidad * p.precio) AS total_ventas
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY mes, p.categoria
ORDER BY mes;

-- TOP 5 clientes con mayores compras (último año)
SELECT 
    c.nombre,
    SUM(v.cantidad * p.precio) AS total_compras
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
JOIN productos p ON v.id_producto = p.id_producto
WHERE v.fecha_venta >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR)
GROUP BY c.nombre
ORDER BY total_compras DESC
LIMIT 5;