import sys
sys.path.append("..")
from print_utils import pretty_print, print_bin

class Decoder_8086:
    def __init__(self, path):
        self.path = path
        self.file = None
        self.ops = []
        self.op = None
        self.d = None
        self.w = None
        self.mod = None
        self.reg = None
        self.rm = None

        self.opcodes = {
            0b100010: 'mov',
        }

    def read_file(self):
        self.file = open(self.path, 'rb')
        raw_bytes_data = self.file.read()
        for byte in raw_bytes_data:
            self.ops.append(''.join(f'{byte:08b}'))
        for i in range(0, len(self.ops) - 1, 2):
            self.ops[i] = self.ops[i] + self.ops[i+1]
        for i in range(1, 6, 2):
            self.ops.pop(i)
        print(self.ops)
        
    @pretty_print
    def decode_op(self, op):    
        print(op)
        self.op = self.opcodes[int(op[:6], 2)]
        self.d = int(op[6], 2)
        self.w = int(op[7], 2)
        self.mod = int(op[8:10], 2)
        self.reg = int(op[10:13], 2)
        self.rm = int(op[13:16], 2)

        print(self.op)
        print_bin(self.d)
        print_bin(self.w)
        print_bin(self.mod)
        print_bin(self.reg) 
        print_bin(self.rm)

    @pretty_print
    def print_current_op(self):
        print("CURRENT OP: ", self.op)
hi
if __name__ == "__main__":
    decoder = Decoder_8086(sys.argv[1])
    decoder.read_file()
    for op in decoder.ops:
        decoder.decode_op(op)