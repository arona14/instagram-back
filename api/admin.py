from wagtail.contrib.modeladmin.options import(
    ModelAdmin,
    modeladmin_register,
)
from .models import Like, Profile, Photo, Album, Comment, Like


class ProfileAdmin(ModelAdmin):
    model = Profile
    menu_label = 'Profiles'
    menu_icon = 'Placeholder'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("user", "bio", "logo",)
    search_field = ("user",)
    
modeladmin_register(ProfileAdmin)

class PhotoAdmin(ModelAdmin):
    model = Photo
    menu_label = 'Photos'
    menu_icon = 'Placeholder'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("image", "profile",)
    search_field = ("profile",)
    
modeladmin_register(PhotoAdmin)


class AlbumAdmin(ModelAdmin):
    model = Album
    menu_label = 'Albums'
    menu_icon = 'Placeholder'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("profile", "photos",)
    search_field = ("profile",)

modeladmin_register(AlbumAdmin)


class CommentAdmin(ModelAdmin):
    model = Comment
    menu_label = 'Comments'
    menu_icon = 'Placeholder'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("profile", "photo", "content",)
    search_field = ("profile",)

modeladmin_register(CommentAdmin)


class LikeAdmin(ModelAdmin):
    model = Like
    menu_label = 'Likes'
    menu_icon = 'Placeholder'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("profile", "photo",)
    search_field = ("profile",)

modeladmin_register(LikeAdmin)
