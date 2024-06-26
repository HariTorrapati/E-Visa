# Generated by Django 3.2.19 on 2024-02-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topplaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=2000)),
                ('photo', models.ImageField(upload_to='images/uploads')),
                ('TimetoVisit', models.CharField(max_length=250)),
                ('HowtoReach', models.CharField(max_length=250)),
                ('Attractions', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'Topplaces',
            },
        ),
    ]
