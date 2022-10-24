1. [ok] mover a Loja para Inicio / home. 
2. [ok] modificar url do menu principal para apontar o REGISTRE-SE para o AUTH do django.
3. [ok] Adicionar registre-se na tela de login 
4. [ok] Alterar no app usuarios a view UsuarioCreate para PerfilCreate
5. [ok] condicionar o menu de (nucleo/templates/index.html) ao grupo em que o usuario pertence. 


*** = Basta que o usuario esteja autenticado via django (Auth)
:----------------------------:-------------------:----------------:-----------------:
:                            : aut via site ***      : via painelAdmin: aut via site    : 
:                            :                   :                :                     : não autenticado
:                            : is_autenticated   : is_fornecedor  : is_consumidor       :
:-------------------------:-------------------:----------------:-----------------:-----------------
: home                       :         x         :      x         :      x          :      x
: loja                       :         x         :      x         :      x          :      x
: perfilusuario-registre-se  :                   :                :                 :      x
: perfil create              :         x         :      x         :      x          : 
: perfil update              :         x         :      x         :      x          : 
: perfilconsumidor create    :         x         :      x         :                 :  
: perfilconsumidor update    :         x         :      x         :      x          :
: perfilfornecedor create    :                   :      x         :                 :
: perfilfornecedor update    :                   :      x         :                 :
: produtos create            :                   :      x         :                 :
: produtos update            :                   :      x         :                 :
: depoimentos fornecedor List:                   :                :                 :      x
: depoimentos consumidor List:                   :                :                 :      x
: contato create             :                   :                :                 :      x
: contato create             :                   :                :                 :      x
:----------------------------:-------------------:----------------:-----------------:---------------

6. [ok] Mudar novamente para Onetoonefield
    request.user 
    - PerfilConsumidor -> User (Perfil_id) --> FK(Perfil)
    - PerfilFornecedor -> user (Perfil_id) --> Fk(Perfil)
    - Perfil           -> User (user_id) --> O2O(User)

(by prof)
7. [] criar um migrate empty para incluir produtos automaticamente. 
    - migrate fake (tenho modelo pronto do arquivo para fazer isto acontecer)

8. upload de imagens para dentro do banco de dados. 

9. [ok] loginrequiredmixin para a view - PerfilCompleto de Usuarios . 

10. [ok] Cadastro dos clientes
    
11. [ok] Pedidos
    
12. Fornecedor não tem acesso a area do fornecedor
    
13. Depoimentos

14.  [ok] criar 2 botões no carrinho:
          - atualizar dados (target=blank) (nova view mesmo form ja criado)
          - neste form vai ter um botão FECHAR 

15.  [ ] JAVASCRIPT: request se foi criado o registro no model clientes. 
       
16.  [ok] Deploy

Bugs conhecidos:

- Uploads de imagens no Heroku (para carrossel e loja)
- Voltar o carrossel como estava para buscar as imagens no banco de dados linkado ao produto
- Ajustar o site para mobile
- Ajustar depoimentos dos clientes

  
Planos futuros:
- Georeferenciamento para encontrar o fornecedor mais próximo ao cliente.
- Avaliação do fornecedor 
- Ajustar para permitir encomendas dos produtos
- Area de histórico de pedidos para o consumidor final
- Controle de fidelidade para o consumidor final