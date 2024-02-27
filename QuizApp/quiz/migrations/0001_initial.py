# Generated by Django 5.0.2 on 2024-02-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('question_text', models.TextField()),
                ('correct_answer', models.CharField(max_length=255)),
                ('options', models.JSONField()),
            ],
        ),
    ]