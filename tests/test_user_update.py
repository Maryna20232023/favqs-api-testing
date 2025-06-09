import pytest
import logging
from utils.general_utils import generate_random_user, generate_user_data, generate_invalid_logins, generate_invalid_emails
from utils.customer_utils import create_user, get_user, update_user

logger = logging.getLogger()

pytestmark = [pytest.mark.api, pytest.mark.users, pytest.mark.regression]

@pytest.mark.parametrize("update_data", [generate_user_data() for i in range(3)])
def test_user_update(update_data, created_user):

    #Create new user
    user = created_user
    logger.info(f"Creating a user: {user}")

    # Create data for user data update
    new_data = {
        "user": {
            "login": update_data['user']['login'],
            "email": update_data['user']['email'],
        }
    }

    updated_user = {
        "user": {
            "login": new_data['user']['login'],
            "email": new_data['user']['email'],
            "password": user['user']['password']
        }
    }
    # Update user
    logger.info(f"Updating the user with new data: {new_data}")
    update_user_response_api = update_user(user, new_data)

    # Update user verification
    logger.info(f"Status code for updating user data: {update_user_response_api.status_code}")
    assert update_user_response_api.json()['message'] == 'User successfully updated.', f'User data was not updated'
    assert update_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {update_user_response_api.status_code},"

    # Get updated user data verification
    requested_login = new_data['user']['login']
    get_user_response_api = get_user(requested_login=requested_login, user=updated_user)
    logger.info(f"Get updated user data: {get_user_response_api.json()}")
    assert get_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {get_user_response_api.status_code},"
    assert get_user_response_api.json()['login'] == updated_user['user']['login'], f"API Response return wrong login."\
          f"Expected: {user['user']['login']}, Actual login: {get_user_response_api.json()['login']},"
    assert get_user_response_api.json()['account_details']['email'] == updated_user['user']['email'], f"API Response return wrong email."\
          f"Expected: {user['user']['email']}, Actual email: {get_user_response_api.json()['account_details']['email']},"

def test_user_update_negative_non_existent_user(created_user):

    # Create new valid user
    valid_user = created_user

    # Generate non_existent_user
    non_existent_user = generate_random_user()

    # Generate data for user data update
    new_data = {
        "user": {
            "login": generate_user_data()['user']['login'],
            "email": generate_user_data()['user']['email'],
        }
    }

    logger.info(f"Valid_user: {valid_user}")

    # Update user  with invalid new data
    logger.info(f"Updating the user with  new data: {new_data}")
    update_user_response_api = update_user(non_existent_user, new_data)

    # Update user verification with invalid new data
    logger.info(f"Status code for updating user data with invalid new data: {update_user_response_api.status_code}")
    logger.info(f"Message for updating user data with invalid new data: {update_user_response_api.text}")

    assert update_user_response_api.json()['error_code'] == 20, f'User session not found.'
    assert update_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {update_user_response_api.status_code},"

@pytest.mark.parametrize("login", generate_invalid_logins())
def test_user_update_negative_invalid_logins(login, created_user):
    # Create new valid user
    valid_user = created_user

    # Generate invalid new data
    invalid_new_data = {
        "login": login,
        "email": generate_random_user()["user"]["email"],
    }
    logger.info(f"Valid_user: {valid_user}")

    # Update user  with invalid new data
    logger.info(f"Updating the user with invalid new data: {invalid_new_data}")
    update_user_response_api = update_user(valid_user, invalid_new_data)

    # Update user verification with invalid new data
    logger.info(f"Status code for updating user data with invalid new data: {update_user_response_api.status_code}")
    logger.info(f"Message for updating user data with invalid new data: {update_user_response_api.text}")

    assert update_user_response_api.json()['error_code'] == 32, f'data validation is not working correctly'
    assert update_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {update_user_response_api.status_code},"

@pytest.mark.parametrize("email", generate_invalid_emails())
def test_user_update_negative_invalid_emails(email, created_user):

    # Create new valid user
    valid_user = created_user
    # Generate invalid new data
    invalid_new_data = {
        "login": generate_random_user()["user"]["login"],
        "email": email
    }
    logger.info(f"Valid_user: {valid_user}")

    # Update user with invalid new data
    logger.info(f"Updating the user with invalid new data: {invalid_new_data}")
    update_user_response_api = update_user(valid_user, invalid_new_data)

    # Update user verification with invalid new data
    logger.info(f"Status code for updating user data with invalid new data: {update_user_response_api.status_code}")
    logger.info(f"Message for updating user data with invalid new data: {update_user_response_api.text}")

    assert update_user_response_api.json()['error_code'] == 32, f'data validation is not working correctly'
    assert update_user_response_api.status_code == 200, f"Bad Status code."\
          f"Expected: 200, Actual status code: {update_user_response_api.status_code},"
