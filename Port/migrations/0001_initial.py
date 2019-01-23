# Generated by Django 2.1.5 on 2019-01-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.TextField()),
            ],
        ),
    ]
