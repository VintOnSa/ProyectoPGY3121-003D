# Generated by Django 4.2.2 on 2023-06-26 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Store', '0005_delete_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
