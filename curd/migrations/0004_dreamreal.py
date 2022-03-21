# Generated by Django 4.0.3 on 2022-03-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0003_employee1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dreamreal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
            ],
            options={
                'db_table': 'dreamreal',
            },
        ),
    ]
