from django.conf import settings
def bankname(request):
    return {
        'bankname': settings.BANK_NAME
    }
