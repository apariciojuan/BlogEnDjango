# Generated by Django 2.1.1 on 2018-09-16 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('contenido', markdownx.models.MarkdownxField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('vistas', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('Publicada', 'Publicada'), ('Incompleta', 'Incompleta'), ('No_Publicada', 'No_Publicada')], default='No_Publicada', max_length=20)),
                ('slug', models.SlugField(max_length=80)),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('Asterisk', 'Asterisk'), ('Python', 'Python'), ('Docker', 'Docker'), ('GCD', 'Google Cloud'), ('AWS', 'AWS'), ('Cursos', 'Cursos'), ('Tutorial', 'Tutorial'), ('Linux', 'Linux'), ('Hackers', 'Hackers'), ('Django', 'Django'), ('All', 'All')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(max_length=400)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='categoria',
            field=models.ManyToManyField(blank=True, to='articulos.Category'),
        ),
        migrations.AddField(
            model_name='articles',
            name='comentarios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articulos.Comments'),
        ),
    ]
