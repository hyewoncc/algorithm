"""
리스트를 이용한 스택 클래스
"""


class Stack:
    # 스택으로 사용할 리스트 생성
    def __init__(self):
        self.items = []

    # 리스트 끝에 값 추가하는 push
    def push(self, item):
        self.items.append(item)

    # 리스트 끝의 값을 가져오는 pop
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # 리스트가 비었는지 확인하는 isEmpty
    def is_empty(self):
        return len(self.items) == 0

    # 리스트 끝의 값을 확인하는 peek
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # 스택 값 확인을 위한 문자열 생성
    def __str__(self):
        return str(self.items)


if __name__ == '__main__' :
    stack = Stack()
    print("스택에 빨강 ~ 초록 값 push")
    stack.push("빨강")
    stack.push("주황")
    stack.push("노랑")
    stack.push("초록")
    print(stack.__str__())

    print("스택에서 값 두 개 차례로 pop, 하나를 peek")
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())

    print("pop과 peek를 하고 난 스택의 상태")
    print(stack.__str__())
