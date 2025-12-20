import sys
sys.path.append("..")

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

        self.registers = {
            '0000': 'al',
            '0001': 'cl',
            '0010': 'dl',
            '0011': 'bl',
            '0100': 'ah',
            '0101': 'ch',
            '0110': 'dh',
            '0111': 'bh',
            '1000': 'ax',
            '1001': 'cx',
            '1010': 'dx',
            '1011': 'bx',
            '1100': 'sp',
            '1101': 'bp',
            '1110': 'si',
            '1111': 'di',
        }

    def read_asm(self):
        self.file = open(self.path, 'rb')
        raw_bytes_data = self.file.read()
        for byte in raw_bytes_data:
            self.ops.append(''.join(f'{byte:08b}'))
    
        # build the ops
        i = 0
        while i < len(self.ops) - 1:
            self.ops[i] = self.ops[i] + self.ops[i+1]
            self.ops.pop(i+1)
            i += 1
        
    def decode_op(self, op):    
        self.op = self.opcodes[int(op[:6], 2)]
        self.d = int(op[6], 2)
        self.w = int(op[7], 2)
        self.mod = int(op[8:10], 2)
        self.reg = int(op[10:13], 2)
        self.rm = int(op[13:16], 2)

        # lookup and print out decoded operations in asm
        return f"{self.op} {self.registers[f"{self.w:01b}{self.rm:03b}"]}, {self.registers[f"{self.w:01b}{self.reg:03b}"]}"

if __name__ == "__main__":
    decoder = Decoder_8086(sys.argv[1])
    decoder.read_asm()
    output_file = open('output.asm', 'w')
    for op in decoder.ops:
        output_file.write(decoder.decode_op(op) + "\n")
