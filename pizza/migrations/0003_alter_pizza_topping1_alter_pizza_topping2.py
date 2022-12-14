# Generated by Django 4.0.4 on 2022-04-21 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_toppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='topping1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.toppings'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='topping2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings2toppings', to='pizza.toppings'),
        ),
    ]
