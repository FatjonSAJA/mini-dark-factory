import requests

BASE_URL = "http://localhost:8000/api/cars/"


def run_tests():

    tests = []

    # LIST TEST
    try:
        r = requests.get(BASE_URL)

        tests.append({
            "name": "list_cars",
            "status": r.status_code == 200,
            "details": "GET /api/cars returned 200"
        })


    except Exception as e:
        tests.append({
            "name": "list_cars",
            "status": False,
            "details": str(e)
        })

    return tests