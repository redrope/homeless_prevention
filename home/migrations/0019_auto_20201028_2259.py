# Generated by Django 3.1.1 on 2020-10-28 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20201028_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilities',
            name='payment_due_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
