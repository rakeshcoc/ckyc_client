from django.db import models
status_CHOICES = (('Submitted','Submitted'),("Verification Failed","Verification Failed"),
					("Verified","Verified"),("Rejected_by_blockchain","Rejected_by_blockchain"),
					("Approved","Approved"))
# Create your models here.
class txn_flow(models.Model):
	status = models.CharField(choices=status_CHOICES,max_length=100)
	txn_id = models.CharField(primary_key=True,max_length=100)
	remarks = models.CharField(max_length =200,default="")
	digital_id = models.CharField(max_length=20)
	def __str__(self):
		return str(self.txn_id)
