from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        """representing the record in Admin site """
        return f'{self.name}'


class Member(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=11)
    client_member_id = models.CharField(max_length=30)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['phone_number', 'account_id'], name='unique_phone_number'),
            models.UniqueConstraint(fields=['client_member_id', 'account_id'], name='unique_client_member_id')
        ]

    def __str__(self):
        """representing the record in Admin site """
        return f'{self.first_name} {self.last_name}'