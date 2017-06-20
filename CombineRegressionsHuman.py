
import sys
sys.path.append("/home/goku/py-faster-rcnn/caffe-fast-rcnn-alt/python")

import caffe
from scipy.misc import imresize
from scipy.misc import imresize
from scipy.io import savemat
import numpy as np
from PIL import Image

import random

from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy

class CombineRegressionsLayer(caffe.Layer):

    def setup(self, bottom, top):

        pass

    def reshape(self, bottom, top):

        top[0].reshape(*bottom[0].data.shape)
        top[1].reshape(*bottom[0].data.shape)

    def forward(self, bottom, top):

        Horizontal = bottom[0].data[...]
        Vertical = bottom[1].data[...]

        HorzRegress = bottom[2].data[...]
        VertRegress = bottom[3].data[...]

        HorzReg = np.zeros(Horizontal.shape);
        VertReg = np.zeros(Horizontal.shape);

        Num_Dims = HorzRegress.shape[1]

        # print(Horizontal.shape)
        # print(HorzRegress.shape)
        
        for j in range(Num_Dims):
            if (j>0):
                HorzReg = HorzReg + HorzRegress[:,j,:,:] * (Horizontal==j)
                VertReg = VertReg + VertRegress[:,j,:,:] * (Vertical==j)
        

        # HorzReg = ( ( Hozontal + HorzReg )  ) 
        # VertReg = ( ( Vertical + VertReg)  ) 

        HorzReg[HorzReg<0] = 0
        VertReg[VertReg<0] = 0

        HorzReg[HorzReg>1] = 1 
        VertReg[VertReg>1] = 1 

        top[0].data[...] = HorzReg
        top[1].data[...] = VertReg


    def backward(self, top, propagate_down, bottom):
        pass
