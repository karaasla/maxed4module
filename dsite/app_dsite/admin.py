from django.contrib import admin
from .models import Dsite
from django.db.models.query import QuerySet


class DsiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_at', 'created_date', 'updated_date']
    list_filter = ['auction', 'created_at', 'price']
    actions = ['make_action_as_false', 'make_action_as_true']
    fieldsets = (
        ('Общие', {
            'fields': (
                'title', 'description'
            ),
        }),
        ('Финансы', {
            'fields': (
                'price', 'auction'
            ),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset: QuerySet):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset: QuerySet):
        queryset.update(auction=True)


admin.site.register(Dsite, DsiteAdmin)



