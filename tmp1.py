# def hello(count):
#     if count == 0:    # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
#         return
#     else:
#         print('Hello, world!', count)
    
#         count -= 1      # count를 1 감소시킨 뒤
#         hello(count)    # 다시 hello에 넣음
 
# hello(50)    # hello 함수 호출


def main():
    num = int(input("자연수를 입력해 주세요.\n"))
    fact = factorial(num)
    print("자연수",num,"의 계승은",fact)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

main()