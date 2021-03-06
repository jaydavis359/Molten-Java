# Generated by Django 3.2.9 on 2021-12-07 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_product_has_grind'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('review', models.TextField(blank=True, max_length=1000)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1 - Yikes!'), (2, '2 - Not Good'), (3, '3 - Good'), (4, '4 - Excellent'), (5, '5 - Sublime')])),
                ('helpful', models.PositiveIntegerField(default=0)),
                ('unhelpful', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
