from django.contrib import admin
from .models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("short_text", "author", "approved", "created_at")
    list_filter = ("approved",)
    list_editable = ("approved",)
    search_fields = ("text", "author")
    actions = ["approve_quotes", "unapprove_quotes"]

    def short_text(self, obj):
        return obj.text[:60] + "..." if len(obj.text) > 60 else obj.text
    short_text.short_description = "Quote"

    @admin.action(description="Approve selected quotes")
    def approve_quotes(self, request, queryset):
        queryset.update(approved=True)

    @admin.action(description="Unapprove selected quotes")
    def unapprove_quotes(self, request, queryset):
        queryset.update(approved=False)
