from flask_mail import Message
from flask import render_template
from app import mail, app



def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)



# Password reset email

def send_password_reset_email(user):
    """Send password reset email"""
    token = user.get_reset_password_token()
    send_email(
        "[Taskmate] Reset Your Password",
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[user.email],
        text_body=render_template(
            "emails/reset_password.txt", user=user, token=token),
        html_body=render_template(
            "emails/reset_password.html", user=user, token=token))


# Overdue task email

def overdue_task_email_notification(user, task):
    """Update user of new task"""
    send_email(
        "[Taskmate] Overdue Task",
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[user.email],
        text_body=render_template(
            "emails/overdue_task.txt", user=user, task=task),
        html_body=render_template(
            "emails/overdue_task.html", user=user, task=task))


# Thank you for registration

def thank_you_user(username, email):
    """Email sent to user"""
    send_email(
        "[Taskmate] Thank you for your registration.",
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[email],
        text_body=render_template(
            "emails/thank_you_signup.txt", username=username),
        html_body=render_template(
            "emails/thank_you_signup.html", username=username))
