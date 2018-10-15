from django.shortcuts import render
from django.views.generic import (ListView, CreateView, DeleteView,
                                    UpdateView, DetailView)
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ArticlesCreateForm, SearchForm, CommentsForm

from .models import Articles, Comments
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class ArticlesList(ListView):
    model = Articles
    paginate_by = 5
    fields = ['titulo', 'autor' 'contenido', 'categoria', 'slug']
    form_class = SearchForm
    #context_object_name = 'articulos'
    template_name = 'articulos/home_list.html'

    def get_context_data(self, **kwargs):
        context =super(ArticlesList, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context


def ArticlesListFilter(request):
    #Vista para el filtro
    form = SearchForm
    if request.method == 'POST' and request.POST['q'] == '':
        form = SearchForm(request.POST)
        if form.is_valid(): #si el formulario en valido
            datos = form.cleaned_data
            filterRecive = datos['Categorias']
            if 'All' in filterRecive:
                return HttpResponseRedirect('/')
            elif filterRecive != []: #si el formulario NO esta vacio
                queryset = Articles.objects.filter(
                                            categoria__in=filterRecive)
            else:
                return HttpResponseRedirect('/')
    elif request.method == 'POST' and request.POST['q'] != '':
        queryset = Articles.objects.filter(titulo__icontains=request.POST['q'])
        filterRecive = []
    elif request.method == 'GET':
        filterRecive = request.GET.get('filtro')
        #recive por get en string asi lo cambio a lista
        import ast; filterRecive = ast.literal_eval(filterRecive)
        queryset = Articles.objects.filter(categoria__in=filterRecive)
    else:
        return HttpResponseRedirect('/')

    paginator = Paginator(queryset, 5)
    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    #objectFilter es para mantener los datos de filtro en la paginacion por GET
    #'page_obj': object_list lo mandamos para mantener compatibilidad con las
    #class view que san ese nombre para el paginador
    ctx = {'form': form, 'object_list': object_list, 'page_obj': object_list,
           'objectFilter': filterRecive}
    return render(request, 'articulos/home_list.html', ctx)


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'User.is_staff'
    model = Articles
    template_name = 'articulos/crear_articulo.html'
    form_class = ArticlesCreateForm
    success_url = reverse_lazy('articulos:list_articles')

    def get_context_data(self, **kwargs):
        context =super(ArticlesCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = User.objects.get(username=request.user)
            articulo.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'User.is_staff'
    model = Articles
    template_name = 'articulos/update_articulo.html'
    form_class = ArticlesCreateForm
    success_url = reverse_lazy('articulos:list_articles')

    def get_context_data(self, **kwargs):
        context =super(ArticlesUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        articulo = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_articulo = kwargs['pk']
        articulo = self.model.objects.get(id=id_articulo)
        form = self.form_class(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'User.is_staff'
    model = Articles
    success_url = reverse_lazy('articulos:list_articles')


class ArticlesVer(DetailView):
    model = Articles
    template_name = 'articulos/ver_articulo.html'
    form_class = CommentsForm

    def get_context_data(self, **kwargs):
        context =super(ArticlesVer, self).get_context_data(**kwargs)
        sumaVistas = context['object']
        sumaVistas.vistas += 1
        sumaVistas.save()
        print(context['object'].vistas)
        if 'form' not in context:
            context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            slug = kwargs['slug']
            comentario = form.save(commit=False)
            comentario.autor = User.objects.get(username=request.user)
            comentario.articuloOwn = self.model.objects.get(slug=slug)
            comentario.save()
        return HttpResponseRedirect(comentario.articuloOwn.get_absolute_url())

def LoadComment(request):
    pass
