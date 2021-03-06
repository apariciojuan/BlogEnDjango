# Generated by Django 2.0.6 on 2018-10-12 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0005_auto_20180930_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='comentarios',
        ),
        migrations.AddField(
            model_name='comments',
            name='articuloOwn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articulos.Articles'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='categoria',
            field=models.CharField(choices=[('Asterisk', 'Asterisk'), ('Python', 'Python'), ('Docker', 'Docker'), ('GCD', 'Google Cloud'), ('AWS', 'AWS'), ('Cursos', 'Cursos'), ('Tutorial', 'Tutorial'), ('Linux', 'Linux'), ('Hackers', 'Hackers'), ('Django', 'Django'), ('Otros', 'Otros'), ('All', 'All')], default='Tutorial', max_length=20),
        ),
    ]
