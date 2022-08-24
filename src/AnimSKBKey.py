class AnimSKBKey:
    '''
    uint16 TimeIndex
    int16 Quat[4]
    int16 Tran[3]
    '''

    def __init__(self, timeIndex, quat, tran, scale=[1.0, 1.0, 1.0]):
        self.timeIndex = timeIndex
        self.quat = quat
        self.tran = tran
        self.scale = scale
        self.__normalize_quats()
        self.__scale_translations()

    def __normalize_quats(self):
        self.quat[0] = self.quat[0] / 32767.0
        self.quat[1] = self.quat[1] / 32767.0
        self.quat[2] = self.quat[2] / 32767.0
        self.quat[3] = self.quat[3] / 32767.0
        # Blender uses W,X,Y,Z instead of X,Y,Z,W
        qautReordered = [self.quat[3], self.quat[0],
                         self.quat[1], self.quat[2]]
        self.quat = qautReordered

    def __scale_translations(self):
        self.tran[0] *= self.scale[0]
        self.tran[1] *= self.scale[1]
        self.tran[2] *= self.scale[2]
        # This fixes incorrect bone translations (still don't know why, must be a Blender thing)
        self.tran = [self.tran[0], -self.tran[2], self.tran[1]]
