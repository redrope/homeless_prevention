# Generated by Django 3.1.1 on 2020-10-28 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0017_utilities_statement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilities',
            name='statement',
        ),
        migrations.AddField(
            model_name='utilities',
            name='payment_due_date',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('ACCEPTED', 'ACCEPTED'), ('RESUBMIT', 'RESUBMIT')], default='NEW', max_length=100)),
                ('date_uploaded', models.DateField()),
                ('doc_type', models.CharField(choices=[('Lease Agreement', 'Lease Agreement'), ('Mortgage Statement', 'Mortgage Statement'), ('Electric Bill', 'Electric Bill'), ('Water Bill', 'Water Bill'), ('Gas Bill', 'Gas Bill'), ('Identification', 'Identification'), ('Pay Stub', 'Pay Stub'), ('Crisis/COVID Letter', 'Crisis/COVID Letter')], max_length=100)),
                ('doc_file', models.FileField(upload_to=home.models.user_directory_path)),
                ('comment', models.TextField(blank=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]