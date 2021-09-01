from contextlib import contextmanager
import os
import tempfile


@contextmanager
def temp_file_ctx():
    fd, path = tempfile.mkstemp()

    try:
        open(fd).close()
        yield path

    finally:
        os.remove(path)
