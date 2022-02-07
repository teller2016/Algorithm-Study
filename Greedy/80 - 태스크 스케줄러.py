# https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_cnt = 0
            for task, _ in counter.most_common(n + 1):
                sub_cnt += 1
                result += 1

                counter.subtract(task)
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_cnt + 1

        return result