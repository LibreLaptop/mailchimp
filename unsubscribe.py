import hashlib
import mailchimp_marketing as MlMark
from mailchimp_marketing.api_client import ApiClientError

api_key = ""
server_prefix = "us5"

mailchimp = MlMark.Client()
mailchimp.set_config(api_key, server_prefix)

list_id = ""
member_email = mail
member_email_hash = hashlib.md5(member_email.encode('utf-8').lower()).hexdigest()
member_update = {"status": "unsubscribed"}

try:
    response = mailchimp.lists.update_list_member(list_id, member_email_hash, member_update)
    print("Response: {}".format(response))
except ApiClientError as error:
    print("An exception occurred: {}".format(error.text))
