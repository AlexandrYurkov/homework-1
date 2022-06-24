def int32_to_ip(int32):
    one_byte = int(int32 / 16777216) % 256
    two_byte = int(int32 / 65536) % 256
    three_byte = int(int32 / 256) % 256
    four_byte = int(int32) % 256
    return '%(one_byte)s.%(two_byte)s.%(three_byte)s.%(four_byte)s' % locals()
