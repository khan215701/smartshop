from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
# Create your models here.


class UserManager(BaseUserManager):

    def check_validations(self, username, email, password):
        # Check if the 'username' parameter is None
        if username is None:
            return TypeError("User must have a username")
        # Check if the 'email' parameter is None
        if email is None:
            return TypeError("User must have a email")
        # Check if the 'password' parameter is None
        if password is None:
            return TypeError("User must have a password")

    def get_object_by_id(self, id):
        try:
            # Attempt to retrieve an object by its ID
            instance = self.get(id=id)
            return instance
        except (ObjectDoesNotExist, TypeError, ValueError):
            # Handle the case where the object is not found
            return Http404

    def create_user(self, first_name, last_name, username, email, password=None, **kwargs):
        """Create and return a `User` with an username, email and password."""
        self.check_validations(username, email, password)
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self.db)

    def create_superuser(self, first_name, last_name, username, email, password=None, **kwargs):
        self.check_validations(username, email, password)
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            password=password)
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
