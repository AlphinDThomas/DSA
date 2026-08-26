class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def solve(s,open,closed):
            if len(s) == 2*n:
                res.append(s)
                return
            
            if open<n:
                solve(s+"(",open+1,closed)
            
            if closed<open:
                solve(s+")",open,closed+1)
        solve("",0,0)
        return res