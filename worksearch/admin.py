from django.contrib import admin
from .models import Post, PostPlan,PostUserSett, PostUserUpload

# Register your models here.
admin.site.register(Post)
admin.site.register(PostPlan)
admin.site.register(PostUserSett)
admin.site.register(PostUserUpload)