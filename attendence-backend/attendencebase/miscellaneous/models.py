from django.contrib.gis.db.models import PointField
from django.db import models
import datetime


class TimeStampMixin(models.Model):
    created_on = models.DateTimeField(null=True)
    updated_on = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_on = datetime.datetime.now()
        self.updated_on = datetime.datetime.now()

        return super(TimeStampMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True