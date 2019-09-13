CREATE TABLE IF NOT EXISTS CLIENTE (
	nomeCliente VARCHAR(45),
	endereco VARCHAR(45),
	CPF CHAR (11) unique,
	primary key (CPF)
);