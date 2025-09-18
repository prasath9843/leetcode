class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        for i in range(len(points)):
            l.append([[points[i][0]**2+points[i][1]**2],[points[i]]])
        l.sort()
        p=[]
        for i in range(k):
            p.append(l[i][1][0])
        return p