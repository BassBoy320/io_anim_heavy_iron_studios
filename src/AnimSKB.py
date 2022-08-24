from .AnimSKBHeader import AnimSKBHeader
from .AnimSKBKey import AnimSKBKey


class AnimSKB:
    '''
    iAnimSKBHeader header
    iAnimSKBKey keys[header.KeyCount]
    float times[header.TimeCount]
    unsigned short offsets[header.TimeCount - 1][header.BoneCount]
    '''

    def __init__(self, header: AnimSKBHeader, keys, times, offsets):
        self.header = header
        self.keys: list[AnimSKBKey] = keys
        self.times = times
        self.offsets = offsets
