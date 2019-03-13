from VirtualMachine.Operations import VM


inst = VM([],0, "dreg")
print(inst.push())
print(inst.push())
print(inst.push())
print(inst.pop())