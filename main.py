import sys
import wave
import numpy as np
import datetime

from WaveDefine import *

def CreateWaveStereo( leftHz : float, rightHz : float, waveRange : int, filename : str , time : int = 10):
    '''ステレオなWaveファイルを作成する'''
    pi = np.pi
    s  = time         #10秒の長さのwaveファイルを作る
    N  = WaveDefine.WaveData.Framerate * s     #フレーム数（左右で1フレーム）
    t = np.arange(0, s, 1 / WaveDefine.WaveData.Framerate)   #横軸

    #sin(2π*□＊t) の周波数は□の部分。16ビットで録音するので、
    #－32768～32767がデータの範囲。だから－15000～15000の範囲の
    #大きさの音を作ることにした。
    leftData = waveRange * np.sin(2*pi*leftHz*t)
    rightData = waveRange * np.sin(2*pi*rightHz*t)
    soundData = np.zeros(N * 2, dtype= "int16") #左右のデータ分が必要
    soundData[0::2] = leftData # 0番目から2要素ずつ代入
    soundData[1::2] = rightData # 1番目から2要素ずつ代入

    writewave = wave.Wave_write(filename) #保存先ファイル
    #setparamの引数は
    #(nchannels, sampwidth, framerate, nframes, comptype, compname)
    #先頭から順にステレオ、サンプルのサイズ2バイト、
    #サンプリング周波数framerate、フレーム数N。
    writewave.setparams((WaveDefine.Channel.Stereo, WaveDefine.SamplingWidth.Bit16, WaveDefine.WaveData.Framerate, N, 'NONE', 'NONE'))
    writewave.writeframes(soundData) #編集したサウンドデータを保存
    writewave.close()

dt = datetime.datetime.now()
print('▼▼▼▼ {}:{}:{}'.format(dt.hour, dt.minute, dt.second))

# L:ラ R:ド　の音声ファイルを作成
# #Hzは振幅の回数　100Hzの場合0~10000~0~-10000~0　という変化を1秒間に100回繰り返す
CreateWaveStereo(WaveDefine.MusicalScale.Ra, WaveDefine.MusicalScale.So, 10000, "sample.wav")

dt = datetime.datetime.now()
print('▲▲▲▲ {}:{}:{}'.format(dt.hour, dt.minute, dt.second))
sys.exit()