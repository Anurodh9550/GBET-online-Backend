from django.apps import AppConfig


class LeadsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "leads"
    verbose_name = "Admissions desk"

    def ready(self):
        from django.contrib import admin

        admin.site.site_header = "GBET Online desk"
        admin.site.site_title = "GBET Online"
        admin.site.index_title = "Enquiries"
