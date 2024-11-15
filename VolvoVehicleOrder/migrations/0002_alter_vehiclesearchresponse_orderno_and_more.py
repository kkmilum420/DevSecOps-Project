# Generated by Django 4.1.5 on 2023-07-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("VolvoVehicleOrder", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehiclesearchresponse",
            name="orderNo",
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name="vehiclesearchresponse",
            name="orderQty",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="vehiclesearchresponse",
            name="orderTotalCost",
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name="vehiclesearchresponse",
            name="requestedDeliveryDate",
            field=models.CharField(default="", max_length=10),
        ),
    ]
