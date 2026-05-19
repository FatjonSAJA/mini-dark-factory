import subprocess


django_process = None


def start_django():

    global django_process

    if django_process:
        return

    django_process = subprocess.Popen(
        [
            "python",
            "manage.py",
            "runserver",
            "8000"
        ],
        cwd="backend"
    )

    print("🚀 Django server started")


def stop_django():

    global django_process

    if django_process:

        django_process.terminate()

        django_process = None

        print("🛑 Django server stopped")