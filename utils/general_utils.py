import random
import string
def generate_random_user(email_domain=None, email_prefix=None):
    if not email_domain:
        email_domain = 'gmail.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_login_string_length = 10
    random_login = ''.join(random.choices(string.ascii_lowercase, k=random_login_string_length))
    login = random_login

    random_email_string_length = 10
    random_email = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + '_' + random_email + '@' + email_domain

    random_password_string_length = 20
    random_password = ''.join(random.choices(string.ascii_letters, k=random_password_string_length))
    password = random_password

    random_user = {
        "user": {
            "login": login,
            "email": email,
            "password": password
        }
    }
    print(random_user)
    return random_user

def generate_user_data(email_domain=None, email_prefix=None):
    if not email_domain:
        email_domain = 'gmail.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_login_string_length = 10
    random_login = ''.join(random.choices(string.ascii_lowercase, k=random_login_string_length))
    login = random_login

    random_email_string_length = 10
    random_email = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + '_' + random_email + '@' + email_domain

    random_password_string_length = 20
    random_password = ''.join(random.choices(string.ascii_letters, k=random_password_string_length))
    password = random_password

    random_twitter_username_string_length = 20
    random_twitter_username = ''.join(random.choices(string.ascii_lowercase, k=random_twitter_username_string_length))
    twitter_username = random_twitter_username

    random_facebook_username_string_length = 20
    random_facebook_username = ''.join(random.choices(string.ascii_lowercase, k=random_facebook_username_string_length))
    facebook_username = random_facebook_username

    random_pic = random.choice(["twitter", "facebook", "gravater", ""])

    random_profanity_filter = random.choice([True, False])

    random_user_data = {
      "user": {
        "login": login,
        "email": email,
        "password": password,
        "twitter_username": twitter_username,
        "facebook_username": facebook_username,
        "pic": random_pic,
        "profanity_filter": random_profanity_filter
      }
    }
    print(random_user_data)
    return random_user_data

def generate_invalid_logins():
    list_of_invalid_logins = []
    invalid_login = [
        "",  # Порожній логін
        ''.join(random.choices(string.ascii_letters + string.digits, k=51)),  # Занадто довгий
        'login ' + ''.join(random.choices(string.ascii_lowercase, k=5)) + ' spaces',  # Пробіли
        'логін_' + ''.join(random.choices('йцукенгшщзфівапролджєячсмить', k=5)),  # Нелатиниця
        ''.join(random.choices('!@#$%^&*()_+=[]{}|;', k=8)),  # Символи
        'user\nname' + str(random.randint(1, 9)),  # Спецсимволи
        random.randint(10000, 99999),  # Не рядок
        None  # None
    ]
    for i in invalid_login:
        list_of_invalid_logins.append(i)
    print(f'list of inv {list_of_invalid_logins}')
    return list_of_invalid_logins

def generate_invalid_emails():
    list_of_invalid_emails = []
    invalid_emails = [
        "",  # Порожній
        ''.join(random.choices(string.ascii_letters + string.digits, k=10)),  # Без @
        '@' + ''.join(random.choices(string.ascii_lowercase, k=5)) + '.com',  # Без ім’я
        ''.join(random.choices(string.ascii_lowercase, k=5)) + '@.com',  # Немає домену
        ''.join(random.choices(string.ascii_lowercase, k=5)) + '@domain',  # Без точки
        ''.join(random.choices(string.ascii_lowercase, k=5)) + ' domain.com',  # Пробіли
        ''.join(random.choices(string.ascii_lowercase, k=5)) + '@domain..com',  # Подвійна крапка
        ''.join(random.choices(string.ascii_lowercase, k=5)) + '@.domain.com',  # Починається з крапки
        random.randint(10000, 99999),  # Не рядок
        None  # None
    ]
    for i in invalid_emails:
        list_of_invalid_emails.append(i)
    print(f'list of inv {list_of_invalid_emails}')
    return list_of_invalid_emails

def generate_invalid_passwords():
    list_of_invalid_passwords = []
    invalid_passwords = [
        "",  # Порожній
        ''.join(random.choices(string.ascii_letters, k=1)),  # Занадто короткий
        ''.join(random.choices(string.ascii_letters + string.digits, k=51)),  # Занадто довгий
        'pass ' + ''.join(random.choices(string.ascii_lowercase, k=5)) + ' word',  # Пробіли
        'пароль' + ''.join(random.choices('йцукенгшщзфівапролджєячсмить', k=3)),  # Нелатиниця
        ''.join(random.choices('!@#$%^&*()_+=[]{}|;', k=8)),  # Тільки символи
        'pass\nword' + str(random.randint(1, 9)),  # Спецсимволи (\n)
        random.randint(10000, 99999),  # Не рядок
        None  # None
    ]
    for i in invalid_passwords:
        list_of_invalid_passwords.append(i)
    print(f'list of inv {list_of_invalid_passwords}')
    return list_of_invalid_passwords