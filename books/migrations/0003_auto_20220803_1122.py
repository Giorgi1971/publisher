# Generated by Django 3.2.5 on 2022-08-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_booksinstore'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_receive',
            field=models.DateField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('O', 'Ordered'), ('D', 'Done')], default='O', max_length=12),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sales_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
