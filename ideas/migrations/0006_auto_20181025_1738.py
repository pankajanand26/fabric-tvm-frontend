# Generated by Django 2.1.2 on 2018-10-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0005_auto_20181025_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='idea',
            name='CRID',
            field=models.CharField(max_length=200),
        ),
    ]