from queue import Queue

"""
파이썬 Queue를 이용 
"""


# 큐를 전부 인출하며 출력
def print_que(que):
    while not que.empty():
        print(f"data : {que.get()}")


if __name__ == '__main__':
    # 큐 생성
    que = Queue()

    # 차례로 값 집어넣기
    que.put("고양이")
    que.put(134)
    que.put(["강아지", 6, 1.52])
    que.put("토끼")
    print_que(que)
