# def outer(msg):
#     def inner(logo):
#         print(f"{logo} {msg}")
#     return inner

# fn = outer("hello")
# fn("python")


# def outer2(num1):
#     def inner2(num2):
#         nonlocal num1
#         num1+=num2
#         print(num1)
#     return inner2
# f1 = outer2(10)
# f1(10)
# f1(10)
# f1(10)

# 实现atm小案例
def account_create(initial_amount=0):
    def atm(num,deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount+=num
            print(f"存款{num}元，账户余额为：{initial_amount}")
        else:
            initial_amount-=num
            print(f"取款{num}元，账户余额为：{initial_amount}")
    return atm

atm = account_create(1000)
atm(500)
atm(200,False)
atm(300)

