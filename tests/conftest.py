import pytest
import logging
import os
from datetime import datetime
from utils.general_utils import generate_random_user, generate_user_data
from utils.customer_utils import create_user, create_session

os.makedirs("reports", exist_ok=True)
log_filename = f"reports/test_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filename, mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()

@pytest.fixture(autouse=True)
def log_test_start_and_end(request):
    logger.info(f"\n🔹 START TEST: {request.node.name}")
    yield
    logger.info(f"✅ END TEST: {request.node.name}\n")

def pytest_runtest_makereport(item, call):
    # Лог статусу тесту після виконання (фаза 'call' - основне виконання тесту)
    if call.when == "call":
        status = "PASS" if call.excinfo is None else "FAIL"
        logger.info(f"📝 STATUS TEST: {item.name} — {status}")

@pytest.fixture
def created_user():
    user = generate_random_user()
    response = create_user(user)
    assert response.status_code == 200, f"User not created: {response.text}"
    assert response.json()['login'] == user['user']['login'], f"API Response return wrong login. login: {user['user']['login']}"
    return user

