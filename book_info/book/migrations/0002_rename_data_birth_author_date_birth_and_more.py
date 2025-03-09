# Сгенерировано Django 4.2.1 2025-03-08 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='data_birth',
            new_name='date_birth',
        ),
        migrations.AlterField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reader_book', to=settings.AUTH_USER_MODEL),
        ),
    ]