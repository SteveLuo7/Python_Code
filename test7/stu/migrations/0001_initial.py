# Generated by Django 4.2.8 on 2023-12-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goodisd', models.AutoField(primary_key=True, serialize=False)),
                ('gname', models.CharField(max_length=30)),
                ('gdesc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('count', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('gimg', models.ImageField(upload_to='images/')),
            ],
        ),
    ]