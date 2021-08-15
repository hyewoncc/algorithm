from collections import deque

"""
파이썬 deque를 이용
"""

if __name__ == '__main__':
    # deque로 que 생성
    que = deque()

    # 값 차례로 집어넣기
    que.append("도마뱀")
    que.append(4.1)
    que.append([10, "물고기"])
    que.append("오리")
    print(f"현재 큐 : {que}")

    # 처음 들어간 값 부터 인출하기
    print(f"값 인출 : {que.popleft()}")
    print(f"값 인출 : {que.popleft()}")
    print(f"현재 큐 : {que}")
