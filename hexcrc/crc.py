_INITIAL_VALUE = 0xFFFF
_POLYNOMIAL = 0x1021


def crc16(data, start_value=None):
    # CCITT CRC16

    crc = start_value if start_value is not None else _INITIAL_VALUE
    for v in data:
        crc = crc_update(crc, v)
    return crc


def crc_update(crc, data):
    tmp = (data << 8) ^ (crc & 0xFF00)

    for i in range(8):
        if tmp & 0x8000:
            tmp <<= 1
            tmp ^= _POLYNOMIAL
        else:
            tmp <<= 1

    tmp &= 0xFFFF
    crc = ((crc & 0xFF) << 8) ^ tmp

    return crc
