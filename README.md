# Projeto-Entra21
## Esse projeto é um treinamento, realizado em 2022, para demonstar nosso aprendizado no curso online de Python; 

Desenvolvedores:

- Ana Clara Perosa: Front-end;
- Jaqueline Peres Altismo: DBA;
- Lucas Dimon: Back-end;
- Renan Oliveira: Front-end;

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
- Back-end
- Front-end
- Deploy
- documentação e testes

Conte sobre o contexto em que esse projeto está sendo executado: coloque a data, fale que é treinamento, etc. Lembre-se que os commits mostram sua participação no trabalho, e há indicadores que o próprio github fornece!

Quem fez não testa!

## Guia Scrum:
- https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-PortugueseBR-3.0.pdf

## Sexta-feira 12/08/22:
- Criação do banco de dados pelo DBeaver;
- Tabelas criadas:
  - Clientes;
  - Fornecedores;
  - Cidades;
  - Segmento;
  - Produtos;
  - Pedidos;
  - Itens do pedido;

## Segunda-feira 15/08/22:
- Colocação de um modelo de formulário de cadastro;

## Terça-feira 16/08/22:
- Reunião com o professor -> Precisamos pro projeto:
  - Tela de cadastro/login pra cliente e fornecedor;
  - Filtro por nichos no site;
  - Carrinho;
  - Exemplo fictício pra apresentação;

## Quinta-feira 18/08/22 - Ferramentas em utilização:

- Jamboard para definições do projeto - https://jamboard.google.com/d/1B0b0sqwBy96kvEd2MNXXUcix2Xc2Doh0HGcqaOC3WjQ/edit?usp=sharing

- Trello para definição do Kanban - https://trello.com/b/1VD9MM5o/projeto-grupo3

- Miro para montar o Business Model Canvas para fazer o planejamento estratégico - https://miro.com/welcomeonboard/Z21CWEt4UW9mdG4wbEJHWDFKczB2aVJPRGVIaThxMDBkN2RHZ3Q1dVFON1pyNWowVldGTllTT2xZeDR4M0xaWHwzNDU4NzY0NTE0NjAxOTE3OTI4?share_link_id=787192381582

## Sexta-feira 19/08/22: 
- Atualização Business Model Canvas;

## Historia do usuário
- Desenvolver uma aplicação utilizando Django, com a finalidade de facilitar o acesso a alimentos saudáveis. 

- O projeto facilitará  a comercialização de alimentos saudáveis(incluindo orgânicos), como também, para pessoas com restrição alimentar de forma regionalizada, possibilitando as vendas de formas mais assertivas através de encomendas.

- O nosso projeto vai tornar facil a localização e comercialização de alimentos saudáveis(incluindo organicos) e alimentos para pessoas com restrição alimentar de forma regionalizada...

## Banco de Dados do Projeto:

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

## User story pro formulário:
- O nosso projeto vai tornar fácil a localização e comercialização de alimentos saudáveis (incluindo orgânicos) e alimentos para pessoas com restrição alimentar de forma regionalizada.

## 22/08/22 - 26/08/22:
**Estudando banco de dados na nuvem (aws) e o virtual environment**

## Segunda-feira 29/08/22:
- Acessando o banco de dados na nuvem com o repositório oficial do projeto;

## Terça-feira 30/08/22:
- Últimos ajustes no banco de dados para iniciar a inserção de dados;
- Criação da tela de login;

## Quinta-feira 01/08/22:
- Término da tela de login;
- Criação de algumas templates pro projeto;

## Sexta-feira 02/09/22:
- Aula sobre HTML e criação de forms;

## Sábado 03/09/22:
- Reunião do grupo para atualizações das ações realizadas e definições dos proximos passos;
- Atualização do Trello;
- O que foi feito:
 - Renan montou navbar e carrinho de compras do site;
 - Ana montou navbar e formulário de fornecedores;
 - Jaqueline montou logo e prototipação;
 - Lucas está estudando a conexão do back-end com o front-end;

