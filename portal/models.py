from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Customer(models.Model):
    """
        This model help to record customer entries in the database
    """
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    dob = models.DateField(verbose_name="Date of Birth")
    phone_no = models.CharField(max_length=13, verbose_name="Phone No.")
    email = models.EmailField(verbose_name="Email ID")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")

    class Meta:
        ordering = ("first_name",)
        constraints = [
            models.UniqueConstraint(
                fields=['dob', 'phone_no', 'email'],
                name='unique_dob_phone_email'
            )
        ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse("home")  # kwargs={"pk": self.pk}


def send_welcome_mail(user):
    try:
        # send new password email to user
        subject = "Your new account details"
        message = f"""Hi {user.first_name}, \nYou have been grant access to our portal. 
        Your user name is: {user.username} \n\n Your password is: {user.password} \n 
        Kindly change your default password as soon as possible."""
        from_email = "gajanan.kathar@outlook.com"
        user.email_user(subject, message, from_email=from_email)
    except Exception as e:
        print("User email error", e)


@receiver(pre_save, sender=Customer)
def customer_pre_save(sender, instance, **kwargs):
    if instance.id is None:
        user = User.objects.create_user(
            first_name=instance.first_name,
            last_name=instance.last_name,
            username=instance.first_name.lower(),
            email=instance.email,
        )
        temp_pass = "password"
        user.set_password(temp_pass)
        user.save()
        instance.user = user

        pre_save.disconnect(customer_pre_save, sender=Customer)
        instance.save()
        pre_save.connect(customer_pre_save, sender=Customer)


@receiver(post_save, sender=Customer)
def customer_post_save(sender, instance, created, **kwargs):
    print("post save === ", instance, created, kwargs)
    if created:
        user = instance.user
        print(user)
        send_welcome_mail(user)
