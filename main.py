
from src.move9 import Move9


def testFun():
    list = [9,3,4,9,9,3,2,1]
    move9_obj = Move9()
    print('Before moving 9')
    print(list)
    print('After moving 9')
    print(move9_obj.move_9_to_end(list))





if __name__ == '__main__':
    testFun()