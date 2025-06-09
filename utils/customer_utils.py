import requests
from utils.general_utils import generate_random_user
from utils.endpoints import CREATE_USER_URL, CREATE_SESSION_URL, GET_USER_URL, UPDATE_USER_URL
from utils.config import headers_auth, headers_auth_user_session

def create_user(user=None):
    if not user:
        user = generate_random_user()
    response = requests.post(CREATE_USER_URL, json=user, headers=headers_auth)
    response_api = response.json()
    print(response_api)
    return response

def create_session(user):
    response = requests.post(CREATE_SESSION_URL, json=user, headers=headers_auth)
    response_api = response.json()
    error_code = response_api.get("error_code")
    print(response_api)
    if 'User-Token' in response_api:
        return response_api['User-Token']
    elif error_code == 21:
        print(f"Error 21: Invalid username or password – {response.json().get('message')}")
    elif error_code == 22:
        print(f"Error 22: Account not activated – {response.json().get('message')}")
    elif error_code == 23:
        print(f"Error 23: Username or password missing – {response.json().get('message')}")
    else:
        print(f"Unknown session creation error: {response.json().get('message')}")

    return None

def get_user(requested_login, user):
    user_token = create_session(user)
    get_user_url = GET_USER_URL(requested_login)
    headers_auth_user_session = headers_auth.copy()
    headers_auth_user_session.update({"User-Token": user_token})
    response = requests.get(get_user_url, headers=headers_auth_user_session)
    print(response.json())
    return response


def update_user(user, new_data):
    user_token = create_session(user)
    headers_auth_user_session = headers_auth.copy()
    headers_auth_user_session.update({"User-Token": user_token})
    update_user_url = UPDATE_USER_URL(user['user']['login'])
    response = requests.put(update_user_url, json= new_data, headers=headers_auth_user_session)
    return response
