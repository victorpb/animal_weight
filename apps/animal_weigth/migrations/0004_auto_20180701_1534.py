# Generated by Django 2.0.6 on 2018-07-01 18:34

import apps.animal_weigth.choices
import dj.choices.fields
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [('animal_weigth', '0003_farmmodel_token')]

    operations = [
        migrations.CreateModel(
            name='AnimalWeigthModel',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name='created'
                    ),
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name='modified'
                    ),
                ),
                (
                    'type_animal',
                    dj.choices.fields.ChoiceField(
                        choices=apps.animal_weigth.choices.AnimalChoice,
                        default=1,
                        verbose_name='Tipo do Animal',
                    ),
                ),
                (
                    'weigth',
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name='Peso do animal'
                    ),
                ),
                (
                    'earring_number',
                    models.CharField(max_length=15, verbose_name='Número do brinco'),
                ),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='farmmodel',
            name='token',
            field=models.CharField(
                default='900d37be696cea145432e448d0ff088795b35017668b050547e728b7c0be',
                max_length=30,
                unique=True,
                verbose_name='CNPJ',
            ),
        ),
        migrations.AddField(
            model_name='animalweigthmodel',
            name='farm',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='animal_witgth_farm',
                to='animal_weigth.FarmModel',
            ),
        ),
    ]