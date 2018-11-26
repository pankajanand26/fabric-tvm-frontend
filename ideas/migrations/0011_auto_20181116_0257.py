# Generated by Django 2.1.2 on 2018-11-15 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0010_auto_20181116_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='CRID',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='CRIDStage',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='ChangeFrom',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='GSR',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='bcDate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='carryOverSavings',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='changeTo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='class1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='dateOfImp',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='expImpDate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='ideaGeneratedBy',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='ideaInDate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='ideaSource',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='ideaType',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='leadFunction',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='market',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='model',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='owner',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partNumber',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='plantCode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='rank',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='remark',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='spoc',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='supplierGSDB',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='tvmCategory',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='weekShownForProj',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='weekShownOnImp',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=100),
        ),
    ]
