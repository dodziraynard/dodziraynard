import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient


# update to your dynamic template id from the UI
TEMPLATE_ID = 'd-57284dc5b6204b22b4e95d86075db174'

# list of emails and preheader names, update with yours

def SendDynamic(from_email, to_emails, fullname):
    message = Mail(
        from_email=from_email,
        to_emails=to_emails)

    # pass custom values for our HTML placeholders
    message.dynamic_template_data = {
        'subject': 'Welcome! We think you will love it here.',
        'fullname': fullname
    }
    message.template_id = TEMPLATE_ID
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY')) ## (^_^) This face is just to grab your attention for api key needed
        response = sg.send(message)
    except Exception as e:
        print("Error: {0}".format(e))
    return str(response.status_code)