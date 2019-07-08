from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

from django.utils.safestring import mark_safe



from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse







# header
admin.site.site_header ="ADMIN"
# Register your models here.
admin.site.unregister(Group)

# log
class LogEntryAdmin(admin.ModelAdmin):
    
    date_hierarchy = 'action_time'


    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]


    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag_',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def action_flag_(self, obj):
        flags = {
            1: "Addition",
            2: "Changed",
            3: "Deleted",
        }
        return flags[obj.action_flag]

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'


admin.site.register(LogEntry, LogEntryAdmin)


# slide
class SlideAdmin(admin.ModelAdmin):
    list_display    =['status','image','date']
    search_fields   =['status']
    list_filter     =['status']


admin.site.register(Slide,SlideAdmin)


#news
class NewsAdmin(admin.ModelAdmin):
    list_display    =['status','title','created_by','created_at','updated_at','image']
    search_fields   =['title']
    list_filter     =['status']
    readonly_fields = ["headshot_image"]
    def headshot_image(self, obj):
        return mark_safe('<img src="/media/{url}" width="{width}" height={height} />'.format(
            url = obj.image,
            width='211px',
            height='211px',
            )
        )

admin.site.register(New,NewsAdmin)

#comment

class CommentAdmin(admin.ModelAdmin):
    list_display    =['new_id','name','created_at']
    search_fields   =['new_id']
    list_filter     =['new_id']


admin.site.register(Comment,CommentAdmin)


#category
class CategoryAdmin(admin.ModelAdmin):
    list_display    =['name','description','created_at']
    search_fields   =['name']
    list_filter     =['name']
    readonly_fields = ["path_name"]
    class Meta:
        verbose_name = "pizza"

admin.site.register(Category,CategoryAdmin) 

#product
class ProductAdmin(admin.ModelAdmin):
    list_display    =['name','description','created_at','category_id']
    search_fields   =['name']
    list_filter     =['name']
    def category_display(self, obj):
        return ", ".join([
            category.name for child in obj.category.all()
        ])

    category_display.short_description = "Category"
admin.site.register(Product,ProductAdmin)