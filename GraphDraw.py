import numpy as np
import matplotlib.pyplot as plt

class GraphDraw:
    '''
    _summary_ Matplotlib を使用したグラフ描画クラス

    _extended_summary_
        Matplotlib はPythonのグラフ描画のためのライブラリ
        グラフの描画やデータの可視化が簡単に行える
        折れ線グラフ、ヒストグラムや散布図など表現可能
    '''
    def __init__(self) -> None:
        pass

    def Draw(self):
        '''グラフの描画'''
        #0 <= t < 1 を0.2間隔で
        t = np.arange(0, 1, 0.2)
        y = t * t
        plt.plot(y)
        plt.show()
