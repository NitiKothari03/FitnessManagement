from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True) 
    password = models.CharField(max_length=30)

    def _str_(self):
        return self.email

class Trainees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=10, 
        choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHERS', 'Others')],
        default='MALE'
    )
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    goal = models.CharField(
        max_length=20,
        choices=[('CUTTING', 'Cutting'), ('BULKING', 'Bulking'), ('WEIGHTLOSS', 'Weightloss'), ('PYSIQUE', 'Physique')],
        default='WEIGHTLOSS')
    health_issues = models.CharField(
        max_length=20, 
        choices=[('DIABETES', 'Diabetes'), ('CHOLESTEROL', 'Cholesterol'), ('THYROID', 'Thyroid'), ('OTHERS', 'Others'), ('NONE', 'None')],
        default='NONE')
    email = models.EmailField(max_length=30, unique=True) 
    password = models.CharField(max_length=30)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def _str_(self):
        return self.email