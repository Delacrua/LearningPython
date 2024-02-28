import asyncio
import os.path
import sys
sys.path.insert(1, os.path.join(sys.path[0], ".."))

from queries.core import get_data_sync, get_data_async, create_tables, insert_data

if __name__ == "__main__":
    # get_data_sync()
    #
    # # Only preform check if your code will run on non-windows environments.
    # if sys.platform == 'win32':
    #     # Set the policy to prevent "Event loop is closed" error on Windows
    #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # asyncio.run(get_data_async())

    create_tables()
    insert_data()
