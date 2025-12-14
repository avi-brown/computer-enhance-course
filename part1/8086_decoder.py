import sys
sys.path.append("..")
from print_utils import pretty_print

@pretty_print
def decode(path):    
    FILE = open(path, 'rb')
    raw_bytes_data = FILE.read()
    bin_data = ''.join(f'{byte:08b}' for byte in raw_bytes_data)
    print("READ FILE")
    print("GOT BINARY DATA: ", bin_data)

if __name__ == "__main__":
    decode(sys.argv[1])
