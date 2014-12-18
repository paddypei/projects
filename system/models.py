from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.role_name
    class Meta:
        #abstract = True
        #app_label = "blog"
        db_table = "role"