## Segunda-feira 05/09/22:
- Daily Scrum;
- Sprint Planning e definições dos Kanbans; 
- Foi definido as divisões dos Apps:
  - App1 - Front-end e Contato;
  - App2 - Fornecedores;
  - App3 - Produtos e Segmentos;
  - App4 - Carinho de Compras;
  - App5 - Pedidos e Itens dos Pedidos;
  - App6 - Clientes;

## Terça-feira 06/09/22:
- Por unanimidade o grupo decidiu remover o I. F. nesta data, conforme a orientação do professor Adriano Machado.
    - Eu Jaqueline Peres Altismo estou de acordo com a remoção.
    - Eu Ana Clara Perosa estou de acordo com a remoção.
    - Eu Renan Oliveira estou de acordo com a remoção.
    - Eu Lucas Salvaro Dimon estou de acordo com a remoção.

---------------------------------------------------------------------------------------------

# SCRUM - iPicles

## Backlog

**Created:** 05/09/2022 14:20:12

**Created by: Grupo 3** 

#### Identidade Visual e Logo

#### Produtos - Saudável e sustentável

#### Cadastro de Clientes

#### Localização aproximada

#### Cadastro de produtos

#### Compras por encomendas

#### Backend - Integração com Frontend

#### Carrinho de compras

#### Cadastro de Fornecedores

#### Prototipação

#### Banco de dados


## 1º Sprint 05/09/22 a 10/09/22


## 2º Sprint 11/09/22 a 16/09/22


## 3º Sprint 16/09/22 a 23/09/22


## 4º Sprint 24/09/22 a 01/10/22


## 5º Sprint 02/10/22 a 09/10/22

- Definir as categorias

- Criar um front para pagamentos

- Revisar as paginas

- Carrossel

- Pedido do Cliente

- Depoimento da nossa pagina iPicles (Sobre)

- Loja fazer o icone do carrinho adicionar o produto ao carrinho

- Loja fazer a filtragem

- Area do Fornecedor fazer a paginação

- Migrar da base teste para a base oficial

- Atualizar o Readme com o Trello


## Em andamento

- Ajustes nos Front dos templates

- Testar inserção de dados

- Área de depoimentos para fornecedores, linkada ao produto

- Separar grupo de fornecedores e clientes

- Ajustar a adição da quantidade de produtos na pagina de compra de produtos

- Carrinho ao finalizar a compra direcionar para o cadastro do cliente se ja tiver cadastrada, ir para a finalização do pedido


## Feito

- Deploy

- Adicionar arquivos estáticos( css, js)

- Criar aplicativo para visualizações principais e adicionar aos aplicativos instalados - Main - Inicio - Clientes -Fornecedores - Produtos - Projeto iPicles

- Inserção, deleção e update dos produtos pelos fornecedores

- tirar do rodapé o link para a área do cliente  - perguntas do cliente - depoimentos e politicas de segurança

- Loja fazer a contagem dos produtos

- Carrinho (app, banco, integrar com Front)

- Adicionar o Produto na area do fornecedor fazer a formatação

- Formatar a pagina de compra de produtos

- Tirar o cupom de desconto do carrinho de compras

- Loja fazer a paginação

- Formularios cadastro de login e fornecedores

- Ajuste do Front do Carrinho

- Mostrar uma categoria

- Mostrar visualização detalhada de um produto

- Mostrar lista de produtos na área do fornecedor

- Mostrar os produtos mais recentes na página de produtos

- Permitir que os fornecedores adicionem produtos

- Criar área simples para fornecedores( painel com os dados e produtos que ele irá adicionar)

- Criar um pesquisa para os produtos (search)

- pesquisar imagens para o frontend freepik

- Tornar possível fazer login e logout

- Criar visualização(view), modelo(model) e formulário(form) para login

- Adicionar uma frontpage simples(html - conexão)

- Definir os nomes para os aplicativos comitar da base teste para a base oficial. Primeiro ver como limpar a base oficial

- Criar um aplicativo para fornecedores e adicionar aos aplicativos instalados

- Criar modelo de banco de dados para os fornecedores (models main)

- Criar aplicativo e modelos para produtos e categorias (models e app2)

- Definir os apps e criar os models

- Instalar o Django e iniciar um projeto

- Criar e ativar um ambiente virtual (venv)
  
- Identidade visual e logo


-------------------------------------------------



