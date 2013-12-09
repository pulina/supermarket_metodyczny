from django.contrib.admin.options import ModelAdmin


old_media = ModelAdmin.__dict__['media']


def new_media(self):
    media_instance = old_media.fget(self)
    media_instance.add_js(('force_jquery.js',))
    return media_instance

ModelAdmin.media = property(new_media)
