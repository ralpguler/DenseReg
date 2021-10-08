# DenseReg: 
## Fully Convolutional Dense Shape Regression In-the-Wild
*Rıza Alp Güler, George Trigeorgis, Epameinondas Antonakos, Patrick Snape, Stefanos Zafeiriou, Iasonas Kokkinos*
* * *
This is an implementation of the method described in the [arXiv paper](http://alpguler.com/DenseReg.html). For a video demonstration and supplementary materials see  [the project page](http://alpguler.com/DenseReg.html).

Currently, only the Caffe(deeplab) based test-code that allows regressing template face coordinates on a given image is available. Training code will be provided soon.
***
### Caffe Setup
You have two options:
#### 1- Use deeplabv2 submodule
First install deeplabv2. It is added as a submodule to this repository, you can follow its own installation instructions.
Make sure that you have set WITH_PYTHON_LAYER=1 in "Makefile.config" of the Caffe.

#### 2- Using your own caffe

Alternatively, you can use your favorite installed caffe, then all you need to add is the "interpolation layer", which can be found in the provided deeplab version. If you do this, you have to change the caffe path in (i)DenseReg.ipynb  and (ii) CombineRegressions.py caffe layer before "import caffe" line.

### Running DenseReg

+ You have to download the caffemodel by running the script: *get_densereg_model.sh*.
+ Then, you can use the ipyton notebook *DenseReg.ipynb*, which very basically demonstrates how example results for the *Lena's face* are obtained.

Namely, putting a uniform grid in the temple space onto the face, semantic face part segmentation and landmark localization results are demonstrated (as portrayed in the image below).

![](https://docs.google.com/drawings/d/1Jh2bSW5CGE8IHssDaj6D0i6zl2bY65xm7yPt5fRtIqM/pub?w=596&h=202)
 
 - - -
 ### Running DenseReg for Human Bodies

+ You have to download the caffemodel by running the script: *get_densereg_model.sh*.
+ Then, you can use the ipyton notebook *DenseRegHumanBody.ipynb*, which demonstrates dense-correspondences for human bodies on sample images. Note that this network is not trained to be invariant to changes in scale. 

Demonstrated result is depicted for a test sample.

![](https://docs.google.com/drawings/d/1DxuWFrcQpSYCEGxdfZyhPemnc25vX1cknpYFe1E-uMk/pub?w=471&h=208)
 
  - - -
#### Bibtex entry for citations:
 
      @article{Guler2016DenseReg,
      title={DenseReg: Fully Convolutional Dense Shape Regression In-the-Wild},
      author={R\{i}za Alp G\"uler, George Trigeorgis, Epameinondas Antonakos, Patrick Snape, Stefanos Zafeiriou, Iasonas Kokkinos},
      journal={arXiv:1612.01202},
      year={2016}
      }
thanks.

