# Generated by Django 5.1.1 on 2024-09-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_alter_aluno_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='alunos'),
        ),
    ]
