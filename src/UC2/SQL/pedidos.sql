SELECT * FROM meu_ecommerce.produtos;


USE meu_ecommerce;


CREATE TABLE Clientes(
id_cliente INT NOT NULL PRIMARY KEY,
nome VARCHAR(100),
email VARCHAR(100)

);


CREATE TABLE Pedidos(
id_pedido INT NOT NULL PRIMARY KEY ,
id_cliente INT,
data_pedido DATETIME,
valor_total DECIMAL(10,2),
id_produto INT,
quantidade SMALLINT,
FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente),
FOREIGN KEY (id_produto) REFERENCES produtos (id_produto)


);

DROP TABLE produtos ;

ALTER TABLE clientes ADD CONSTRAINT pk_clientes PRIMARY KEY (id_cliente);

ALTER TABLE produtos ADD CONSTRAINT pk_clientes PRIMARY KEY (id_produto);

ALTER TABLE pedidos ADD CONSTRAINT pk_clientes PRIMARY KEY (id_pedido);


ALTER TABLE pedidos ADD CONSTRAINT  fk_pedidos_produtos FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);

ALTER TABLE pedidos ADD CONSTRAINT  fk_pedidos_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);


ALTER TABLE pedidos ADD CONSTRAINT  pk_clientes FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);

ALTER TABLE pedidos ADD CONSTRAINT  fk_pedidos_produtos FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);

SHOW CREATE TABLE produtos;
SHOW CREATE TABLE pedidos;

SELECT * FROM pedidos;
