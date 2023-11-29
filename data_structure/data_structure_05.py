'''
    stack
'''

class Stack(object):
    #   defination initialize function
    def __init__(self):
        #   initialize empty list
        self.__list = []


    #   push stack
    def push(self,item):
        self.__list.append(item)
        self.__list.insert(0,item)

    #   pop elements
    def pop(self):
        self.__list.pop()

    #   back the top of stack
    def peek(self):
        return self.__list[len(self.__list)-1]

    #   empty or not
    def is_empty(self):
        return self.__list == []

    #   calculate the size of stack
    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    stack = Stack()
    print('--------------------is_empty---------------------------')
    print(stack.is_empty())
    print('--------------------push---------------------------')
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print('--------------------is_empty---------------------------')
    print(stack.is_empty())
    print('--------------------pop---------------------------')
    pop1 = stack.pop()
    print(pop1)
    print('--------------------size---------------------------')
    print(stack.size())


    print('-----------------------------------------------')

