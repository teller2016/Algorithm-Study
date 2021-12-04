#https://leetcode.com/problems/most-common-word/submissions/
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pList = re.sub('[^\w]',' ',paragraph.lower()).split()
        pList = [word for word in pList if word not in banned]
        return collections.Counter(pList).most_common(1)[0][0]