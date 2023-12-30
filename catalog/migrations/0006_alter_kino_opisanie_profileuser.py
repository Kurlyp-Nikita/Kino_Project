# Generated by Django 4.2.7 on 2023-12-17 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0005_kino_treler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kino',
            name='opisanie',
            field=models.TextField(max_length=50000, verbose_name='Описание'),
        ),
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podpiska', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.podpiska')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]