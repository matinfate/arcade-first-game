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

