

class VM:

    def __init__(self, stack, sp, dReg):
        self.stack = stack
        self.sp = sp
        self.dReg = dReg

    def push(self):
        self.stack.append(self.dReg)
        self.sp +=1

        return self.sp, self.stack

    def pop(self):
        self.stack.pop()
        self.sp -=1
        return self.sp, self.stack
