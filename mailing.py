'''from mailchimp_marketing import Client
mailchimp = Client()
Mailchimp.set_config({
    "api_key":"883b2275140025309af4299d6f4a88b2-us5",
    "server":"us5"
})

response = mailchimp.ping.get()
print(response)'''

import mailchimp_markenting as MlMark
from mailchimp_marketing.api_client import ApiClientError

mailchimp = MlMark.Client()
Mailchimp.set_config({
    "api_key":"883b2275140025309af4299d6f4a88b2-us5",
    "server":"us5"
})
body ={
    "permission_reminder":"You signed up for updates on our website",
    "email_type_option":False,
    "campaign_defaults":{
        "from_name":"Mailchimp",
        "from_email":"freddie@mailchimp.com",
        "subject":"Python Devs",
        "language":"EN_US"
    }
