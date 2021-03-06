# Generated by Django 4.0.2 on 2022-02-15 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(choices=[('Fant.', 'Fantasia'), ('Fic.C.', 'Ficção Científica'), ('Ação', 'Ação'), ('Aven.', 'Aventura'), ('Horror', 'Horror'), ('Susp.', 'Suspense')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('editora', models.CharField(max_length=20)),
                ('sinopse', models.TextField()),
                ('ano', models.IntegerField()),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='register.genero')),
            ],
        ),
    ]
