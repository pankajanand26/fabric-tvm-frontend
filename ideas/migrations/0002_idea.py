# Generated by Django 2.1.2 on 2018-10-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class1', models.CharField(max_length=200)),
                ('CRID', models.CharField(max_length=200)),
                ('market', models.CharField(max_length=200)),
                ('plantCode', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('tvmCategory', models.CharField(max_length=200)),
                ('ideaType', models.CharField(max_length=200)),
                ('partNumber', models.CharField(max_length=200)),
                ('supplierGSDB', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('ChangeFrom', models.CharField(max_length=200)),
                ('changeTo', models.CharField(max_length=200)),
                ('ideaInDate', models.CharField(max_length=200)),
                ('bcStatus', models.CharField(max_length=200)),
                ('bcDate', models.CharField(max_length=200)),
                ('leadFunction', models.CharField(max_length=200)),
                ('spoc', models.CharField(max_length=200)),
                ('ideaSource', models.CharField(max_length=200)),
                ('CRIDStage', models.CharField(max_length=200)),
                ('CRIDStatus', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
                ('expImpDate', models.CharField(max_length=200)),
                ('weekShownOnImp', models.CharField(max_length=200)),
                ('weekShownForProj', models.CharField(max_length=200)),
                ('annualSavings', models.IntegerField(default=0)),
                ('calSaving', models.IntegerField(default=0)),
                ('carryOverSavings', models.CharField(max_length=200)),
                ('ageingDays', models.IntegerField(default=0)),
                ('rank', models.CharField(max_length=200)),
                ('GSR', models.CharField(max_length=200)),
                ('ideaGeneratedBy', models.CharField(max_length=200)),
                ('dateOfImp', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
    ]