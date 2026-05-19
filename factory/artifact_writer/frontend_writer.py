from factory.artifact_writer.file_utils import write_file


FRONTEND_BASE = "frontend/src/generated"


def write_frontend_files(generated_frontend):

    for filename, content in generated_frontend.items():

        full_path = f"{FRONTEND_BASE}/{filename}"

        write_file(full_path, content)