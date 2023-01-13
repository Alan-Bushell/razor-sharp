# Generated by Django 3.2 on 2023-01-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=700)),
                ('reason', models.CharField(choices=[('order', 'Order Tracking'), ('general', 'General Query'), ('complaint', 'Complaint'), ('return', 'Return Request')], max_length=15)),
            ],
        ),
    ]
