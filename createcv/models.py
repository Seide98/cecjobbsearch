from django.db import models
from django.conf import settings
from django.urls import reverse

class PostCreateCV(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    # picture,
    cvname = models.CharField(max_length=255)
    # education,
    # workexperiance,
    # lang,
    # otherskills,
    # references,
    # shortdescription,
    # firstname
    # lastname
    # phone
    # email
    # title

    def __str__(self):
        return str(self.cvname) + ' | ' + str(self.user)

    def get_absolute_url(self):
        return reverse('worksearch')