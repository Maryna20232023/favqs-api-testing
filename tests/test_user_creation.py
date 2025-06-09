import pytest
import logging
from utils.general_utils import generate_random_user, generate_invalid_logins, generate_invalid_emails, generate_invalid_passwords
from utils.customer_utils import create_user, get_user

logger = logging.getLogger()
pytestmark = [pytest.mark.api, pytest.mark.users, pytest.mark.regression]

@pytest.mark.parametrize("user", [generate_random_user() for i in range(3)])
def test_user_creation(user):
    # Create new user
    create_user_response_api = create_user(user)
    logger.info(f"Creating a user: {create_user_response_api.json()}")

    # Create user verification
    assert create_user_response_api.json()['login'] == user['user']['login'], f'API Response return wrong login. login: {user['user']['login']} '
    assert create_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {create_user_response_api.status_code},"

    # Get user verification
    requested_login = user['user']['login']
    get_user_response_api = get_user(requested_login=requested_login, user=user)
    logger.info(f"Get user: {get_user_response_api.json()}")
    assert get_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {get_user_response_api.status_code},"
    assert get_user_response_api.json()['login'] == user['user']['login'], f"API Response return wrong login."\
          f"Expected: {user['user']['login']}, Actual login: {get_user_response_api.json()['login']},"
    assert get_user_response_api.json()['account_details']['email'] == user['user']['email'], f"API Response return wrong email."\
          f"Expected: {user['user']['email']}, Actual email: {get_user_response_api.json()['account_details']['email']},"

@pytest.mark.parametrize("user", [generate_random_user() for i in range(3)])
def test_user_creation_negative_with_existing_user(user):
    # Create new user
    create_user_response_api = create_user(user)
    logger.info(f"Creating a user: {create_user_response_api.json()}")

    # Create user verification
    assert create_user_response_api.json()['login'] == user['user']['login'], f'API Response return wrong login. login: {user['user']['login']} '
    assert create_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {create_user_response_api.status_code},"

    # creating a user with an existing email
    create_user_response_api = create_user(user)
    logger.info(f"Creating user with an existing email: {create_user_response_api.json()}")

    # creating a user with an existing email verification
    assert create_user_response_api.json()["message"] == 'Username has already been taken; Email has already been taken', f"Bad mes"
    assert create_user_response_api.json()["error_code"] == 32, f"API Response return wrong error_code"\
          f"Expected: 32, Actual error_code: {create_user_response_api.json()["error_code"]},"
    assert create_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {create_user_response_api.status_code},"



@pytest.mark.parametrize("login", generate_invalid_logins())
def test_user_creation_negative_invalid_logins(login):
    user = {
        "login": login,
        "email": generate_random_user()["user"]["email"],
        "password": generate_random_user()["user"]["password"]
    }
    logger.info(f"invalid_user: {user}")
    create_user_response_api = create_user(user)
    logger.info(f"response from creating a new user: {create_user_response_api.json()}")
    assert create_user_response_api.json()['error_code'] == 32, f'data validation is not successful'
    assert create_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {create_user_response_api.status_code},"

@pytest.mark.parametrize("email", generate_invalid_emails())
def test_user_creation_negative_invalid_emails(email):
    user = {
        "login": generate_random_user()["user"]["login"],
        "email": email,
        "password": generate_random_user()["user"]["password"]
    }
    logger.info(f"invalid_user: {user}")
    create_user_response_api = create_user(user)
    logger.info(f"response from creating a new user: {create_user_response_api.json()}")
    assert create_user_response_api.json()['error_code'] == 32, f'data validation is not successful'
    assert create_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {create_user_response_api.status_code},"


@pytest.mark.parametrize("password", generate_invalid_passwords())
def test_user_creation_negative_invalid_passwords(password):
    user = {
        "login": generate_random_user()["user"]["login"],
        "email": generate_random_user()["user"]["email"],
        "password": password
    }
    logger.info(f"invalid_user: {user}")
    create_user_response_api = create_user(user)
    logger.info(f"response from creating a new user: {create_user_response_api.json()}")
    assert create_user_response_api.json()['error_code'] == 32, f'data validation is not successful'
    assert create_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {create_user_response_api.status_code},"