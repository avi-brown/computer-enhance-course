import sys
sys.path.append("..")
from print_utils import pretty_print

class Decoder_8086:
    def __init__(self, path):
        self.path = path
        self.current_op = None
        self.opcodes = {
            100010: 'mov',
        }

        @pretty_print
        def decode(self):    
            FILE = open(self.path, 'rb')
            raw_bytes_data = FILE.read()
            bin_data = ''.join(f'{byte:08b}' for byte in raw_bytes_data)
            print("READ FILE")
            print("GOT BINARY DATA: ", bin_data)

            self.current_op = self.opcodes[bin_data[:6]]
            print(self.current_op)

if __name__ == "__main__":
    decode(sys.argv[1])
