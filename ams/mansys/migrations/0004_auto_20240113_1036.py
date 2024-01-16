# Generated by Django 3.1.2 on 2024-01-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mansys', '0003_faculty_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civil',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='civil',
            name='subjectid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='civil',
            name='subjectname',
            field=models.CharField(blank=True, default='NA', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='csbs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='csbs',
            name='subjectid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='csbs',
            name='subjectname',
            field=models.CharField(blank=True, default='NA', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='csd',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='csd',
            name='subjectid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='csd',
            name='subjectname',
            field=models.CharField(blank=True, default='NA', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cse',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cse',
            name='subjectid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cse',
            name='subjectname',
            field=models.CharField(blank=True, default='NA', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='csm',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='csm',
            name='subjectid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='csm',
            name='subjectname',
            field=models.CharField(blank=True, default='NA', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ece',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ece',
            name='subjectid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ece',
            name='subjectname',
            field=models.CharField(blank=True, default='NA', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='eee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='eee',
            name='subjectid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='eee',
            name='subjectname',
            field=models.CharField(blank=True, default='NA', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mech',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mech',
            name='subjectid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mech',
            name='subjectname',
            field=models.CharField(blank=True, default='NA', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]