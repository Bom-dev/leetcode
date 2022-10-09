class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        hours = []
        hours.append(logs[0][1])
        for i in range(len(logs) - 1):
            hour = logs[i + 1][1] - logs[i][1]
            hours.append(hour)
        max_hour = max(hours)
        max_index = hours.index(max_hour)
        if hours.count(max_hour) > 1:
            indexes = []
            ids = []
            indexes.append(max_index)
            hours.remove(max_hour)
            for i in range(hours.count(max_hour)):
                new_max_index = hours.index(max_hour) + 1 + i
                indexes.append(new_max_index)
                hours.remove(max_hour)
            for x in range(len(indexes)):
                ids.append(logs[indexes[x]][0])
            return min(ids)
        else:
            return logs[max_index][0]