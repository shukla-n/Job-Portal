from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class Account(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"
        COMPANY = "COMPANY", "Company"

    base_role = Role.ADMIN
    is_active = models.BooleanField(default=False)
    can_login = models.BooleanField(default=True)
    role = models.CharField(max_length=50, choices=Role.choices)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)


class EmployeeManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=Account.Role.USER)


class Employee(Account):
    base_role = Account.Role.USER
    employee = EmployeeManager()
    # company_profile = models.ForeignKey(CompanyProfile,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        proxy = True

    
    def full_name(self):
        return self.first_name + ' ' + self.last_name



class CompanyManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=Account.Role.COMPANY)


class Company(Account):
    
    base_role = Account.Role.COMPANY
    company = CompanyManager()

    class Meta:
        proxy = True


class UserOTP(models.Model):
    otp = models.CharField(max_length=10)
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    