# Generated by Django 2.2.16 on 2020-11-04 10:43

from django.db import migrations


def create_waffle_switch(apps, schema_editor):
    Switch = apps.get_model("waffle", "Switch")

    Switch.objects.create(
        name="disable-linter-xpi-autoclose",
        active=False,
        note=(
            "Disable the XPI auto-close feature in addons-linter (which should"
            " improve the overall performances)."
        ),
    )


class Migration(migrations.Migration):

    dependencies = [
        ("scanners", "0040_scannerqueryresult_was_blocked"),
    ]

    operations = [migrations.RunPython(create_waffle_switch)]
