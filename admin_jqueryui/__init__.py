from django.contrib.admin.options import ModelAdmin

old_media = ModelAdmin.media


def new_media(self):
    media_instance = old_media.fget(self)
    media_instance.add_js(('admin_jqueryui/js/admin_jqueryui.min.js',))
    return media_instance
ModelAdmin.media = property(new_media)
