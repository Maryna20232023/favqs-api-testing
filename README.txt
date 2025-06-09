# FavQs API Testing with Pytest

This project contains API tests for FavQs (https://favqs.com/api/) using Python, `requests`, and `pytest`.

## Project Structure

- `tests/` – test cases
- `utils/` – helper and configuration modules
- `reports/` – logs are saved here after each run
- `requirements.txt` – dependencies list

## Setup

Before running the tests, make sure to generate your API keys at [https://favqs.com/api_keys](https://favqs.com/api_keys)
and add them to a `.env` file in the root of the project in the following format:
API_KEY=your_generated_api_key


## How to Run Tests

1. Install dependencies:
pip install -r requirements.txt

2. Run specific tests with logging to console and file:
pytest tests/test_user_creation.py --capture=tee-sys
pytest tests/test_user_update.py --capture=tee-sys
Logs are saved to `reports/test_log_<timestamp>.log`

## Features

- Tests: User creation verification
- Tests: User update verification
- Positive tests
- Negative tests
- Auto-logging to `reports/` folder with timestamped log files
