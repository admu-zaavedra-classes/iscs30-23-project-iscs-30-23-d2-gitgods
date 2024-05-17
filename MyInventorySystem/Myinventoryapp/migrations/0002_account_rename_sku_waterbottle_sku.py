# Generated by Django 4.1.5 on 2023-05-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myinventoryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
        migrations.RenameField(
            model_name='waterbottle',
            old_name='sku',
            new_name='SKU',
        ),
    ]