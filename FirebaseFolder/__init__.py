import atexit

from ._async import process_pool
from FirebaseFolder import *


@atexit.register
def close_process_pool():
    """
    Clean up function that closes and terminates the process pool
    defined in the ``async`` file.
    """
    process_pool.close()
    process_pool.join()
    process_pool.terminate()
