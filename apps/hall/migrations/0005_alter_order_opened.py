# Generated by Django 3.2.7 on 2022-03-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0004_rename_clostime_order_closetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='opened',
            field=models.BooleanField(default=True),
        ),
    ]