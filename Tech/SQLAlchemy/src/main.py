import asyncio
import os.path
import sys

from queries.core import SyncCore

sys.path.insert(1, os.path.join(sys.path[0], ".."))

from queries.orm import SyncORM, insert_data_async

if __name__ == "__main__":
    if sys.platform == 'win32':
        # Set the policy to prevent "Event loop is closed" error on Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # get_data_sync()
    #
    # # Only preform check if your code will run on non-windows environments.
    # asyncio.run(get_data_async())

    SyncORM.create_tables()
    SyncORM.insert_workers()
    SyncORM.insert_resumes()
    SyncORM.insert_additional_resumes()
    # SyncORM.update_worker(1, "Rogozenko")
    SyncORM.select_workers()
    # SyncORM.select_resumes_avg_compensation("Python")
    # SyncORM.select_with_join_cte_subquery_window_func()
    # SyncORM.select_workers_with_lazy_relationship()
    # SyncORM.select_workers_with_joined_relationship()
    # SyncORM.select_workers_with_selectin_relationship()
    # SyncORM.select_workers_with_condition_relationship()
    # SyncORM.select_workers_with_condition_relationship_contains_eager()
    # SyncORM.select_workers_with_condition_relationship_contains_eager_with_limit()

    SyncORM.insert_vacancies_and_replies()
    SyncORM.select_resumes_with_all_relationships()


    # SyncCore.create_tables()
    # SyncCore.select_workers()
    # SyncCore.update_worker(1, "Rogozenko")
    # SyncCore.select_workers()

