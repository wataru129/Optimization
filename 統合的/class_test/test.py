import numpy as np
import math

class RBFN:
    def settig_parameter(self): #パラメータ設定
        samp_hyoukati_max=max(samp_hyoukati)
        for h in range(samp_kazu):
            y_rbf(h,1)=samp_hyoukati(h,1)-samp_hyoukati_max
        H=zeros(samp_kazu,samp_kazu)                                   #H行列の初期化
    
    def caluculate_max_distance(self):#サンプル点間最大距離の計算
        d_max=0                                                        #サンプル点間の最大距離の初期化
        samp_kyori=0                                                   #サンプル点間の各距離の行列の初期化
        for j in range(samp_kazu-1):
            for j1 in range(j+1,samp_kazu):
                samp_kyori[j1-1,j]=sum(np.square(seikiten[j,:]-seikiten[j1,:]))
        d_max=sqrt(max(max((samp_kyori))))                             #サンプル点間の最大距離

    def caluculate_r(self):#基底関数半径ｒの計算
        if dimension == 2:
            r=d_max/(np.sqrt(samp_kazu*dimension)^(1/dimension))
        else:
            r=d_max/(np.sqrt(dimension)*(sqrt(samp_kazu)^(1/dimension)))
        if r==0:
            r=0.5
            
    def caluculate_radial(self): #基底関数計算
        for j in range(samp_kazu):
            for j1 in range(samp_kazu):
                H(j,j1)=sum(np.square(seikiten[j,:]-seikiten[j1,:]))
                H(j,j1)=math.exp(-H(j,j1)/(np.square(r)))
            
    def caluculate_w(self):#基底関数計算開始#　ωの計算開始
        ramda = math.pow(10, 2)                                               #ラムダの設定
        G_ramda = ramda *np.eye(samp_kazu,samp_kazu)                     #ラムダの行列
        A=H.T * H + G_ramda
        omega = inv(A) * H.T * y_rbf                                            #重み値ωの設定
###############　ωの計算終了　##############

###############　出力関数O(x)　##############

###############　出力関数O(x)　##############
#fprintf('******* RBFN終了 *******************\n')