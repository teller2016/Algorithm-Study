#https://leetcode.com/problems/reorder-data-in-log-files/submissions/
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []

        for log in logs:
            log_li = log.split(' ')
            if log_li[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter + digit