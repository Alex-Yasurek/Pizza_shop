# Generated by Django 4.0.4 on 2022-04-21 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.CharField(choices=[('cheese', 'Cheese'), ('pepperoni', 'Pepperoni'), ('chicken', 'Chicken'), ('peppers', 'Peppers'), ('sausage', 'Sausage'), ('olives', 'Olives')], default='Cheese', max_length=20)),
            ],
        ),
    ]
