"""
Node(노드) 클래스의 구성
data : 값 저장
next : 다음 노드를 가르키는 링크를 저장
prev : 이전 노드를 가르키는 링크를 저장
"""


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


# 노드 A~D를 생성하고 A->D 순으로 링크 지정
def init_list():
    global node_A
    node_A = Node(7)
    node_B = Node(23)
    node_C = Node(59)
    node_D = Node(91)

    node_A.next = node_B
    node_B.next = node_C
    node_B.prev = node_A
    node_C.next = node_D
    node_C.prev = node_B
    node_D.prev = node_C


# 노드 A를 시작으로 순회하며 출력
def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print


# 새로운 data 값 노드 삽입
def insert_node(data):
    global node_A

    # data 값의 새로운 노드
    new_node = Node(data)

    # node_P <-> new_node <-> node_T
    node_P = node_A
    node_T = node_A

    # 순회하며 data 값에 맞는 자리 찾기
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next

    # node_P와 node_T의 링크를 new_node에 연결
    # new_node의 양방향 링크를 node_P와 node_T에 연결
    node_P.next = new_node
    new_node.prev = node_P
    new_node.next = node_T
    node_T.prev = new_node


# 특정 노드 삭제
def delete_node(del_data):
    global node_A

    # 순회 노드인 pre_node와 그 다음 노드인 next_node 지정
    pre_node = node_A
    next_node = pre_node.next

    # 첫 노드가 삭제 대상 노드라면 삭제하고 next_node를 첫 노드로 지정
    if pre_node.data == del_data:
        del pre_node
        node_A = next_node
        return

    # 다음 노드가 삭제 대상 노드라면
    # 앞선 노드의 링크를 그 다음 노드에 걸고 해당 노드 삭제
    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            next_node.next.prev = next_node.prev
            del next_node
            break
        pre_node = next_node
        next_node = pre_node.next


if __name__ == '__main__':
    # 연결 리스트 초기화 후 출력
    init_list()
    print_list()

    # 57 값의 노드 삽입 후 출력
    insert_node(37)
    print_list()

    # 23 값의 노드 삭제 후 출력
    delete_node(23)
    print_list()
