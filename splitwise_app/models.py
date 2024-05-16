from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile_no = models.CharField(max_length=200)


class AccountSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_acc_setting')
    simplyfy = models.BooleanField(default=False)
    
class Expense(models.Model):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"
    ACTIVE= "ACTIVE"
    SETTLED_UP= "SETTLED_UP"
    SHARE_TYPE = {
        EQUAL: "Equal",
        EXACT: "Exact",
        PERCENT: "Percent",
    }
    
    STATUS = {
        ACTIVE: "Active",
        SETTLED_UP: "Settled Up",
    }
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='expense_paid_by')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='expense_added_by')
    description = models.TextField()
    amount = models.FloatField(default=0.0)
    currency = models.CharField(max_length=3) # iso code
    paid_on=models.DateTimeField()
    share_bitween= models.JSONField()
    share_type = models.CharField(
        max_length=8,
        choices=SHARE_TYPE,
        default=EQUAL,
    )
    status=models.CharField(
        max_length=12,
        choices=STATUS,
        default=EQUAL,
    )
    

class Transaction(models.Model):
    PENDING="PENDING"
    IN_PROGRESS='IN_PROGRESS'
    PAID="PAID"
    STATUS = {
        PENDING: "Pending",
        IN_PROGRESS:'In Progress',
        PAID: "Paid",
    }
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE,related_name='txn_expense')
    txn_id = models.UUIDField()
    amount = models.FloatField(default=0.0)
    currency = models.CharField(max_length=3) # iso code
    from_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='txn_from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='txn_to_user')
    paid_on=models.DateTimeField()
    status=models.CharField(
        max_length=12,
        choices=STATUS,
        default=PENDING,
    )
    