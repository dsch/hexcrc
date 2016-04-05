import pytest

from hexcrc.crc import crc16
from hexcrc.hex import parse_line


def test_dummy():
    with open('/home/david/PycharmProjects/hexcrc/test/test.hex') as f:
        line = f.readline()
        parse_line(line)


def test_parse_line_with_data():
    data = parse_line(':10010000214601360121470136007EFE09D2190140')
    assert data == [0x21, 0x46, 0x01, 0x36, 0x01, 0x21, 0x47, 0x01, 0x36, 0x00, 0x7E, 0xFE, 0x09, 0xD2, 0x19, 0x01]


def test_parse_line_no_data():
    data = parse_line(':10010001214601360121470136007EFE09D2190140')
    assert data is None


def test_parse_line_invalid_start():
    with pytest.raises(Exception):
        parse_line('_')


def test_crc_check():
    assert crc16('123456789') == 0x291B


