# Generated by Django 4.2.2 on 2023-06-21 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category_of_tech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category_of_tech.category')),
            ],
        ),
    ]