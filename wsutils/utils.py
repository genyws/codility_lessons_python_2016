import random
class InputType:
    @staticmethod
    def getRandomIntegerWithRange(start,end):
        ret = random.randint(start, end+1)
        print("%d generated.." % ret)
        return  ret


