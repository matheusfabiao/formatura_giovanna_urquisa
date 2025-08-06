from django.contrib import admin
from .models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone')
    ordering = ('-created_at',)
    
    def message_preview(self, obj):
        if obj.message:
            if len(obj.message) > 30:
                return obj.message[:30] + '...'
            else:
                return obj.message
        else:
            return '-'

    message_preview.short_description = 'Mensagem'
