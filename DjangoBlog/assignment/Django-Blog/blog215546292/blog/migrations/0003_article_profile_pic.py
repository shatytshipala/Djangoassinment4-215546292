# Generated by Django 4.2.4 on 2023-08-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]