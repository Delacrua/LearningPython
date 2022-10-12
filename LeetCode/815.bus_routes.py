"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels
in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target.
You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
"""

from collections import defaultdict, deque  # Not needed on LeetCode


class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0
        stop_dict = defaultdict(set)
        for bus_number, stops in enumerate(routes):
            for stop in stops:
                stop_dict[stop].add(bus_number)

        queue = deque([(source, 0)])
        used_stops, used_buses = set(), set()

        while queue:
            current_stop, bus_count = queue.popleft()
            if current_stop == target:
                return bus_count

            for bus_number in stop_dict[current_stop]:
                if bus_number not in used_buses:
                    used_buses.add(bus_number)
                    for stop in routes[bus_number]:
                        if stop not in used_stops:
                            used_stops.add(stop)
                            queue.append((stop, bus_count + 1))

        return -1
