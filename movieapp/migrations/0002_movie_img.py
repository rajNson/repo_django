# Generated by Django 3.1.7 on 2023-02-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='jujub', upload_to='gallary'),
            preserve_default=False,
        ),
    ]
