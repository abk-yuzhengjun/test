from django.contrib import admin
from myapp.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    # inlines = [TagInline]
    # fieldsets = (
    #     ['Main',{
    #         'fields':('name','email')
    #     }],
    #     ['Advance', {
    #         'classes': ('collapse',),
    #         'fields':('age',),
    #     }],
    # )
    list_display = ('id','name','age','email')
    search_fields = ('name',)

class TestAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

admin.site.register(Contact,ContactAdmin)
admin.site.register(Test,TestAdmin)
admin.site.register([Tag])
