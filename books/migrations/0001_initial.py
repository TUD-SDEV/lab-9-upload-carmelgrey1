# Generated by Django 3.2.7 on 2022-11-11 15:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_publication', models.DateField()),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
            ],
        ),
    ]
