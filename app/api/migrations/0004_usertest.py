# Generated by Django 3.2.8 on 2022-05-12 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_felling_dailyfeeling_feeling'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('datetimes', models.CharField(max_length=50)),
                ('question1', models.CharField(max_length=250)),
                ('answer1', models.CharField(max_length=250)),
                ('question2', models.CharField(max_length=250)),
                ('answer2', models.CharField(max_length=250)),
                ('question3', models.CharField(max_length=250)),
                ('answer3', models.CharField(max_length=250)),
                ('question4', models.CharField(max_length=250)),
                ('answer4', models.CharField(max_length=250)),
                ('question5', models.CharField(max_length=250)),
                ('answer5', models.CharField(max_length=250)),
                ('question6', models.CharField(max_length=250)),
                ('answer6', models.CharField(max_length=250)),
                ('question7', models.CharField(max_length=250)),
                ('answer7', models.CharField(max_length=250)),
                ('question8', models.CharField(max_length=250)),
                ('answer8', models.CharField(max_length=250)),
                ('question9', models.CharField(max_length=250)),
                ('answer9', models.CharField(max_length=250)),
                ('question10', models.CharField(max_length=250)),
                ('answer10', models.CharField(max_length=250)),
                ('question11', models.CharField(max_length=250)),
                ('answer11', models.CharField(max_length=250)),
                ('question12', models.CharField(max_length=250)),
                ('answer12', models.CharField(max_length=250)),
                ('question13', models.CharField(max_length=250)),
                ('answer13', models.CharField(max_length=250)),
                ('question14', models.CharField(max_length=250)),
                ('answer14', models.CharField(max_length=250)),
                ('question15', models.CharField(max_length=250)),
                ('answer15', models.CharField(max_length=250)),
                ('question16', models.CharField(max_length=250)),
                ('answer16', models.CharField(max_length=250)),
                ('question17', models.CharField(max_length=250)),
                ('answer17', models.CharField(max_length=250)),
                ('question18', models.CharField(max_length=250)),
                ('answer18', models.CharField(max_length=250)),
                ('question19', models.CharField(max_length=250)),
                ('answer19', models.CharField(max_length=250)),
                ('question20', models.CharField(max_length=250)),
                ('answer20', models.CharField(max_length=250)),
                ('question21', models.CharField(max_length=250)),
                ('answer21', models.CharField(max_length=250)),
            ],
        ),
    ]
