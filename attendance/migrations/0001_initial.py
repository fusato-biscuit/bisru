# Generated by Django 3.0.6 on 2020-05-24 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uezu_seminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=7)),
                ('attended_day', models.DateField(verbose_name='出席日')),
            ],
        ),
    ]
