# Generated by Django 4.2.7 on 2024-09-07 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('restaurant_type', models.CharField(choices=[('american', 'American'), ('mexican', 'Mexican'), ('chinese', 'Chinese'), ('japanese', 'Japanese'), ('italian', 'Italian'), ('other', 'Other')], default='other', max_length=10)),
                ('location', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('menu_category', models.CharField(choices=[('appetizer', 'Appetizer'), ('main_course', 'Main Course'), ('dessert', 'Dessert'), ('drink', 'Drink')], default='main_course', max_length=20)),
                ('modifiers', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('available_stock', models.IntegerField()),
                ('order_count', models.IntegerField(default=0)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item', to='restaurants.menu')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='restaurants.restaurant'),
        ),
    ]
