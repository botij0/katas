from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dirs = self.build_directions_dict(tickets)
        stack = ["JFK"]
        new_itinerary = []
        print(dirs)

        while stack:
            print(stack, new_itinerary)
            if stack[-1] in dirs.keys() and dirs[stack[-1]]:
                stack.append(dirs[stack[-1]].pop(0))
            else:
                new_itinerary.insert(0, stack.pop())

        return new_itinerary

    def build_directions_dict(self, tickets: List[List[str]]) -> dict:
        directions = {}
        for t in tickets:
            if t[0] in directions.keys():
                directions[t[0]].append(t[1])
                directions[t[0]].sort()
            else:
                directions[t[0]] = [t[1]]

        return directions


if __name__ == "__main__":
    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    print(Solution().findItinerary(tickets))  # ["JFK","AAA","JFK","CCC","JFK","BBB"]
