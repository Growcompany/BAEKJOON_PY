input_list = list(input())
stack = []
result = ''
math = ['+','-','*','/','(',')']

for char in input_list:
    if char in math:
        if char == '(':
            stack.append(char)
        if char == '*' or char == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                result += stack.pop()
            stack.append(char)
        if char == '+' or char == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(char)
        if char == ')':
            while stack and stack[-1] != '(':
                result +=stack.pop()
            stack.pop()
    else:
        result +=char
        
while stack:
    result += stack.pop()
print(result)