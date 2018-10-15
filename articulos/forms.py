from .models import Articles, Categoria, Comments
from django import forms

class SearchForm(forms.Form):
    Categorias = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=Categoria, required=False)

#class CommentsForm(forms.Form):
#    comentario = forms.CharField(widget=forms.Textarea(
#                        attrs={'width':"70%", 'cols' : "50", 'rows': "4", }))

class CommentsForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ['comment']
        widgets = { 'comment': forms.Textarea(
                        attrs={'width':"70%", 'cols' : "50", 'rows': "4", })
                  }


class ArticlesCreateForm(forms.ModelForm):

    class Meta():
        model = Articles
        fields = [
            'titulo',
            'contenido',
            'categoria',
            'status',
            'autor',
        ]
        labels = {
            'titulo': 'Titulo',
            'contenido': 'Contenido',
            'categoria': 'Categorias',
            'status': 'Status',
            'autor': 'autor',
        }
        widgets = {
            'autor': forms.HiddenInput(),
   #         'nombre': forms.TextInput(attrs={'class': 'form-control'}),
    #        'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
     #       'edad': forms.TextInput(attrs={'class': 'form-control'}),
        #     'contenido': forms.Textarea(attrs={'class': 'form-control'}),
        #     'categoria': forms.CheckboxSelectMultiple(),
        #     'status': forms.CheckboxSelectMultiple,
                      }
#        help_texts = {
#            'name': _('Some useful help text.'),
#        }
#        error_messages = {
#            'name': {
#                'max_length': _("This writer's name is too long."),
#            },
#        }
