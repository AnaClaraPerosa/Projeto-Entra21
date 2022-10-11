1. [ok] mover a Loja para Inicio / home. 
2. modificar url do menu principal para apontar o REGISTRE-SE para o AUTH do django.
3. Adicionar registre-se na tela de login 
4. Alterar no app usuarios a view UsuarioCreate para PerfilCreate
5. condicionar o menu de (nucleo/templates/index.html) ao grupo em que o usuario pertence. 


*** = Basta que o usuario esteja autenticado via django (Auth)
:----------------------------:-------------------:----------------:-----------------:
:                            : aut via site ***      : via painelAdmin: aut via site    : 
:                            :                   :                :                 : não autenticado
:                            : is_autenticated   : is_fornecedor  : is_cliente      :
:----------------------------:-------------------:----------------:-----------------:-----------------
: home                       :         x         :      x         :      x          :      x
: loja                       :         x         :      x         :      x          :      x
: perfilusuario-registre-se  :                   :                :                 :       x
: perfilcliente create       :        x          :      x         :                 :  
: perfilcliente update       :        x          :      x         :      x          :
: perfilfornecedor create    :                   :      x         :                 :
: perfilfornecedor update    :                   :      x         :                 :
: produtos create            :                   :      x         :                 :
: produtos update            :                   :      x         :                 :
: depoimentos fornecedor List:                   :                :                 :      x
: depoimentos consumidor List:                   :                :                 :      x
: contato create             :                   :                :                 :      x
: contato create             :                   :                :                 :      x
:----------------------------:-------------------:----------------:-----------------:---------------

6. Mudar novamente para Onetoonefield
    request.user 
    - PerfilConsumidor -> User   (user_id) --> fk(User)
    - PerfilFornecedor -> user (user_id) --> fk(User)

(by prof)
7. criar um migrate empty para incluir produtos automaticamente. 
    - migrate fake (tenho modelo pronto do arquivo para fazer isto acontecer)

8. upload de imagens para dentro do banco de dados. 
