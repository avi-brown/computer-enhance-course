import sys
sys.path.append("..")
from print_utils import pretty_print, print_bin

class Decoder_8086:
    def __init__(self, path):
        self.path = path

        self.op = None
        self.d = None
        self.w = None
        self.mod = None
        self.reg = None
        self.rm = None

        self.opcodes = {
            0b100010: 'mov',
        }

    @pretty_print
    def decode_op(self):    
        FILE = open(self.path, 'rb')
        raw_bytes_data = FILE.read()
        bin_data = ''.join(f'{byte:08b}' for byte in raw_bytes_data)
        print("READ FILE")
        print("GOT BINARY DATA: ", bin_data)

        self.op = self.opcodes[int(bin_data[:6], 2)]
        self.d = int(bin_data[6], 2)
        self.w = int(bin_data[7], 2)
        self.mod = int(bin_data[8:10], 2)
        self.reg = int(bin_data[10:13], 2)
        self.rm = int(bin_data[13:16], 2)

        print(self.op)
        print_bin(self.d)
        print_bin(self.w)
        print_bin(self.mod)
        print_bin(self.reg)
        print_bin(self.rm)

    @pretty_print
    def print_current_op(self):
        print("CURRENT OP: ", self.op)

if __name__ == "__main__":
    decoder = Decoder_8086(sys.argv[1])
    decoder.decode_op()
    decoder.print_current_op()
