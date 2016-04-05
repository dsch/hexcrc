def crc16(data, start_value=None):
    # CCITT CRC16
    polynomial = 0x1021
    inital_value = 0xFFFF

    crc = inital_value
    for v in data:
        crc = crc_update(crc, ord(v))
    return crc


def crc_update(crc, data):
    crc ^= (data << 8)
    for i in range(8):
        if crc & 0x8000:
            crc = (crc << 1) ^ 0x1021
        else:
            crc <<= 1

    return crc & 0xFFFF;
