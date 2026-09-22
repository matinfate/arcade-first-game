import os
import sys


def resource_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = os.path.join(
            os.path.dirname(sys.executable),
            "_internal"
        )
    else:
        base_path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

    return os.path.join(base_path, relative_path)

def data_path(filename):
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

    data_directory = os.path.join(base_path, "data")
    os.makedirs(data_directory, exist_ok=True)

    return os.path.join(data_directory, filename)