# Generated by Django 2.2.2 on 2019-06-14 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('easydilemma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReasonPartTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('selected_option', models.CharField(max_length=50)),
                ('dilemma', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='easydilemma.DilemmaPartTwo')),
            ],
        ),
    ]