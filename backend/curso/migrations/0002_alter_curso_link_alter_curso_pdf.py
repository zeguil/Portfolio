# Generated by Django 4.0.2 on 2022-02-07 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='link',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='pdf',
            field=models.FileField(upload_to=''),
        ),
    ]