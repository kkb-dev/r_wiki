# Generated by Django 3.1.7 on 2021-03-17 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210317_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='char_sheet',
        ),
        migrations.AddField(
            model_name='sheet',
            name='rank_e',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='rank_i',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='rank_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='rank_r',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='rank_s',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='rank_t',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sheet',
            name='t_affil',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheet',
            name='t_age',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheet',
            name='t_bday',
            field=models.CharField(default=1.0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheet',
            name='t_bplace',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheet',
            name='t_debut',
            field=models.CharField(default='dynasty', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheet',
            name='t_form',
            field=models.CharField(default='Morph', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheet',
            name='t_img',
            field=models.FilePathField(null=True, path='/images', recursive=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]