from django.db import models
import secrets

class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length= 200)
    verified=models.BooleanField(default=False)
    date= models.DateTimeField(auto_now_add=True)

class Meta:
    ordering= ('date_created')

    def __str__(self) -> str:
        return f"Payment:  {self.Amount}"
    
def save(self, *args,**kwargs) -> None:

    while not self.ref:

        ref = secrets.token_urlsafe(50)
        object_with_similar_ref= Payment.objects.filter(ref=ref)
        if not object_with_similar_ref:
            self.ref =ref
    super().save(*args, **kwargs)

def amount_value(self) -> int:
    return self.amount*100

