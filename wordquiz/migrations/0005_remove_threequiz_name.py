# Generated by Django 2.2.1 on 2019-06-04 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordquiz', '0004_auto_20190604_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threequiz',
            name='name',
        ),
    ]
