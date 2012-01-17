from modeltranslation.admin import TranslationAdmin
from django.contrib import admin

from mezzanine.blog.admin import BlogPostAdmin

class TranslatedBlogPostAdmin(BlogPostAdmin, TranslationAdmin):
    pass
