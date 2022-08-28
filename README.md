# Projeto-Entra21
## Esse projeto é um treinamento, realizado em 2022, para demonstar nosso aprendizado no curso online de Python; 

Desenvolvedores:

- Ana Clara Perosa;
- Igor Freire;
- Jaqueline Peres Altismo;
- Lucas Dimon
- Renan Oliveira;

# JAM Board:

## **Nomes pro projeto:**
- Foodfit;
- eFit;
- eBeet;
- Eatwell;
- iPicles;
- iCarrot;
- eAncore;
- Da Terra;
- FoodBuddy;

## **Produtos por assinatura:**
- Montar uma plataforma pra clube de assinaturas ("marketplace");
- Quais produtos colocar para fazer o box?

## **Concorrência:**
- 

## **Pilotos:**
- 

## **Nicho:**
- Pessoas com restrições alimentares?
- Pequenos produtores?
- Produtos naturais diversos?
- ...

## **Outros:**
- Produtor pagar para fazer seu anúncio/arte;
- Conteúdo (fotos, vídeos, receitas) disponibilizado pelo produtor;
- Programa para indicar fornecedores;
- Mostrar produtos a nível nacional e apresentar os pontos mais próximos de venda;
- Interface de cadastro de usuários;
- Divulgação em redes sociais;
- Programa de desconto por indicações;
- Disponível para PC e smartphones;
- Futuramente ter um produto próprio;
- Parceria com nutricionistas;
- Cartão fidelidade;
- Programa de avaliação/feedback dos clientes;

# Guia do professor:

1.	Scrum - Backlog
    a.	Product Owner
    b.	Scrum master 
    c.	Time e atribuições. (Developers)
    d.	Definir prioridades 
    e.	Divisão das sprints 

2.	Kanban - Divisão da primeira e segunda semana (sprint)

3.	Ferramentas - Definir: 
    a.	repositório git local / github.com 
    b.	compartilhar repositório com a equipe exclusivamente e com o prof. (adriano@machado.tec.br)

4.	Tudo deve ser definido via README.md NA PAGINA INICIAL COM SEUS ARQUIVOS AUXILIARES. 

Foco em desenvolver apenas o que realmente importa!!!

Deixar a perfumaria para final de setembro quando o projeto/app/dashboard estiver funcional. 

5.	Definir as bibliotecas que serão utilizadas no projeto.  (re-atribuição)

6.	Definir como o projeto será exposto (deploy) (re-atribuição)
    a.	Isto deve ser feito logo no início do projeto. (não fique só na mão de um membro da equipe)

7.	Treinar APRESENTAÇÃO GRAVADA DE 5-8 MINUTOS DA APLICAÇÃO. O ideal seria uma apresentação pessoal. Lembre-se de trabalhar isso durante todo o período, não deixe para última hora ;)

Dividir as equipes em duplas para cada função (inicialmente):
-	Back-end
- Front-end
- Deploy
- documentação e testes

Conte sobre o contexto em que esse projeto está sendo executado: coloque a data, fale que é treinamento, etc. Lembre-se que os commits mostram sua participação no trabalho, e há indicadores que o próprio github fornece!

Quem fez não testa!

## Guia Scrum:
- https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-PortugueseBR-3.0.pdf

## Sexta feira 12/08/22:
- Criação do banco de dados pelo DBeaver;
- Tabelas criadas:
  - Clientes;
  - Fornecedores;
  - Cidades;
  - Segmento;
  - Produtos;
  - Pedidos;
  - Itens do pedido;
<<<<<<< HEAD
  - 
  - 
=======

## Segunda Feira 15/08/22:
- Colocação de um modelo de formulário de cadastro;
>>>>>>> 967f6cd11e8228ca4122907601dd74f7c650b1b8


## Terça feira 16/08/22:
- Reunião com o professor -> Precisamos pro projeto:
  - Tela de cadastro/login pra cliente e fornecedor;
  - Filtro por nichos no site;
  - Carrinho;
  - Exemplo fictício pra apresentação;
  -  

## Quinta feira 18/08/22 - Ferramentas em utilização:

- Jamboard para definições do projeto - https://jamboard.google.com/d/1B0b0sqwBy96kvEd2MNXXUcix2Xc2Doh0HGcqaOC3WjQ/edit?usp=sharing
<<<<<<< HEAD
<<<<<<< HEAD

- Trello para definição do Scrum - 
=======
=======

>>>>>>> 8b509f1f517649f2aa898a9ca50bf34821fba28c
- Trello para definição do Kanban - https://trello.com/b/1VD9MM5o/projeto-grupo3
>>>>>>> 653ba5ecf9db209b3835b3b82ee65e3b25095ff6

- Miro para montar o Business Model Canvas para fazer o planejamento estratégico - https://miro.com/welcomeonboard/Z21CWEt4UW9mdG4wbEJHWDFKczB2aVJPRGVIaThxMDBkN2RHZ3Q1dVFON1pyNWowVldGTllTT2xZeDR4M0xaWHwzNDU4NzY0NTE0NjAxOTE3OTI4?share_link_id=787192381582

## Sexta feira 19/08/22: 
- Atualização Business Model Canvas;

## Historia do usuário
- Desenvolver uma aplicação utilizando Django, com a finalidade de facilitar o acesso a alimentos saudáveis. 

O projeto facilitará  a comercialização de alimentos saudáveis(incluindo orgânicos), como também, para pessoas com restrição alimentar de forma regionalizada, possibilitando as vendas de formas mais assertivas através de encomendas.

  
<<<<<<< HEAD
- O nosso projeto vai tornar facil a localização e comercialização de alimentos saudáveis(incluindo organicos) e alimentos para pessoas com restrição alimentar de forma regionalizada...

## Bando de Dados do Projeto

-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
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
=======
- O nosso projeto vai tornar fácil a localização e comercialização de alimentos saudáveis (incluindo orgânicos) e alimentos para pessoas com restrição alimentar de forma regionalizada.



- 
>>>>>>> 8b509f1f517649f2aa898a9ca50bf34821fba28c




