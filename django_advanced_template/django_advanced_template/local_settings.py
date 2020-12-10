import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

#REMEMBER TO CHANGE THIS!!
SECRET_KEY = 'mjqukiixswytfz(exsa50-0fnl8+k4j(=b%rq9$8_+*n5j@6gl'

DEBUG = True

# sentry_sdk.init(
#     dsn="https://XX@XX.ingest.sentry.io/XX",
#     integrations=[DjangoIntegration()],
#     traces_sample_rate=1.0,
#
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )
