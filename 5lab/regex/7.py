import re

def camelCase(snake):
    parts = snake.split('_')
    
    return parts[0] + ''.join(i.title() for i in parts[1:])

snake = input()

print(camelCase((snake)))