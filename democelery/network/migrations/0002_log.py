# Generated by Django 3.2.1 on 2021-05-14 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_to', models.CharField(max_length=1000, verbose_name='Enviado a')),
                ('data', models.TextField(verbose_name='Data')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
    ]
