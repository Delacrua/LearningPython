import asyncio
import os.path
import sys
sys.path.insert(1, os.path.join(sys.path[0], ".."))

from queries.orm import create_tables, insert_data, insert_data_async

if __name__ == "__main__":
    if sys.platform == 'win32':
        # Set the policy to prevent "Event loop is closed" error on Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # get_data_sync()
    #
    # # Only preform check if your code will run on non-windows environments.
    # asyncio.run(get_data_async())

    create_tables()
    insert_data()

    asyncio.run(insert_data_async())

