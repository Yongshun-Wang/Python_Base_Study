def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我醒了")
    return inner

@outer
def sleep():
    import time
    import random
    print("睡眠中...")
    time.sleep(random.randint(1,5))

sleep()