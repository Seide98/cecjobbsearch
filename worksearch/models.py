from django.db import models
from django.conf import settings
from django.urls import reverse

WORKS_ACTIVITY = (
    ('Work application','Work application'),
    ('Registration of interest', 'Registration of interest'),
    ('Other activity','Other activity'),
)

class Post(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    link = models.URLField('Application Link')
    choises_activity = models.CharField(max_length=25, choices=WORKS_ACTIVITY, default="Work application")
    date_added = models.DateField(auto_now_add=True)
    free_text_field = models.TextField(blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.company) + ' | ' + str(self.date_added) + ' | ' + str(self.user)

    def get_absolute_url(self):
        return reverse('worksearch')

class PostPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    link = models.URLField('Application Link')
    choises_activity = models.CharField(max_length=25, choices=WORKS_ACTIVITY, default="Work application")
    last_app_date = models.DateField('Last Date to Apply')
    free_text_field = models.TextField(blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.company) + ' | ' + str(self.last_app_date) + ' | ' + str(self.user)

    def get_absolute_url(self):
        return reverse('worksearch')

class PostUserSett(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.URLField('Link to websites')


    def __str__(self):
        return self.title + ' | ' + str(self.user)

    def get_absolute_url(self):
        return reverse('worksearch')

class PostUserUpload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    document = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.document) + ' | ' + str(self.user)

    def get_absolute_url(self):
        return reverse('worksearch')

