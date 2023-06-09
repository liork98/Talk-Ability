# Generated by Django 4.2.1 on 2023-05-11 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('language', models.CharField(choices=[('EN', 'English'), ('SP', 'Spanish'), ('FR', 'French'), ('GE', 'German'), ('CH', 'Chinese'), ('HE', 'Hebrew'), ('AR', 'Arabic'), ('RU', 'Russian')], max_length=15)),
                ('age', models.IntegerField()),
                ('city', models.CharField(choices=[('NY', 'New York'), ('LA', 'Los Angeles'), ('CH', 'Chicago'), ('HO', 'Houston'), ('PH', 'Phoenix'), ('SA', 'San Antonio'), ('SD', 'San Diego'), ('DA', 'Dallas'), ('SJ', 'San Jose'), ('AU', 'Austin'), ('JA', 'Jacksonville'), ('FW', 'Fort Worth')], max_length=15)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('ID', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('ID', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('origin_transcript', models.CharField(max_length=200)),
                ('target_transcript', models.CharField(max_length=200)),
                ('origin_language', models.CharField(choices=[('EN', 'English'), ('SP', 'Spanish'), ('FR', 'French'), ('GE', 'German'), ('CH', 'Chinese'), ('HE', 'Hebrew'), ('AR', 'Arabic'), ('RU', 'Russian'), ('OTHER', 'Other')], default='EN', max_length=15)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled'), ('FAILED', 'Failed')], default='PENDING', max_length=15)),
                ('department', models.CharField(choices=[('LEGAL', 'Legal'), ('MEDICAL', 'Medical'), ('FINANCIAL', 'Financial'), ('TECHNICAL', 'Technical'), ('EDUCATIONAL', 'Educational'), ('BUSINESS', 'Business'), ('OTHER', 'Other')], default='OTHER', max_length=15)),
                ('time_of_request', models.DateTimeField(verbose_name='date published')),
                ('request_summary', models.CharField(max_length=200)),
                ('customer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.customer')),
                ('representative_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.representative')),
            ],
        ),
    ]
