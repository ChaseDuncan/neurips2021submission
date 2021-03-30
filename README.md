# NeurIPS 2021 submission 

![alt text](https://github.com/ChaseDuncan/tmipaper/blob/main/pics/problem_statement5_resize.png?raw=true)

## The problem

**Estimating** prediction **uncertainty** in **DNN**s on volumetric (**3D**) biomedical **image segmentation**.

![alt text](https://github.com/ChaseDuncan/tmipaper/blob/main/pics/3d_out.png?raw=true)

### Key challenge: scale

- Study the practical problem of scaling up the method of large ensembles for estimating prediction uncertainty in DNNs for 3D MR image segementation.
- Novelly show how transforming the problem into a lower-dimensional problem space allows for efficient 3D ensembling that maintains segmentation performance while simultaneously improving predictive uncertainty estimation.
- *Propose novel method for distributed training that only trains the decoder part of the standard Unet-based representation.*
- *Leverage existing resources from computer vision community to further reduce computational cost.*

## Background
[Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles](https://arxiv.org/abs/1612.01474)
Lakshminarayanan, et al. *NeurIPs 2017*

## Related Work I
[Confidence Calibration and Predictive Uncertainty Estimation for Deep Medical Image Segmentation](https://arxiv.org/abs/1911.13273)
Mehrtash, et al., *Journal of IEEE Transactions on Medical Imaging 2019*

<!-- ![alt text](https://github.com/ChaseDuncan/tmipaper/blob/main/pics/dsc_vs_ce.png?raw=true) -->

## Related Work II
[Attention-Guided Version of 2D UNet for Automatic Brain Tumor Segmentation](https://arxiv.org/abs/2004.02009)
Noori, et al.
*International Conference on Computer and Knowledge Engineering (ICCKE) 2019*

## Related Work III
[On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599)
Guo, et al., *ICML 2017*

## Related Work IV
[Critical Assessment of Transfer Learning for Medical Image Segmentation with Fully Convolutional Neural Networks](https://arxiv.org/abs/2006.00356)
Karimi, et al. 2020

