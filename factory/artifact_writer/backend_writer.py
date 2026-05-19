from factory.artifact_writer.file_utils import write_file


BACKEND_BASE = "backend/cars"


def write_backend_files(generated_backend):

    for filename, content in generated_backend.items():

        full_path = f"{BACKEND_BASE}/{filename}"

        write_file(full_path, content)