# Generated by Django 3.1.2 on 2020-10-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('f_cost', models.CharField(max_length=20)),
                ('f_timing', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'facility',
            },
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=100)),
                ('m_age', models.CharField(max_length=20)),
                ('m_phno', models.CharField(max_length=20)),
                ('m_time', models.CharField(max_length=20)),
                ('m_years', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=100)),
                ('t_age', models.CharField(max_length=20)),
                ('t_phno', models.CharField(max_length=20)),
                ('t_hours', models.CharField(max_length=20)),
                ('t_salary', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'trainer',
            },
        ),
    ]
