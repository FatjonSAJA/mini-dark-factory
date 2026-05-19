import requests


BASE_URL = "http://localhost:8000/api/cars/"


def run_tests():

    tests = []

    try:

        # CREATE

        payload = {
            "plate_number": "AA123AA",
            "brand": "Audi",
            "model": "Q5",
            "year": 2024
        }

        r = requests.post(
            BASE_URL,
            json=payload
        )

        create_ok = r.status_code in [200, 201]

        tests.append({
            "name": "create_car",
            "status": create_ok,
            "details": r.text
        })

        # LIST

        r = requests.get(BASE_URL)

        list_ok = r.status_code == 200

        tests.append({
            "name": "list_cars",
            "status": list_ok,
            "details": r.text
        })

    except Exception as e:

        tests.append({
            "name": "crud_test",
            "status": False,
            "details": str(e)
        })

    return tests