# Generated by Django 4.2.8 on 2023-12-12 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 't_student',
            },
        ),
        migrations.CreateModel(
            name='Scard',
            fields=[
                ('stud', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stu1.student')),
                ('department', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 't_scard',
            },
        ),
    ]
