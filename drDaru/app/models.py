from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True, db_index=True)
    full_name = models.CharField(max_length=255)
    hashed_password = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    cart_meli_photo = models.CharField(max_length=255)
    cart_meli_number = models.BigIntegerField()
    doctor_photo = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class License(models.Model):
    LICENSE_TYPES = [
        ('technical', 'Technical'),
        ('tasis', 'Tasis'),
    ]
    
    LICENSE_STATUSES = [
        ('bought', 'Bought'),
        ('rented', 'Rented'),
    ]
    
    type = models.CharField(max_length=10, choices=LICENSE_TYPES)
    status = models.CharField(max_length=10, choices=LICENSE_STATUSES)
    license_code = models.CharField(max_length=255)
    drugstore = models.OneToOneField('DrugStore', on_delete=models.CASCADE, related_name='license')

    def __str__(self):
        return f"{self.license_code} - {self.type}"

class DrugStore(models.Model):
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    point = models.CharField(max_length=255)
    fare = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city} - {self.location}"

class Photo(models.Model):
    photoName = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50, null=True, blank=True)
    size = models.BigIntegerField(null=True, blank=True)
    minio_url = models.URLField(max_length=255, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photoName
