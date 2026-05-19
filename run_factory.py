from pathlib import Path

from factory.orchestrator import run_factory


SPEC_PATH = "specs/car_crud.md"


def main():

    spec = Path(SPEC_PATH).read_text()

    result = run_factory(spec)

    print("\n🏁 FACTORY RESULT\n")

    print(result)


if __name__ == "__main__":
    main()