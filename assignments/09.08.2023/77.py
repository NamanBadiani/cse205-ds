class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # result=[]
        # def comb(start,temp):
        #     if len(temp)==k:
        #         result.append(temp.copy())
        #         return
        #     for i in range (start,n+1):
        #         temp.append(i)
        #         comb(i+1,temp)
        #         temp.pop()
        # comb(1,[])
        # return result


        result=[]
        def comb(start,temp):
            if len(temp)==k:
                result.append(temp.copy())
                return
            for i in range (start,n+1):
                temp.append(i)
                comb(i+1,temp)
                temp.pop()
        comb(1,[])
        return result