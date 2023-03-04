from django.db import models


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    event_name  = models.CharField(max_length=255)
    event_date = models.DateField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name
