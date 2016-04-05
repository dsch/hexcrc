def parse_line(line):
    if line[0] != ':':
        raise Exception('invalid format')
    length = int(line[1:3], 16) * 2
    cs_data = [int(line[i:i + 2], 16) for i in range(1, 8, 2)]

    if line[7:9] != '00':
        return
    data = [int(line[i:i + 2], 16) for i in range(9, length + 9, 2)]

    check = (~sum(cs_data + data) & 0xFF) + 1
    checksum = int(line[9 + length:11 + length], 16)

    if check != checksum:
        raise Exception('invalid checksum')

    return data