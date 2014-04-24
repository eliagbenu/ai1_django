from django.db import models

# Create your models here.

def upload_avatar_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'profiles/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )

class Bank(models.Model):
    bank_name = models.CharField(max_length=30)
    website_address = models.URLField()
    avatar = models.ImageField("Avatar", upload_to=upload_avatar_to, blank=True)

    def __unicode__(self):
        return self.bank_name


