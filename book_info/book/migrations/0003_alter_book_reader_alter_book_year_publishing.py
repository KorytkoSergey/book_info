# Generated by Django 4.2.1 on 2023-05-15 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0002_alter_author_author_id_alter_book_book_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='reader_book',
                to=settings.AUTH_USER_MODEL),

        ),
        migrations.AlterField(
            model_name='book',
            name='year_publishing',
            field=models.IntegerField(blank=True,
                                      null=True,
                                      verbose_name='Год издания'),
        ),
    ]
