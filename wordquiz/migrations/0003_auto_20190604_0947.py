# Generated by Django 2.2.1 on 2019-06-04 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordquiz', '0002_threequiz_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threequiz',
            name='tag',
            field=models.IntegerField(),
        ),
    ]
