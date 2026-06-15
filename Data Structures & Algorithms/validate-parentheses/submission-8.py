class Solution:
    def stackChange(self, stack, i):
        if stack and stack[-1] == i:
            stack.pop()
            return True
        return False

    def isValid(self, s: str) -> bool:
        #if len(s) % 2 == 1:
        #    return False

        stack = []
        for c in s:
            if c == '}':
                i = '{'
                if not self.stackChange(stack,i):
                    return False
            elif c == ')':
                i = '('
                if not self.stackChange(stack,i):
                    return False
            elif c == ']':
                i = '['
                if not self.stackChange(stack,i):
                    return False
        
            #if stack and stack[-1] == i:
            #    stack.pop()
            #else:
            #    return False

            if (c == '(' or c == '{' or c == '['):
               stack.append(c)
        return len(stack) == 0



        #pl = 0
        #pr = 1
        #   
        #while pl < pr and pr < len(s):
        #    countPairs = 0
        #    while pr < len(s) and s[pr] in "({[":                
        #        pr+= 1 # go towards closed bracket
        #        countPairs+= 1 
        #        if pr < len(s) and s[pr] in ")}]":
        #            pr += countPairs
        #            break
                #if s[pr] in ")}]":
                #    pr += countPairs #now outside of pairs

            # check if brackets match
        #    for i in range(countPairs):
         #       if ((s[pl] == '{' and s[pr] != '}') or (s[pl] == '(' and s[pr] != ')') or (s[pl] == '[' and s[pr] != ']')):
        #            return False
        #        pl += 1
        #        pr -= 1
        #    pl += countPairs + 1
        #    pr += countPairs + 1
        #return True

