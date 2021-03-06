# Generated by Django 3.0.2 on 2020-08-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(default='None', max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('spouse_name', models.CharField(default='None', max_length=100)),
                ('nominee_name', models.CharField(max_length=100)),
                ('mobile_no', models.IntegerField()),
                ('aadharcard', models.IntegerField()),
                ('pancard', models.CharField(blank=True, default='None', max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('checkbook', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=200)),
                ('spouse_bod', models.DateField(default='01/01/1970')),
                ('married_status', models.BooleanField(default=True)),
                ('education', models.CharField(default='None', max_length=50)),
                ('caste', models.CharField(max_length=10)),
                ('annual_income', models.IntegerField()),
                ('ammount', models.FloatField()),
                ('interest_ammount', models.FloatField()),
                ('occupation', models.CharField(max_length=20)),
                ('place_of_birth', models.CharField(max_length=20)),
                ('income_category', models.CharField(max_length=100)),
                ('nature_of_barring', models.CharField(max_length=100)),
                ('loan_date', models.DateField()),
                ('interest_date', models.DateField()),
                ('profile', models.ImageField(blank=True, upload_to='imgs/')),
                ('distric', models.CharField(default='None', max_length=10)),
            ],
        ),
    ]
