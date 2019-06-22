from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from silverstrike import models

@receiver(user_signed_up)
def after_user_signed_up(request, user):
    default_account = models.Account.objects.create(
            user=user
            name='default',
            active=True,
            show_on_dashboard=True,
            account_type=models.Account.PERSONAL
        )
    import pdb; pdb.set_trace()
