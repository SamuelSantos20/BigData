-- CRIANDO MEU BANCO DE DADOS

CREATE DATABASE meu_ecommerce;

USE  meu_ecommerce;


CREATE TABLE produtos(
id_produto INT NOT NULL PRIMARY KEY,
nome VARCHAR(100),
categoria VARCHAR(50),
preco DECIMAL(8,2),
estoque INT
);

DROP TABLE produtos;

SELECT * FROM produtos;