# Generated by Django 3.1.2 on 2021-02-19 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextOz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.button')),
            ],
        ),
    ]
