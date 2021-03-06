# Generated by Django 4.0.3 on 2022-04-22 06:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('breeze', '0004_remove_shoppinglist_list_id_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, help_text='Unique User ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('default_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
