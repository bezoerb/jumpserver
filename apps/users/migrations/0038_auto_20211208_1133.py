# Generated by Django 3.1.13 on 2021-12-08 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_auto_20210929_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userpasswordhistory',
            options={'verbose_name': 'User password history'},
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, default='User', max_length=10, verbose_name='Role'),
        ),
    ]
