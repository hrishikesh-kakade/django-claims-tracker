from django.db import models

# Create your models here.
class Claim(models.Model):

    

    case_id=models.CharField(max_length=20)
    policy_id=models.CharField(max_length=20)
    claim_date=models.DateField()
    sum_insured_inr=models.PositiveIntegerField()
    DECISION_CHOICES = [
        ('APPROVED', 'Approved'),
        ('NEEDS_REVIEW', 'Needs Review'),
        ('REJECTED', 'Rejected'),
    ]
    decision = models.CharField(
        max_length=30,
        choices=DECISION_CHOICES
    )

    def __str__(self):
            return self.case_id