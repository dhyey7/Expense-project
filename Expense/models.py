from django.db import models
from User.models import User
# Create your models here.

class Category (models.Model):
    #categoryid = models.AutoField(primary_key=True)
    categoryname=models.CharField(max_length=100)
    
    class meta:
        db_table = 'Category'
    def __str__(self):
        return self.categoryname
        
        
class Subcategory (models.Model):
    #subcategoryid = models.AutoField(primary_key=True)
    subcategoryname=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class meta:
        db_table = 'Subcategory'
    def __str__(self):
        return self.subcategoryname
        
class Label (models.Model):
    #labelid = models.AutoField(primary_key=True)
    labelname=models.CharField(max_length=100)
    
    class meta:
        db_table = 'label'
    def __str__(self):
        return self.labelname
            

        
class Payee (models.Model):
    #pld=models.CharField (primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
   
    class meta:
        db_table = 'Payee'
    def __str__(self):
        return self.name
        

paymentMethods = (('cash','Cash'), ('cheque', 'Cheque'), ('creditcard','creditcard'))        
class Accounttype (models.Model):
    #accountTypeId = models.CharField(primary_key=True)
    typeName = models.CharField(choices=paymentMethods, max_length=50)
     
    class meta:
        db_table = 'Accounttype'
    def __str__(self):
        return self.typeName
       

class Currencytype(models.Model):
    #currencytypeid = models.CharField(primary_key=True)
    Currency = models.CharField(max_length=50)

    class meta:
        db_table = 'Currencytype'
    def __str__(self):
        return self.Currency
        
        
class Account(models.Model):
    #accountId = models.CharField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.FloatField()
    currencyType=models.ForeignKey(Currencytype, on_delete=models.CASCADE)
    default = models.CharField(max_length=50)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) 
    # accountType =models.CharField(models.ForeignKey("app.Model", on_delete=models.CASCADE))
 
    class meta:
        db_table = 'Account'
  
        
status = (('cleared','cleared'),('uncleared','uncleared'),('void','void'))
transaction=(('expense','expense'),('income','income'))
class Expense(models.Model):
    #expenseId = models.CharField(primary_key=True)
    amount = models.FloatField()
    expDateTime = models.DateField()
    payee = models.ForeignKey(Payee, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategory =models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    paymentMethod=models.CharField(choices=paymentMethods ,max_length=30)
    status = models.CharField(choices=status, max_length=30)
    description=models.CharField(max_length=100)
    transactionType=models.CharField(choices=transaction, max_length=50)
        
    class meta:
        db_table = 'expense'
        
    def __str__(self):
        return str(self.amount)
