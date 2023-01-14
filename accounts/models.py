from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django_countries.fields import CountryField
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email,
                    password=None):
        if not email:
            return ValueError('User must input email address')

        if not username:
            ValueError('User must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username,
                         password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    """Base account class"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    phone_number = models.CharField(max_length=25)

    # Required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # Change the base login to email address
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    """User profile to extend the account profile
    Added images so they can be displayed on the blog if users comment.
    """
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    street_address1 = models.CharField(blank=True, max_length=100)
    street_address2 = models.CharField(blank=True, default=00, max_length=100)
    town_or_city = models.CharField(blank=True, max_length=30)
    county = models.CharField(blank=True, default=00, max_length=30)
    postcode = models.CharField(blank=True, max_length=30)
    country = CountryField(blank=True, max_length=30)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'(self.street_address1) (self.street_address2)'
