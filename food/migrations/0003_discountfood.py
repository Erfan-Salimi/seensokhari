# Generated by Django 3.0 on 2022-06-21 15:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_food_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('value', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('food', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FoodDiscount', to='food.Food')),
            ],
        ),
    ]
