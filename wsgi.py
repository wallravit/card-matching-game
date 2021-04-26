import os

from api import create_app


def set_python_path():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    base_dir = os.path.join(script_dir, "..")
    sys.path.append(base_dir)


app = create_app()