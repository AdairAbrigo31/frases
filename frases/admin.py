from django.contrib import admin
from .models import Work, Quote

# Register your models here.
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'director', 'year', 'created_at')
    list_filter = ('type', 'year')
    search_fields = ('title', 'director')


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('work', 'text_preview', 'created_at')
    list_filter = ('work__type',)
    search_fields = ('text', 'work__title')
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Quote'