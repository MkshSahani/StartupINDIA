# Generated by Django 3.0.3 on 2020-11-01 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartUpProduct',
            fields=[
                ('productID', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=200)),
                ('productType', models.CharField(max_length=100)),
                ('shortDescription', models.TextField()),
                ('patent', models.BooleanField(default=False)),
                ('company_ceo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_company', to='start_app.Company_CEO')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
