class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        def cs(i,cur,total):
            if total==target:
                result.append(cur.copy())
                return
            if total>target or i>= len(candidates):
                return
            
            cur.append(candidates[i])
            cs(i,cur,total+candidates[i])
            cur.pop()
            cs(i+1,cur,total)

        cs(0,[],0)
        return result
