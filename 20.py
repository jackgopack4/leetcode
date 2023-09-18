class Solution:
    def isValid(self, s_string: str) -> bool:
        char_stack = []
        char_set = set(['(',')','{','}','[',']'])
        for s in s_string:
            if s in char_set:
                if s == '(':
                    char_stack.append(s)
                elif s == ')':
                    if not char_stack or char_stack.pop() != '(':
                        return False
                elif s == '{':
                    char_stack.append(s)
                elif s == '}':
                    if not char_stack or char_stack.pop() != '{':
                        return False
                elif s == '[':
                    char_stack.append(s)
                elif s == ']':
                    if not char_stack or char_stack.pop() != '[':
                        return False
        return not char_stack
