"""
Node(노드) 클래스의 구성
data : 값 저장
next : 다음 노드를 가르키는 링크를 저장
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 노드 A~D를 생성하고 A->D 순으로 링크 지정
def init_list():
    global node_A
    node_A = Node(3)
    node_B = Node(17)
    node_C = Node(31)
    node_D = Node(83)

    node_A.next = node_B
    node_B.next = node_C
    node_C.next = node_D


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

    # node_P -> new_node -> node_T
    node_P = node_A
    node_T = node_A

    # 순회하며 data 값에 맞는 자리 찾기
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next

    new_node.next = node_T
    node_P.next = new_node


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
            del next_node
            break
        pre_node = next_node
        next_node = pre_node.next


if __name__ == '__main__':
    # 연결 리스트 초기화 후 출력
    init_list()
    print_list()

    # 57 값의 노드 삽입 후 출력
    insert_node(57)
    print_list()

    # 31 값의 노드 삭제 후 출력
    delete_node(31)
    print_list()
