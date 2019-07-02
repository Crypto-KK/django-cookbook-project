# Generated by Django 2.1.9 on 2019-07-02 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('meta_keywords', models.CharField(blank=True, help_text='Separate keywords with commas.', max_length=255, verbose_name='Keywords')),
                ('meta_description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('meta_author', models.CharField(blank=True, max_length=255, verbose_name='Author')),
                ('meta_copyright', models.CharField(blank=True, max_length=255, verbose_name='Copyright')),
                ('title_en_us', models.CharField(blank=True, db_tablespace='', max_length=200, verbose_name='Title (US English)')),
                ('title_zh_hans', models.CharField(db_tablespace='', max_length=200, verbose_name='Title (Asia/Shanghai)')),
                ('description_en_us', models.TextField(blank=True, db_tablespace='', verbose_name='Description (US English)')),
                ('description_zh_hans', models.TextField(blank=True, db_tablespace='', verbose_name='Description (Asia/Shanghai)')),
                ('content_en_us', models.TextField(blank=True, db_tablespace='', verbose_name='Content (US English)')),
                ('content_zh_hans', models.TextField(db_tablespace='', verbose_name='Content (Asia/Shanghai)')),
                ('categories', models.ManyToManyField(blank=True, related_name='ideas', to='demo_app.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(default='', help_text='Please enter the ID of the related object.', max_length=255, verbose_name='Related object')),
                ('owner_object_id', models.CharField(default='', help_text='Please enter the ID of the related object.', max_length=255, verbose_name='Owner')),
                ('content_type', models.ForeignKey(help_text='Please select the type (model) for the relation, you want to build.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name="Related object's type (model)")),
                ('owner_content_type', models.ForeignKey(help_text='Please select the type (model) for the relation, you want to build.', limit_choices_to={'model__in': ('user', 'institution')}, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='contenttypes.ContentType', verbose_name="Owner's type (model)")),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
    ]
