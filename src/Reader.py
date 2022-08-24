from struct import calcsize, unpack
from .AnimSKB import AnimSKB
from .AnimSKBHeader import AnimSKBHeader
from .AnimSKBKey import AnimSKBKey


class Reader:
    HEADER_FORMAT = '2I2HI3f'
    KEY_FORMAT = 'H7h'

    def __init__(self, filepath):
        self.filepath = filepath
        self.byte_order = self.__get_byte_order()

    def __get_byte_order(self) -> str:
        with open(self.filepath, 'rb') as reader:
            magic = unpack('>I', reader.read(4))[0]
            if magic == 0x534B4231:
                # magic = SKB1: use Little Endian
                return '<'
            elif magic == 0x31424B53:
                # magic = 1BKS: use Big Endian
                return '>'
            else:
                raise Exception('Invalid ANIM File.')

    def __get_header_format(self) -> str:
        return self.byte_order + self.HEADER_FORMAT

    def __get_full_format(self, header: AnimSKBHeader) -> str:
        return self.__get_header_format() + str(self.KEY_FORMAT * header.keyCount) + str(header.timeCount) + 'f' + str((header.timeCount-1)*header.boneCount) + 'H'

    def read(self) -> AnimSKB:
        header = None

        # Read Header
        with open(self.filepath, 'rb') as reader:
            data = unpack(self.__get_header_format(), reader.read(
                calcsize(self.__get_header_format())))
            header = AnimSKBHeader(
                data[0], data[1], data[2], data[3], data[4], data[5:8])

        # Create Format String to read the whole file
        full_format = self.__get_full_format(header)

        # Read whole file
        with open(self.filepath, 'rb') as reader:
            data = unpack(full_format, reader.read(calcsize(full_format)))
            data = list(data)

            keys = []
            times = []
            offsets = []

            data = data[8:]

            for i in range(header.keyCount):
                keys.append(AnimSKBKey(data.pop(0), [data.pop(0), data.pop(0), data.pop(0), data.pop(0)], [
                            data.pop(0), data.pop(0), data.pop(0)], header.scale))

            for i in range(header.timeCount):
                times.append(data.pop(0))

            for i in range(header.timeCount - 1):
                row = []
                for j in range(header.boneCount):
                    row.append(data.pop(0))
                offsets.append(row)

            return AnimSKB(header, keys, times, offsets)
