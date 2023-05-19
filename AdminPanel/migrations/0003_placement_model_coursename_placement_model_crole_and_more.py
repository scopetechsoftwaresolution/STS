# Generated by Django 4.1.7 on 2023-05-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0002_alter_placement_model_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement_model',
            name='coursename',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='placement_model',
            name='crole',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='placement_model',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='placement_model',
            name='cname',
            field=models.CharField(max_length=100),
        ),
    ]
