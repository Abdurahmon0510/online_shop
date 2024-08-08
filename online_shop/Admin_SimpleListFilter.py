from django.contrib import admin
class IsVeryExpensiveFilter(admin.SimpleListFilter):
    title = 'Very expensive products'
    parameter_name = 'is_very_expensive_product'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )
    def queryset(self, request, queryset):
        value=self.value()
        if value == 'Yes':
            return queryset.filter(price__gt=700)
        elif value == 'No':
            return queryset.exclude(price__gt=700)
        return queryset
