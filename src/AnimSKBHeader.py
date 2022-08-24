class AnimSKBHeader:
    '''
    uint32 Magic
    uint32 Flags
    uint16 BoneCount
    uint16 TimeCount
    uint32 KeyCount
    float32 Scale[3]
    '''

    def __init__(self, magic, flags, boneCount, timeCount, keyCount, scale):
        self.magic = magic
        self.flags = flags
        self.boneCount = boneCount
        self.timeCount = timeCount
        self.keyCount = keyCount
        self.scale: list[float] = scale
