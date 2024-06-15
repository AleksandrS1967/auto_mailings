# Generated by Django 5.0.6 on 2024-06-15 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0002_mailing_owner_mailingmessage_owner_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailing",
            options={
                "permissions": [
                    ("can_edit_mailings_status", "Can edit Mailings status"),
                    ("can_view_mailings", "Can view Mailings"),
                ],
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
    ]