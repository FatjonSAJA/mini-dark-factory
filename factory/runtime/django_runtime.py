import subprocess


def run_migrations():

    subprocess.run(
        [
            "python",
            "manage.py",
            "makemigrations"
        ],
        cwd="backend"
    )

    subprocess.run(
        [
            "python",
            "manage.py",
            "migrate"
        ],
        cwd="backend"
    )

    print("✅ Migrations complete")