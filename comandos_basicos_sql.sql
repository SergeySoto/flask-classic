/* seleccionar todos los registros de una tabla */
/*SELECT * from movements */
/* seleccionar algunos campos de una tabla */
/*SELECT concept, quantity from movements */
/* para insertar nuevos registros en la tabla movements */
/*INSERT into movements (date,concept,quantity) VALUES ('2024-12-10','comida',-500) */
/* select con where (filtro por campos) */
/* SELECT date,concept,quantity from movements where id=2; */
/* Actualizar cualquier campo de la tabla, importante siempre referenciar por where */
/* UPDATE movements SET concept = 'desayuno', quantity = -50 WHERE id = 2; */
/* Borramos un registro especifico de la tabla movimientos */
/* DELETE from movements WHERE id=3; */
INSERT into movements (date,concept,quantity) VALUES ('2024-11-10','compra del mercadona',-150);
SELECT * from movements 
