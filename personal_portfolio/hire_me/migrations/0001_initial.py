# Generated by Django 4.0 on 2021-12-30 22:30

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
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=255)),
                ('project_type', models.CharField(choices=[('web', 'Web app'), ('mobile', 'Mobile app'), ('desktop', 'Desktop app')], max_length=100)),
                ('budget_range', models.DecimalField(decimal_places=2, max_digits=10)),
                ('details', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
