from enum import IntEnum

class WaveDefine:
    '''Waveファイル周りの定義等'''
    class Channel(IntEnum):
        Monaural = 1,
        Stereo = 2

    class SamplingWidth(IntEnum):
        Bit8 = 1,
        Bit16 = 2

    class WaveData:
        Framerate : int = 44100 #サンプリング周波数 1秒間に何回音の強さを測定するか

    class MusicalScale:
        '''音階'''
        Do : float = 261.63
        Re : float = 293.67
        Mi : float = 329.63
        Fa : float = 349.23
        So : float = 392.00
        Ra : float = 440.00
        Si : float = 493.88
        Do : float = 523.23
