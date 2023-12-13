# Generated by Django 4.2.8 on 2023-12-12 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clazz',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 't_cls',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu2.clazz')),
            ],
            options={
                'db_table': 't_stu2',
            },
        ),
    ]