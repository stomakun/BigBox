from django.http import *
from django.conf import settings
from django.contrib import messages
from oauth2client import client
from apiclient.discovery import build
from .models import *


def add_storage_account(request, next_url, cloud):
    flow = client.flow_from_clientsecrets(settings.GDRIVE_SECRETS_FILE, settings.GDRIVE_SCOPE,
                                          settings.GDRIVE_REDIRECT_URL)
    flow.params['access_type'] = 'offline'
    if 'error' in request.GET:
        error_message = 'An error occurred: ' + request.GET['error']
        messages.error(request, error_message)
        return HttpResponseRedirect(next_url)
    elif 'code' in request.GET:
        try:
            credentials = flow.step2_exchange(request.GET['code'])
            id = credentials.id_token['email']
        except:
            messages.error(request, 'An error occurred')
        else:
            if StorageAccount.objects.all().filter(user=request.user).filter(identifier=id).exists():
                messages.warning(request, 'This Google Drive space is already linked to your account')
            else:
                sa = StorageAccount(user=request.user, cloud=cloud, identifier=id, status=1,
                                    refresh_token=credentials.refresh_token, access_token=credentials.access_token,
                                    access_token_expire=credentials.token_expiry, additional_data=credentials.to_json())
                sa.save()
                messages.success(request, 'A new Google Drive space is now linked to your account')
        return HttpResponseRedirect(next_url)
    else:
        auth_uri = flow.step1_get_authorize_url()
        return HttpResponseRedirect(auth_uri)
