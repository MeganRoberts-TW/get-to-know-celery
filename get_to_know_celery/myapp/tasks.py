from celery import shared_task
import time

@shared_task
def send_fake_email(user_email):
    print(f"Starting to send email to {user_email}")
    time.sleep(5)  # Delay if needed
    print(f"Finished sending email to {user_email}")
    return f"Email sent to {user_email}"
