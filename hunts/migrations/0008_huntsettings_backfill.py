# Generated by Django 4.0.1 on 2022-01-06 23:08
from django.db import migrations
from django.template.defaultfilters import slugify
from django.conf import settings


def add_settings(apps, schema_editor):
    Hunt = apps.get_model("hunts", "Hunt")
    HuntSettings = apps.get_model("hunts", "HuntSettings")
    for hunt in Hunt.objects.all():
        if not hasattr(hunt, "settings"):
            hunt_settings = HuntSettings(
                hunt=hunt,
                google_drive_folder_id=settings.GOOGLE_DRIVE_HUNT_FOLDER_ID or "",
                google_sheets_template_file_id=settings.GOOGLE_SHEETS_TEMPLATE_FILE_ID
                or "",
                google_drive_human_url=settings.GOOGLE_HUMAN_DRIVE_HUNT_FOLDER_URL
                or "",
                discord_guild_id=settings.DISCORD_GUILD_ID or "",
                discord_puzzle_announcements_channel_id=settings.DISCORD_PUZZLE_ANNOUNCEMENTS_CHANNEL
                or "",
                discord_text_category=settings.DISCORD_TEXT_CATEGORY or "",
                discord_voice_category=settings.DISCORD_VOICE_CATEGORY or "",
                discord_archive_category=settings.DISCORD_ARCHIVE_CATEGORY or "",
                discord_devs_role=settings.DISCORD_DEVS_ROLE or "",
            )
            hunt_settings.save()


class Migration(migrations.Migration):

    dependencies = [
        ("hunts", "0007_huntsettings"),
    ]

    operations = [
        migrations.RunPython(
            add_settings,
            reverse_code=migrations.RunPython.noop,
        )
    ]