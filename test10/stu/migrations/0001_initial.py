# Generated by Django 4.2.8 on 2023-12-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 't_student',
            },
        ),
    ]
