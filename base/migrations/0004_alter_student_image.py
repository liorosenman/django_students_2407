# Generated by Django 5.0.7 on 2024-07-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]