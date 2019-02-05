# Solution without supporting ~

"""
class Solution(object):
    def simplifyPath(self, path):
        parts = path.split('/')
        stack = []
        for part in parts:
            if part:
                if part == '..' and stack:
                    stack.pop()
                elif part not in ['.', '..']:
                    stack.append(part)

        return '/' + '/'.join(stack)
"""

class Solution(object):
    def simplifyPath(self, path, home='/home/user'):
        parts = path.split('/')
        stack = []
        for part in parts:
            if part:
                if part == '..' and stack:
                    stack.pop()
                elif part == '~':
                    stack.append(home.lstrip('/'))
                elif part not in ['.', '..']:
                    stack.append(part)

        return '/' + '/'.join(stack)
