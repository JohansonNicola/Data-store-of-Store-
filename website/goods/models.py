from django.db import models

# Create your models here.
class good(models.Model):
    title = models.CharField(max_length=300)
    isbn = models.CharField(max_length=50)
    Supplier = models.CharField(max_length=50)
    weight = models.FloatField(blank=True, null=True)
    Price = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    def __repr__(self) -> str:
        return "<good id={} title={} weight={}>".format(
            self.id, self.title, self.weight
        )
