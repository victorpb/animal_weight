# Generated by Django 2.0.6 on 2018-07-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('animal_weigth', '0004_auto_20180701_1534')]

    operations = [
        migrations.AlterField(
            model_name='farmmodel',
            name='token',
            field=models.CharField(
                default='6e1deff8a974bb9022470a4c73509fce18a420f2b00eea91ea2314cc1bab',
                max_length=30,
                unique=True,
                verbose_name='token',
            ),
        )
    ]
