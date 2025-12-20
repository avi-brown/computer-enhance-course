import sys
sys.path.append("..")

class Decoder_8086:
    def __init__(self, path):
        self.path = path
        self.file = None
        self.bytes = []
        self.opcode = None
        self.d = None
        self.w = None
        self.mod = None
        self.reg = None
        self.rm = None

        self.opcodes = {
            0b100010: 'mov',    # register memory to/from register
            0b1011:   'mov',    # immediate to register
        }

        # this is w + reg encoding 
        # (see table on p161 of manual)
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

    def pop_bytes(self, n):
        for _ in range(n):
            self.bytes.pop(0)

    def read_bin(self):
        self.file = open(self.path, 'rb')
        raw_bytes_data = self.file.read()
        for byte in raw_bytes_data:
            self.bytes.append(''.join(f'{byte:08b}'))

    def parse_bytes(self):
        while len(self.bytes):
            for byte in self.bytes:

                # immediate to register
                if byte.startswith('1011'):
                    if byte[4] == '1':
                        self.decode_imm_to_reg_w(self.bytes[0], self.bytes[1], self.bytes[2])
                        self.pop_bytes(3)
                    else:
                        self.decode_imm_to_reg(self.bytes[0], self.bytes[1])
                        self.pop_bytes(2)

                # register memory to/from register
                elif byte.startswith('100010'):
                    mod = self.bytes[1][:2]
                    rw = self.bytes[1][5:8]

                    # check mod
                    if mod == "00": # no disp 
                        if rw == "110": # special case - see table * on p162
                            self.decode_reg_mem_to_from_reg_16b_disp(self.bytes[0], self.bytes[1], self.bytes[2], self.bytes[3])
                            self.pop_bytes(4)
                        else:
                            self.decode_reg_mem_to_from_reg(self.bytes[0], self.bytes[1])
                            self.pop_bytes(2)

                    elif mod == "01": # 8 bit disp
                            self.decode_reg_mem_to_from_reg_8b_disp(self.bytes[0], self.bytes[1], self.bytes[2])
                            self.pop_bytes(3)

                    elif mod == "10": # 16 bit disp
                            self.decode_reg_mem_to_from_reg_16b_disp(self.bytes[0], self.bytes[1], self.bytes[2], self.bytes[3])
                            self.pop_bytes(4)

                    elif mod == "11": # no disp
                        self.decode_reg_mem_to_from_reg(self.bytes[0], self.bytes[1])
                        self.pop_bytes(2)

    def decode_imm_to_reg(self, b1, b2):
        print("decode_imm_to_reg:\t\t\t", b1, b2)

    def decode_imm_to_reg_w(self, b1, b2, b3):
        print("decode_imm_to_reg_w:\t\t\t", b1, b2, b3)

    def decode_reg_mem_to_from_reg(self, b1, b2):
        print("decode_reg_mem_to_from_reg:\t\t", b1, b2)

    def decode_reg_mem_to_from_reg_8b_disp(self, b1, b2, b3):
        print("decode_reg_mem_to_from_reg_8b_disp:\t", b1, b2, b3)

    def decode_reg_mem_to_from_reg_16b_disp(self, b1, b2, b3, b4):
        print("decode_reg_mem_to_from_reg_16b_disp:\t", b1, b2, b3, b4)

    def decode_op(self, op):   
        pass 
        # self.op = self.opcodes[int(op[:6], 2)]
        # self.d = int(op[6], 2)
        # self.w = int(op[7], 2)
        # self.mod = int(op[8:10], 2)
        # self.reg = int(op[10:13], 2)
        # self.rm = int(op[13:16], 2)

        # # lookup and print out decoded operations in asm
        # return f"{self.op} {self.registers[f"{self.w:01b}{self.rm:03b}"]}, {self.registers[f"{self.w:01b}{self.reg:03b}"]}"

if __name__ == "__main__":
    output_file = open('output.asm', 'w')
    decoder = Decoder_8086(sys.argv[1])
    decoder.read_bin()
    decoder.parse_bytes()
    for byte in decoder.bytes:
        output_file.write(decoder.decode_op(byte) + "\n")
