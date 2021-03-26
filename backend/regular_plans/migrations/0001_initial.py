import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RegularPlan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("tar_included", models.BooleanField()),
                ("subscription", models.FloatField()),
                (
                    "cycle",
                    models.CharField(
                        choices=[("W", "Weekly"), ("D", "Daily")], max_length=1
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("bi", "bi-time"),
                            ("tri", "tri-time"),
                            ("simple", "simple"),
                        ],
                        max_length=6,
                    ),
                ),
                ("offer_iva", models.BooleanField()),
                ("off_peak_price", models.FloatField()),
                ("peak_price", models.FloatField()),
                (
                    "unit",
                    models.CharField(
                        choices=[("KWH", "kwh"), ("MIN", "min")], max_length=3
                    ),
                ),
                ("valid", models.BooleanField()),
                ("publish", models.BooleanField()),
                (
                    "vat",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="plans",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
