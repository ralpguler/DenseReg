# This is a python layer used for combining the quantized values and estimated residuals for each quantized value.
# Note that you might have to change the caffe location below.

import sys
sys.path.append("DeepLab-Context2/python")

import caffe
import numpy as np


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
        
        for j in range(Num_Dims):
            if (j>0):
                HorzReg = HorzReg + HorzRegress[:,j,:,:] * (Horizontal==j)
                VertReg = VertReg + VertRegress[:,j,:,:] * (Vertical==j)
        

        HorzReg = ( ( Horizontal + HorzReg ) -1 ) / (Num_Dims-1)
        VertReg = ( ( Vertical + VertReg) -1 ) / (Num_Dims-1)

        HorzReg[HorzReg<0] = -1
        VertReg[VertReg<0] = -1

        top[0].data[...] = HorzReg
        top[1].data[...] = VertReg


    def backward(self, top, propagate_down, bottom):
        pass
