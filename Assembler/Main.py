from Assembler.symbol_table import symbol_table
from Assembler.Parser import Parser
from Assembler.Code import Code

class Main:
    fileName = "mult.asm"
    file = open(fileName)
    readlines = file.readlines()

    outFileName = fileName.replace("asm", "hack")
    hackFile = open(outFileName, 'w+')

    Code = Code()

    rom_address = 0
    ram_address = 16

    # First Pass
    for i in readlines:
        firstPass = Parser(i)
        type = firstPass.commandType()
        symbol = firstPass.symbol(type)

        if type == "A_COMMAND" or type == "C_COMMAND": rom_address+=1
        elif type =="L_COMMAND": symbol_table[symbol] = rom_address

    # Second Pass
    for i in readlines:
        machine_command = ''
        secondPass = Parser(i)
        type = secondPass.commandType()
        symbol = secondPass.symbol(type)

        if symbol:
            if (type == "A_COMMAND"):
                if symbol[0].isdigit():
                     binary = symbol
                else:
                    if symbol in symbol_table:
                        binary = symbol_table[symbol]
                    else:
                        binary = ram_address
                        symbol_table[symbol] = ram_address
                        ram_address += 1

                machine_command = '{0:016b}\n'.format(int(binary)).strip()
                print(machine_command)
                hackFile.write(machine_command+"\n")


        elif (type=="C_COMMAND"):
            cmd = secondPass.cmd
            dest = secondPass.dest()
            comp1 = secondPass.comp()
            jmp = secondPass.jmp()
            dest = Code.dest(dest)
            comp = Code.comp(comp1)
            jmp = Code.jmp(cmd[len(cmd)-3:len(cmd)])

            machine_command = '111{0}{1}{2}\n'.format(comp, dest, jmp).strip()
            print(machine_command)
            hackFile.write(machine_command+"\n")

    file.close()
    hackFile.close()



main = Main()
