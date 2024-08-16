from django.db import models

# Create your models here.

class Dueño(models.Model):
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)

    def __str__(self):
        pass

    class Meta:
        db_table = 'TestDeDueño'
        managed = True
        verbose_name = 'Dueño'
        verbose_name_plural = 'Dueños'
        
class Doctor(models.Model):
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    specialization = models.CharField(max_length=45)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        
class Mascota(models.Model):
    name = models.CharField(max_length=45)
    owner = models.ForeignKey(Dueño, on_delete=models.CASCADE)
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

class Cita(models.Model):
    description = models.CharField(max_length=45)
    client = models.ForeignKey(Dueño, on_delete=models.CASCADE)
    pet = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'