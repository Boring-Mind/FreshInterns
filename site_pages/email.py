from post_office import mail


def send_email(message: str):
    mail.send(
        ['super.d3280@ya.ru'],
        'FreshInterns <freshinternships@gmail.com>',
        subject='Internship candidates',
        message=message,
    )
