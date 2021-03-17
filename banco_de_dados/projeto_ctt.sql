CREATE DATABASE projeto_ctt;

CREATE TABLE banco (
		id_banco SERIAL PRIMARY KEY,
		nome VARCHAR(255) NOT NULL
);

CREATE TABLE cliente (
		id_cliente SERIAL PRIMARY KEY,
		id_banco INT,
		nome VARCHAR(255) NOT NULL,
		data_de_nascimento DATE,
		rg VARCHAR(9) UNIQUE NOT NULL,
		cpf VARCHAR(11) UNIQUE NOT NULL,
		estado_civil VARCHAR NOT NULL,
		profissao VARCHAR(255) NOT NULL,
		tipo_residencia VARCHAR(15) NOT NULL,
		cep VARCHAR(15) NOT NULL,
		rua VARCHAR(255) NOT NULL,
		numero VARCHAR(5) NOT NULL,
		cidade VARCHAR(100) NOT NULL,
		estado VARCHAR(255) NOT NULL,
		uf VARCHAR(2) NOT NULL,
		FOREIGN KEY (id_banco)
			REFERENCES banco(id_banco)
	 		ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE proprietario (
		id_proprietario SERIAL PRIMARY KEY,
		nome VARCHAR(255) NOT NULL,
		data_de_nascimento DATE,
		rg VARCHAR(9) UNIQUE NOT NULL,
		cpf VARCHAR(11) UNIQUE NOT NULL,
		estado_civil VARCHAR NOT NULL,
		profissao VARCHAR(255) NOT NULL
);

CREATE TABLE despesas (
		id_despesas SERIAL PRIMARY KEY,
		conta_luz DECIMAL NOT NULL,
		conta_agua DECIMAL NOT NULL,
		conta_condominio DECIMAL NOT NULL,
		propaganda_pre_venda DECIMAL NOT NULL
);

CREATE TABLE imovel (
		id_imovel SERIAL PRIMARY KEY,
		id_proprietario INT,
		id_despesas INT,
		valor DECIMAL,
		tipo_residencia VARCHAR(255) NOT NULL,
		cep VARCHAR(15) NOT NULL,
		rua VARCHAR(255) NOT NULL,
		numero VARCHAR(5) NOT NULL,
		cidade VARCHAR(100) NOT NULL,
		estado VARCHAR(255) NOT NULL,
		uf VARCHAR(2) NOT NULL,
		data_de_cadastro DATE,
		FOREIGN KEY (id_proprietario)
			REFERENCES proprietario(id_proprietario)
			ON UPDATE CASCADE ON DELETE CASCADE,
		FOREIGN KEY (id_despesas)
			REFERENCES despesas(id_despesas)
			ON UPDATE CASCADE ON DELETE CASCADE	
);

CREATE TABLE compra (
		id_compra SERIAL PRIMARY KEY,
		id_cliente INT,
		id_imovel INT,
		forma_pagamento VARCHAR(15) NOT NULL,
		numero_parcelas INT,
		data_aquisicao DATE NOT NULL,
		FOREIGN KEY (id_cliente)
			REFERENCES cliente(id_cliente)
			ON UPDATE CASCADE ON DELETE CASCADE,
		FOREIGN KEY (id_imovel)
			REFERENCES imovel(id_imovel)
			ON UPDATE CASCADE ON DELETE CASCADE
);

