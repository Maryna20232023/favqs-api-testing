BASE_URL = 'https://favqs.com/api/'
CREATE_USER_URL = f"{BASE_URL}users"
CREATE_SESSION_URL = f"{BASE_URL}session"
GET_USER_URL = lambda login: f'{BASE_URL}users/{login}'
UPDATE_USER_URL = lambda login: f'{BASE_URL}users/{login}'