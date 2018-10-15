from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters
from django.urls import reverse

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
# Create your models here.

Categoria = (
    ('Asterisk', 'Asterisk'),
    ('Python', 'Python'),
    ('Docker', 'Docker'),
    ('GCD', 'Google Cloud'),
    ('AWS', 'AWS'),
    ('Cursos', 'Cursos'),
    ('Tutorial', 'Tutorial'),
    ('Linux', 'Linux'),
    ('Hackers', 'Hackers'),
    ('Django', 'Django'),
    ('Otros', 'Otros'),
    ('All', 'All'),
)

StatusPubli = (
    ('Publicada', 'Publicada'),
    ('Incompleta', 'Incompleta'),
    ('No_Publicada', 'No_Publicada'),
)

class Articles(models.Model):

    titulo = models.CharField(max_length=80)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    contenido = MarkdownxField()
    likes = models.PositiveIntegerField(default=0)
    vistas = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=20, choices=Categoria,
                                                        default='Tutorial')
    status = models.CharField(max_length=20, choices=StatusPubli,
                                                        default='Publicada')
    slug = models.SlugField(max_length=80)

    def __str__(self):
        return self.titulo

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.contenido)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.titulo)
        super(Articles, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("articulos:ver_articles", kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-id']


class Comments(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=400)
    likes = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    articuloOwn = models.ForeignKey(Articles, related_name='get_comments',
                            on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.articuloOwn.titulo
