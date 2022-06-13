# Generated by Django 3.2 on 2021-06-01 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sanjivini_home', '0002_auto_20210529_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installmodel',
            name='chequeno',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='installmodel',
            name='mode_of_pay',
            field=models.CharField(blank=True, choices=[('Cheque', 'Cheque'), ('Cash', 'Cash'), ('Net Banking', 'Net Banking')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='installmodel',
            name='payid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanjivini_home.customermodel'),
        ),
        migrations.AlterField(
            model_name='paymentmodel',
            name='invoice_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanjivini_home.ordermodel'),
        ),
    ]
