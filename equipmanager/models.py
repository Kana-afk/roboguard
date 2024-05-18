from django.db import models

from django.db import models

# Equipment model

class Equipment(models.Model):
    TYPE_CHOICES = [
        ('robot', 'Robot'),
        ('machine', 'Machine'),
        ('sensor', 'Sensor'),
    ]

    name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.name

# Data model

class Data(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='data')
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Data for {self.equipment.name} at {self.timestamp}"

# Alert model

class Alert(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='alerts')
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.equipment.name}: {self.description}"

