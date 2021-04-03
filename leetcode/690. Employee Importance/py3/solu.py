"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# Algo: Use dfs to traverse every subordiantes of employee of id, 
# to sum up total importance value.
#
# Time Complexity: O(N), where N is the number of employees. We might query each employee in dfs.
# Space Complexity: O(N), the size of the implicit call stack when evaluating dfs.

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hmap = {}
        def dfs(emp: Employee)-> int:
            # print('emp sub: ', emp.subordinates)
            sub = emp.subordinates
            val = emp.importance
            for sid in sub:
                # print('sid: ', sid, ', hmap.get(sid): ', hmap.get(sid))
                val += dfs(hmap.get(sid) )
            return val

        ret = 0
#         print('loyees: ', employees)
        for ix in employees:
            hmap[ix.id] = ix

        ix = hmap.get(id)
        ret = dfs(ix)
        return ret

