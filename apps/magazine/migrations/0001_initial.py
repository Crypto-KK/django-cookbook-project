# Generated by Django 2.1.9 on 2019-07-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('not_listed', 'Not Listed')], default=('draft', 'Draft'), max_length=20, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
