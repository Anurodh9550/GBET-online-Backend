from django.contrib import admin

from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("created_at", "full_name", "mobile", "course", "city", "source", "status")
    list_filter = ("status", "source", "state")
    search_fields = ("full_name", "mobile", "email", "course", "city")
    list_editable = ("status",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 50
    fieldsets = (
        ("Student", {"fields": ("full_name", "mobile", "email", "state", "city")}),
        ("Programme", {"fields": ("course", "message", "source")}),
        ("Desk", {"fields": ("status", "note", "created_at", "updated_at")}),
    )
    actions = ("mark_called", "mark_closed")

    @admin.action(description="Mark selected enquiries as called")
    def mark_called(self, request, queryset):
        queryset.update(status=Enquiry.Status.CALLED)

    @admin.action(description="Mark selected enquiries as closed")
    def mark_closed(self, request, queryset):
        queryset.update(status=Enquiry.Status.CLOSED)
