from django.db import models


class Dataset(models.Model):
    file_name = models.CharField(max_length=255)
    upload_time = models.DateTimeField(auto_now_add=True)

    raw_data = models.JSONField()
    summary_stats = models.JSONField()
    equipment_distribution = models.JSONField()

    def __str__(self):
        return self.file_name
