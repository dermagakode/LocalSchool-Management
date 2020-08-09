import time

from django.db import models
from django.utils.text import slugify
from config.conn import mqtt_publish

def group_based_upload_to(instance, filename):
    return f"{instance.teaching_materials.school}/{instance.teaching_materials.grade}/{filename}"

class TeachingMaterials(models.Model):
    school = models.CharField(verbose_name='Sekolah', max_length=50) # Sekolah
    grade = models.CharField(verbose_name='Tingkat kelas', max_length=50) # Tingkat kelas
    subject = models.CharField(verbose_name='Mata Pelajaran', max_length=50) # Mata Pelajaran
    topic = models.CharField(verbose_name='Topik', max_length=50) # Topik

    def save(self, *args, **kwargs):
        topic = f'ntm/{slugify(self.school) }/{slugify(self.grade)}' # slugify become kebab case
        mqtt_publish(topic, str(time.time()))
        super(TeachingMaterials, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.school} {self.grade}: {self.subject} {self.topic}'

class Attachments(models.Model):
    teaching_materials = models.ForeignKey(TeachingMaterials, on_delete=models.CASCADE, related_name='attachments')
    docs = models.FileField(upload_to=group_based_upload_to)
