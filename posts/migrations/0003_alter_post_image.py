# Generated by Django 3.2.4 on 2023-12-11 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='https://res.cloudinary.com/cheymd/image/upload/v1701641092/default_profile_qdjgyp.jpg', upload_to='images/'),
        ),
    ]
