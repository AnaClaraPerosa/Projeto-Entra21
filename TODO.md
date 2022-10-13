1. [ok] mover a Loja para Inicio / home. 
2. [ok] modificar url do menu principal para apontar o REGISTRE-SE para o AUTH do django.
3. [ok] Adicionar registre-se na tela de login 
4. [ok] Alterar no app usuarios a view UsuarioCreate para PerfilCreate
5. condicionar o menu de (nucleo/templates/index.html) ao grupo em que o usuario pertence. 


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
7. criar um migrate empty para incluir produtos automaticamente. 
    - migrate fake (tenho modelo pronto do arquivo para fazer isto acontecer)

8. upload de imagens para dentro do banco de dados. 

9. loginrequiredmixin para a view - PerfilCompleto de Usuarios . 


Requestes pra index no futuro

                  {% if request.user| has_group:"Fornecedor" %}

                  {% elseif request.user| has_group:"Consumidor" %}

                    {% if request.user.usuario.nome %}
                      <a href="{% url 'perfil_usuario_update'%}">edite seu cadastro aqui</a>
                    {% else %}
                      <a href="{% url 'perfil_usuario_create'%}" class="alarme">preencha seu cdadastro aqui</a>
                      <!-- piscando em vermelho -->
                    {% endif %}
                    
                    <a href="{% url 'seja_fornecedor' %}">Área do Fornecedor (contato)</a>
                  {% else %}

                  {% endif %}