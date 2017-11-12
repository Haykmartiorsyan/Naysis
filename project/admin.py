from django.contrib import admin
from .models import *

admin.site.register(Contact)
admin.site.register(Slider)

# Portfolio
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PortfolioCategory._meta.fields]

    class Meta:
        model = PortfolioCategory

admin.site.register(PortfolioCategory,PortfolioCategoryAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PortfolioItems._meta.fields]

    class Meta:
        model = PortfolioItems

admin.site.register(PortfolioItems, PortfolioAdmin)


# Blog
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PostCategory._meta.fields]

    class Meta:
        model = PostCategory

admin.site.register(PostCategory, PortfolioCategoryAdmin)


class PostCommentInline(admin.TabularInline):
    model = PostComment
    extra = 0

admin.site.register(PostComment)


class BlogPostsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BlogPosts._meta.fields]
    list_display_link = ['updated']
    list_editable = ['name']
    list_filter = ['updated', 'created']
    inlines = [PostCommentInline]

    class Meta:
        model = BlogPosts

admin.site.register(BlogPosts, BlogPostsAdmin)


# Services
class ServicesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServiceItems._meta.fields]

    class Meta:
        model = ServiceItems

admin.site.register(ServiceItems, ServicesAdmin)



