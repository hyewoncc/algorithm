"""
연결 리스트를 이용한 스택 클래스
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    # 스택의 끝을 가리킬 head 생성
    def __init__(self):
        self.head = None

    # 리스트 끝에 값 추가하는 push
    def push(self, data):
        # 새로운 노드 생성 후, head를 이용해 링크 지정
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 리스트 끝의 값을 가져오는 pop
    def pop(self):
        if not self.is_empty():
            item = self.head
            self.head = self.head.next
            return item.data

    # 리스트가 비었는지 확인하는 isEmpty
    def is_empty(self):
        return self.head is None

    # 리스트 끝의 값을 확인하는 peek
    def peek(self):
        if not self.is_empty():
            return self.head.data

    # 스택 값 확인을 위한 문자열 생성
    def __str__(self):
        index = self.head
        string = ""
        while index is not None:
            string += index.data + " "
            index = index.next
        return string


if __name__ == '__main__':
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
