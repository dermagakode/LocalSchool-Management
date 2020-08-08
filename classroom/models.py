from django.db import models

def group_based_upload_to(instance, filename):
    return f"{instance.teaching_materials.school}/{instance.teaching_materials.grade}/{filename}"

class TeachingMaterials(models.Model):
    school = models.CharField(verbose_name='Sekolah', max_length=50) # Sekolah
    grade = models.CharField(verbose_name='Tingkat kelas', max_length=50) # Tingkat kelas
    subject = models.CharField(verbose_name='Mata Pelajaran', max_length=50) # Mata Pelajaran
    topic = models.CharField(verbose_name='Topik', max_length=50) # Topik

class Attachments(models.Model):
    teaching_materials = models.ForeignKey(TeachingMaterials, on_delete=models.CASCADE, related_name='attachments')
    docs = models.FileField(upload_to=group_based_upload_to)
