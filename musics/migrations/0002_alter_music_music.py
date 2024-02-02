# Generated by Django 4.2.9 on 2024-02-02 21:51

from django.db import migrations, models
import musics.validators


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='music',
            field=models.FileField(upload_to='musics', validators=[musics.validators.validate_is_audio]),
        ),
    ]