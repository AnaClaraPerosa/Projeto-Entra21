from .models import Perfil
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import  UsuarioForm, PerfilForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

# PerfilCreate
class PerfilCreate(CreateView):
    template_name = "form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="Usuários")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context


class PerfilUpdate(UpdateView):
    template_name = "form.html"
    model = Perfil
    fields = ["nome", "sobrenome", "telefone"]
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"

        return context
# alt ------------------------------------------------

class PerfilComplemento(CreateView):
    template_name = "cadastro.html"
    form_class = PerfilForm
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        self.usuario_id= request.user.id
        if request.user:
            id_perfil = get_object_or_404(Perfil, usuario=request.user.id)
            if(id_perfil):
                return redirect('index')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        url = super().form_valid(form)

        self.object.usuario_id=self.usuario_id
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url