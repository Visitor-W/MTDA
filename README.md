# MTDA-HSED [![arxiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2409.06196)
The official implementation of *MTDA-HSED:  Mutual-Assistance Tuning and Dual-Branch Aggregating for Heterogeneous Sound Event Detection.* (Submiited to ICASSP 2025)<br>Authors: Zehao Wang, Haobo Yue, Zhicheng Zhang, Da Mu, Jin Tang,Jianqin Yin




[Issues :blush:](https://github.com/Visitor-W) **|** [Lab :clap:](https://github.com/BUPT-COST-lab) **|** [Contact :mailbox:](wzhao@bupt.edu.cn)  

## Updating
Code will be released soon!

## Introduction

### Visualization of the M3A Module
<div align="center">
<img src="./fig/adapter.png" width="400" height="400">
</div>
By comparing the feature maps of the long-term, short-term audio adapter with the spectrograms of the input data, we can see that most of the time-frequency patterns modeled by short-term audio adapter are temporally isolated and disjoint. In contrast, the long-term audio adapter's patterns and their neighbors are in a whole, thereby forming a special time-frequency representation.



### Visualization of the DBMF Module
<div align="center">
<img src="./fig/DBMF.png" width="400" height="400">
</div>
We compare the aggregated feature map using the DBMF module with the feature map of the baseline, we can see that the feature map of the baseline is blurred, as shown in the second row of the figure. After aggregating the local and global feature, the information within the DBMF feature map is more prominent, as shown in the third row of the figure.



## Performance
MTDA-HSED is evaluated on [DESED](https://github.com/turpaultn/DESED) and [Mestro](https://ieeexplore.ieee.org/document/10016759)

Model                   | PSDS1    $\uparrow$| PSDS1(sed score) $\uparrow$| mpAUC $\uparrow$
:----------------------:|:------------------:|:--------------------------:|:----------------:
Baseline                | 0.494              | 0.499                      | 0.709            
ATST-SED                | 0.297              | 0.301                      | 0.554            
MONA                    | 0.497              | 0.507                      | 0.709            
ADAPTER                 | 0.494              | 0.503                      | 0.704                       
ACT-NET                 | 0.308              | 0.316                      | 0.696            
M3A(ours)               | <ins>0.503<ins>    | <ins>0.511</ins>           | <ins>0.753<ins>       
DBMF(ours)              | 0.494              | 0.501                      | 0.748    
MTDA-HSED(ours)         | **0.503**          | **0.514**                  | **0.757**

## Reference



## Citation
If this repository helped your works, please cite papers below! :kissing_heart:
```bib
@article{wang2024mtda,
  title={MTDA-HSED: Mutual-Assistance Tuning and Dual-Branch Aggregating for Heterogeneous Sound Event Detection},
  author={Wang, Zehao and Yue, Haobo and Zhang, Zhicheng and Mu, Da and Tang, Jin and Yin, Jianqin},
  journal={arXiv preprint arXiv:2409.06196},
  year={2024}
}
```
