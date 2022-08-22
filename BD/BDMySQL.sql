﻿-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `CLIENTES` (
    `CLIENTES_ID` INTEGER  NOT NULL ,
    `CLIENTES_NOME` STRING  NOT NULL ,
    `CLIENTES_TELEFONE` TEXT  NOT NULL ,
    `CLIENTES_CPF` TEXT  NOT NULL ,
    `CLIENTES_LOGRADOURO` TEXT  NOT NULL ,
    `CLIENTES_BAIRRO` TEXT  NOT NULL ,
    `CLIENTES_NUMERO` TEXT  NOT NULL ,
    `CLIENTES_CEP` TEXT  NOT NULL ,
    `CLIENTES_COMPLEMENTO` TEXT  NOT NULL ,
    `CLIENTES_OBS` TEXT  NOT NULL ,
    `CLIENTES_CIDADE_ID` INTEGER  NOT NULL ,
    PRIMARY KEY (
        `CLIENTES_ID`
    )
);

CREATE TABLE `FORNECEDORES` (
    `FORNECEDORES_ID` INTEGER  NOT NULL ,
    `FORNECEDORES_RAZAO_SOCIAL` TEXT  NOT NULL ,
    `FORNECEDORES_CPF_CNPJ` TEXT  NOT NULL ,
    `FORNECEDORES_CONTATO` TEXT  NOT NULL ,
    `FORNECEDORES_TELEFONE` TEXT  NOT NULL ,
    `FORNECEDORES_LOGRADOURO` TEXT  NOT NULL ,
    `FORNECEDORES_BAIRRO` TEXT  NOT NULL ,
    `FORNECEDORES_NUMERO` TEXT  NOT NULL ,
    `FORNECEDORES_CEP` TEXT  NOT NULL ,
    `FORNECEDORES_COMPLEMENTO` TEXT  NOT NULL ,
    `FORNECEDORES_OBS` TEXT  NOT NULL ,
    `FORNECEDORES_CIDADE_ID` INTEGER  NOT NULL ,
    PRIMARY KEY (
        `FORNECEDORES_ID`
    )
);

CREATE TABLE `CIDADES` (
    `CIDADES_ID` INTEGER  NOT NULL ,
    `CIDADES_CIDADE` TEXT  NOT NULL ,
    `CIDADES_CEP` TEXT  NOT NULL ,
    PRIMARY KEY (
        `CIDADES_ID`
    )
);

CREATE TABLE `SEGMENTO` (
    `SEGMENTO_ID` INTEGER  NOT NULL ,
    `SEGMENTO_NOME` TEXT  NOT NULL ,
    PRIMARY KEY (
        `SEGMENTO_ID`
    )
);

CREATE TABLE `PRODUTOS` (
    `PRODUTOS_ID` INTEGER  NOT NULL ,
    `PRODUTOS_NOME` TEXT  NOT NULL ,
    `PRODUTOS_DESCRICAO` TEXT  NOT NULL ,
    `PRODUTOS_VALOR_UNIT` REAL  NOT NULL ,
    `PRODUTOS_QTDE` INTEGER  NOT NULL ,
    `PRODUTOS_SEGMENTO_ID` INTEGER  NOT NULL ,
    PRIMARY KEY (
        `PRODUTOS_ID`
    )
);

CREATE TABLE `PEDIDOS` (
    `PEDIDOS_ID` INTEGER  NOT NULL ,
    `PEDIDOS_CLIENTE_ID` INTEGER  NOT NULL ,
    `PEDIDOS_FORNECEDOR_ID` INTEGER  NOT NULL ,
    `PEDIDOS_DATA_PEDIDO` DATE  NOT NULL ,
    `PEDIDOS_PRAZO_ENTREGA` DATE  NOT NULL ,
    `PEDIDOS_OBS` TEXT  NOT NULL ,
    PRIMARY KEY (
        `PEDIDOS_ID`
    )
);

CREATE TABLE `ITENSPED` (
    `ITENSPED_ID` INTEGER  NOT NULL ,
    `ITENSPED_PRODUTO_ID` INTEGER  NOT NULL ,
    `ITENSPED_QTDE` INTEGER  NOT NULL ,
    PRIMARY KEY (
        `ITENSPED_ID`
    )
);

ALTER TABLE `CLIENTES` ADD CONSTRAINT `fk_CLIENTES_CLIENTES_CIDADE_ID` FOREIGN KEY(`CLIENTES_CIDADE_ID`)
REFERENCES `CIDADES` (`CIDADES_ID`);

ALTER TABLE `FORNECEDORES` ADD CONSTRAINT `fk_FORNECEDORES_FORNECEDORES_CIDADE_ID` FOREIGN KEY(`FORNECEDORES_CIDADE_ID`)
REFERENCES `CIDADES` (`CIDADES_ID`);

ALTER TABLE `PRODUTOS` ADD CONSTRAINT `fk_PRODUTOS_PRODUTOS_ID` FOREIGN KEY(`PRODUTOS_ID`)
REFERENCES `ITENSPED` (`ITENSPED_PRODUTO_ID`);

ALTER TABLE `PRODUTOS` ADD CONSTRAINT `fk_PRODUTOS_PRODUTOS_SEGMENTO_ID` FOREIGN KEY(`PRODUTOS_SEGMENTO_ID`)
REFERENCES `SEGMENTO` (`SEGMENTO_ID`);

ALTER TABLE `PEDIDOS` ADD CONSTRAINT `fk_PEDIDOS_PEDIDOS_CLIENTE_ID` FOREIGN KEY(`PEDIDOS_CLIENTE_ID`)
REFERENCES `CLIENTES` (`CLIENTES_ID`);

ALTER TABLE `PEDIDOS` ADD CONSTRAINT `fk_PEDIDOS_PEDIDOS_FORNECEDOR_ID` FOREIGN KEY(`PEDIDOS_FORNECEDOR_ID`)
REFERENCES `FORNECEDORES` (`FORNECEDORES_ID`);

ALTER TABLE `ITENSPED` ADD CONSTRAINT `fk_ITENSPED_ITENSPED_ID` FOREIGN KEY(`ITENSPED_ID`)
REFERENCES `PEDIDOS` (`PEDIDOS_ID`);

