import requests


BASE_URL = "http://localhost:8000/api/cars/"


def run_tests():

    tests = []

    try:

        payload = {
            "plate_number": "AA123AA",
            "brand": "Audi",
            "model": "Q5",
            "year": 2024
        }

        # CREATE

        r = requests.post(
            BASE_URL,
            json=payload
        )

        create_ok = r.status_code in [200, 201]

        data = r.json()

        car_id = data["id"]

        tests.append({
            "name": "create_car",
            "status": create_ok,
            "details": data
        })

        # LIST

        r = requests.get(BASE_URL)

        list_ok = r.status_code == 200

        tests.append({
            "name": "list_cars",
            "status": list_ok,
            "details": r.json()
        })

        # UPDATE

        update_payload = {
            "plate_number": "BB999BB",
            "brand": "BMW",
            "model": "X5",
            "year": 2025
        }

        r = requests.put(
            f"{BASE_URL}{car_id}/",
            json=update_payload
        )

        update_ok = r.status_code == 200

        tests.append({
            "name": "update_car",
            "status": update_ok,
            "details": r.json()
        })

        # DELETE

        r = requests.delete(
            f"{BASE_URL}{car_id}/"
        )

        delete_ok = r.status_code in [200, 204]

        tests.append({
            "name": "delete_car",
            "status": delete_ok,
            "details": r.text
        })

    except Exception as e:

        tests.append({
            "name": "crud_test",
            "status": False,
            "details": str(e)
        })

    return tests