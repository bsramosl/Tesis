from datetime import date

from django.contrib import messages
from django.core.serializers import serialize
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView
from django.contrib.auth.models import User
from .forms import *
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, update_session_auth_hash
from .models import *


class Inicio(TemplateView):
    template_name = 'inicio.html'


class ModeloReact(TemplateView):
    template_name = 'modelo_reactor.html'


class TiempoCultivo(TemplateView):
    template_name = 'tiempo_cultivo.html'


class Admin(TemplateView):
    model = User
    template_name = 'admin.html'

    def get_context_data(self, **kwargs):
        activo = User.objects.filter(is_active=True).count()
        inactivo = User.objects.filter(is_active=False).count()
        nuevo = User.objects.filter(date_joined__gt=date.today()).count()
        organismo = Organismo.objects.count()
        context = super().get_context_data(**kwargs)
        context['activos'] = activo
        context['inactivos'] = inactivo
        context['usuarios'] = activo + inactivo
        context['nuevo'] = nuevo
        context['organismo'] = organismo
        return context


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('ProsPy:Inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, 'Bienvenido')
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))


class LogoutUsuario(RedirectView):
    pattern_name = 'ProsPy:Login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class LUsuarioLista(TemplateView):
    template_name = 'Usuario_Admin.html'


class UsuarioLista(ListView):
    model = User
    context_object_name = 'usuarios'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'aplication/json')
        else:
            return redirect('ProsPy:LUsuarioLista')


class CrearUsuario(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = 'registro.html'
    success_url = reverse_lazy('ProsPy:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar Usuario'
        return context

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response


def CambiarContraseña(request):
    if request.method == 'POST':
        form = ContraseñaForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido cambiada.')
            return redirect('ProsPy:CambiarContraseña')
        else:
            messages.error(request, form.errors)
    else:
        form = ContraseñaForm(request.user)
    return render(request, "config_usu.html", {'form': form})


class EditarUsuario(UpdateView):
    model = User
    form_class = UsuForm
    template_name = 'editar_modal.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar correctamente'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('ProsPy:LUsuarioLista')


class EliminarUsuario(DeleteView):
    model = User
    template_name = 'eliminar_modal.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            user = self.get_object()
            user.is_active = False
            user.save()
            mensaje = f'{self.model.__name__} Eliminado correctamente'
            error = 'No hay error'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('ProsPy:LUsuarioLista')



class LUTipoReactor(TemplateView):
    template_name = 'tabla_tiporeactor.html'

class TipoReactorlista(ListView):
    model = TipoReactor
    context_object_name = 'tiporeactor'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.model.objects.all()), 'aplication/json')
        else:
            return redirect('ProsPy:LUTipoReactor')

class GuardarTipo(CreateView):
    model = TipoReactor
    form_class = TipoReactorForm
    template_name = 'registro_modal_tipo.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} guardado correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo guardar correctamente'
                error = 'no se pudo guardar'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('ProsPy:LUTipoReactor')

class EditarTipo(UpdateView):
    model = TipoReactor
    form_class = TipoReactorForm
    template_name = 'editar_tiporeactor_modal.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar correctamente'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('ProsPy:LUTipoReactor')



class LUOrganismo(TemplateView):
    template_name = 'tabla_organismo.html'

class Organismolista(ListView):
    model = Organismo
    context_object_name = 'organismo'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.model.objects.all()), 'aplication/json')
        else:
            return redirect('ProsPy:LUOrganismo')

class GuardarOrganismo(CreateView):
    model = Organismo
    form_class = OrganismoForm
    template_name = 'registro_modal_organismo.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} guardado correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo guardar correctamente'
                error = 'no se pudo guardar'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('ProsPy:LUOrganismo')

class EditarOrganismo(UpdateView):
    model = Organismo
    form_class = OrganismoForm
    template_name = 'editar_organismo_modal.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar correctamente'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('ProsPy:LUOrganismo')

class EliminarOrganismo(DeleteView):
    model = Organismo
    template_name = 'eliminar_organismo_modal.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            dat = self.get_object()
            dat.delete()
            dat.save()
            mensaje = f'{self.model.__name__} Eliminado correctamente'
            error = 'No hay error'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('ProsPy:LUOrganismo')

