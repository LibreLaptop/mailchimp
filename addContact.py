import mailchimp_marketing as MlMark
from mailchimp_marketing.api_client import ApiClientError

mailchimp = MlMark.Client()
mailchimp.set_config({
    "api_key":"",
    "server":"us5"
})
def addContact(lista,mail,nombres,apellidos):
        list_id = lista #nombre de mailing list
        #add a contact to mailing list_id
        member_info = {
            "email_address": mail,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": nombres,
                "LNAME": apellidos
            }
        }
        try:
            response = mailchimp.lists.add_list_member(list_id, member_info)
            print("response: {}".format(response))
        except ApiClientError as error:
            print("An exception occurred: {}".format(error.text))
