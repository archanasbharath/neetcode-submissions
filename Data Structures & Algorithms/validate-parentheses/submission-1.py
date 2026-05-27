class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        '''
        while '()' in s or '{}' in s or '[]' in s:
            print(s,'()' in s,'{}' in s,'[]' in s)
            s = s.replace('()','')
            s = s.replace('{}','')
            s = s.replace('[]','')
        return s == ''
        '''
        stack = []
        for ch in s:
            if ch in par_dict:
                if stack and stack[-1] == par_dict[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False



        