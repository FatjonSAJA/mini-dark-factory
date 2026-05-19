import time
import requests


def wait_for_backend(
    retries=20,
    delay=2
):

    for i in range(retries):

        try:

            r = requests.get(
                "http://localhost:8000/api/cars/"
            )

            if r.status_code in [200, 404]:

                print(
                    "✅ Backend healthy"
                )

                return True

        except:
            pass

        print(
            f"⏳ Waiting backend... {i+1}"
        )

        time.sleep(delay)

    return False