from msal import ConfidentialClientApplication
from config.settings import settings

msal_app = ConfidentialClientApplication(
    client_id=settings.msal_client_id,
    authority=settings.msal_authority,
    client_credential=settings.msal_client_secret
)
