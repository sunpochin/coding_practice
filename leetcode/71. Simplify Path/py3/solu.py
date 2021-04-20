class Solution:
    def simplifyPath(self, path: str) -> str:
        parsed = path.split("/")
        # print('parsed: ', parsed)
        stack = []
        for it in parsed:
            if '' == it:
                continue
            if '.' == it:
                continue
            
            if '..' == it:
                if len(stack) > 0:
                    stack.pop(len(stack) - 1)
                elif len(stack) is 0:
                    continue
            else:
                stack.append(it)
                
        # print('stack: ', stack)
        res = ''
        for it in stack:
            res = res + '/' + it
        if '' == res:
            res = '/'
            
        # print('res: ', res)
        return res
