-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/hgsmxK
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `Usuario` (
    `Usuario_id` int  NOT NULL ,
    `Nome` string  NOT NULL ,
    PRIMARY KEY (
        `Usuario_id`
    )
);

CREATE TABLE `Senha` (
    `Senha_id` int  NOT NULL ,
    `Email` string  NOT NULL ,
    PRIMARY KEY (
        `Senha_id`
    )
);

CREATE TABLE `Pessoa_Fisica` (
    `CPF` int  NOT NULL ,
    `Genero` VARCHAR(15)  NOT NULL ,
    `EstadoCivil` string  NOT NULL ,
    `Idade` int  NOT NULL ,
    `Cep` VARCHAR(12)  NOT NULL ,
    `Logradouro` string  NOT NULL ,
    `Rua` string  NOT NULL ,
    `Cidade` VARCHAR(30)  NOT NULL ,
    `Estado` VARCHAR(2)  NOT NULL ,
    `Fk_Usuario_id` int  NOT NULL ,
    PRIMARY KEY (
        `CPF`
    )
);

CREATE TABLE `Pessoa_Juridica` (
    `CNJP` int  NOT NULL ,
    `Nome_Fantasia` VARCHAR(50)  NOT NULL ,
    `Razao_Social` VARCHAR(50)  NOT NULL ,
    `FK_Usuario_id` int  NOT NULL ,
    PRIMARY KEY (
        `CNJP`
    )
);

ALTER TABLE `Usuario` ADD CONSTRAINT `fk_Usuario_Usuario_id` FOREIGN KEY(`Usuario_id`)
REFERENCES `Pessoa_Juridica` (`FK_Usuario_id`);

ALTER TABLE `Senha` ADD CONSTRAINT `fk_Senha_Senha_id` FOREIGN KEY(`Senha_id`)
REFERENCES `Usuario` (`Usuario_id`);

ALTER TABLE `Pessoa_Fisica` ADD CONSTRAINT `fk_Pessoa_Fisica_Fk_Usuario_id` FOREIGN KEY(`Fk_Usuario_id`)
REFERENCES `Usuario` (`Usuario_id`);

