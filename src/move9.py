## changes in master
class Move9(object):

    def __init__(self):
        pass

    '''
    move all numbers that are equal to 9 to the end of the list.
    Requirement: 1. no extra space used, i.e., in place operations; 2. all the non-9 numbers maintain the order
    Before moving 9
    [9, 3, 4, 9, 9, 3, 2, 1]
    After moving 9
    [3, 4, 3, 2, 1, 9, 9, 9]
    restrictions: all numbers are within the range [-2,147,483,648, 2,147,483,647], inclusive. Otherwise return None
    '''
    def move_9_to_end(self, list):
        pointer = 0
        iter = 0
        while iter < len(list):
            if list[iter] > pow(2,31) - 1 or list[iter] < -pow(2, 31):
                return None
            if list[iter] != 9:
                list[pointer] = list[iter]
                iter += 1
                pointer += 1
            else:
                iter += 1
        while pointer < len(list):
            list[pointer] = 9
            pointer += 1
        return list