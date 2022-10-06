"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete
either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter
in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
"""


# Direct counting of length
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # tasks = ["A","A","A","B","B","B"]
        # n = 2
        counts = list(collections.Counter(tasks).values())  # [3,3]
        max_count = max(counts)  # 3
        num_of_chars_with_max_count = counts.count(max_count)  # 2, A and B
        num_of_chunks_with_idles = max_count - 1  # 2  -> A  A  A
        # either a task will fill an empty place or the place stays idle,
        # either way the chunk size stays the same
        length_of_a_chunk_with_idle = n + 1  # 3 -> A _ _ A _ _ A
        # on the final chunk, there will only be most frequent letters
        length_of_the_final_chunk = num_of_chars_with_max_count  # 2
        length_of_all_chunks = (num_of_chunks_with_idles * length_of_a_chunk_with_idle) + length_of_the_final_chunk
        # 2*3 + 2 = 8
        # -> A B _ A B _ A B
        return max(len(tasks), length_of_all_chunks)
