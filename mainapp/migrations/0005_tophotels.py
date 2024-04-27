# Generated by Django 3.2.19 on 2024-02-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_topplaces_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tophotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=3000)),
                ('photo', models.ImageField(upload_to='static/img')),
                ('place', models.CharField(max_length=250)),
                ('Style', models.CharField(max_length=250)),
                ('Attractions', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'Tophotels',
            },
        ),
    ]
