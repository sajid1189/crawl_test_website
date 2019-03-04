# Generated by Django 2.1.7 on 2019-03-04 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_pages', models.IntegerField()),
                ('links_per_page', models.SmallIntegerField(default=15)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pagestructure',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Site'),
        ),
    ]
