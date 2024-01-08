### An Implementation of the BDIA Technique from [Exact Diffusion Inversion via Bi-directional Integration Approximation](https://arxiv.org/abs/2307.10829) By Guoqiang Zhang, J. P. Lewis, and W. Bastiaan Kleijn

In brief, BDIA is a time-reversible ODE solver that can be applied to improve the performance of both diffusion sampling and diffusion inversion. Suppose we would like to estimate the next diffusion state $`\boldsymbol{z}_{i-1}`$ by solving a probability ordinary differential equation (ODE) 
```math
d\boldsymbol{z} = \boldsymbol{d}(\boldsymbol{z},t)dt
```
based on the recent information $`(\boldsymbol{z}_{i},t_i)`$ and $`(\boldsymbol{z}_{i+1},t_{i+1})`$.  The basic idea of BDIA is to compute $`\boldsymbol{z}_{i-1}`$ by performing both the forward integration approximation $`\Delta(t_i\rightarrow t_{i-1}|\boldsymbol{z}_i)`$ $`\left(\approx \int_{t_i}^{t_{i-1}}\boldsymbol{d}(\boldsymbol{z},t)dt\right)`$ and the backbackward integration approximation $`\Delta(t_i\rightarrow t_{i+1}|\boldsymbol{z}_i)`$ $`\left(\approx -\int_{t_{i+1}}^{t_{i}}\boldsymbol{d}(\boldsymbol{z},t)dt\right)`$ conditioned on $\boldsymbol{z}_i$. With the above two integration approximations, $`\boldsymbol{z}_{i-1}`$ can be expressed as  
```math
\boldsymbol{z}_{i-1} = \boldsymbol{z}_{i+1} \underbrace{- (1-\textcolor{blue}{\gamma}) (\boldsymbol{z}_{i+1}-\boldsymbol{z}_{i}) - \textcolor{blue}{\gamma}\Delta(t_i\rightarrow t_{i+1}|\boldsymbol{z}_i)}_{\approx \int_{t_{i+1}}^{t_{i}}\boldsymbol{d}(\boldsymbol{z},t)dt } + \underbrace{\Delta(t_i\rightarrow t_{i-1}|\boldsymbol{z}_i)}_{ \approx \int_{t_i}^{t_{i-1}}\boldsymbol{d}(\boldsymbol{z},t)dt } 
```
where $\gamma=[0,1]$ averages the backward and forward integration approximations for the time-slot $`[t_{i+1},t_i]`$. One nice property of the above update expression is that it is invertiable. That is, $\boldsymbol{z}_{i+1}$ can be represented as an expression of $`\boldsymbol{z}_{i-1}`$ and $`\boldsymbol{z}_{i}`$, which enables exact diffusion inversion. 

The BDIA technique can be applied directly to DDIM. In this case, the forward integration approximation $`\Delta(t_i\rightarrow t_{i-1}|\boldsymbol{z}_i)`$ becomes the DDIM updates, which is given by 
```math
\Delta(t_i\rightarrow t_{i-1}|\boldsymbol{z}_i) =  \alpha_{i-1} \left(\frac{\boldsymbol{z}_{i} \hspace{-0.3mm}-\hspace{-0.3mm} \sigma_{i}\hat{\boldsymbol{\epsilon}}_{\boldsymbol{\theta}}(\boldsymbol{z}_{i}, i) }{\alpha_{i}}\right)+\hspace{0.5mm}\sigma_{i-1}\hat{\boldsymbol{\epsilon}}_{\boldsymbol{\theta}}(\boldsymbol{z}_{i}, i)   - \boldsymbol{z}_i
```
One can then work out the the final update expression of BDIA-DDIM (please check the paper for details).

One can also apply the BDIA technique to the EDM and DPM-Solver++ sampling procedures. Experiments on BDIA-EDM show that it outperforms EDM consitently over four pre-trained models in terms of FID scores.  The details can be found out in the paper. 

-------------------------------------------------------
#### [Images generated by BDIA-DDIM and DDIM for text-to-image generation with 10 timesteps over StableDiffusion V2]

<a href="URL_REDIRECT" target="blank"><img align="center" src="https://github.com/guoqiang-zhang-x/BDIA/blob/main/image_examples/BDIADDIM_t2i_20pairs.png" width="900" /></a>

-------------------------------------------------------
#### [Demonstration of controlnet-based image editing by BDIA-DDIM with 10 timesteps]

<a href="URL_REDIRECT" target="blank"><img align="center" src="https://github.com/guoqiang-zhang-x/BDIA/blob/main/image_examples/controlnet_BDIA_pro.png" width="900" /></a>

<a href="URL_REDIRECT" target="blank"><img align="center" src="https://github.com/guoqiang-zhang-x/BDIA/blob/main/image_examples/controlnet_BDIA_2nd.png" width="900" /></a>

-------------------------------------------------------
#### [Demonstration of text-based image editing by BDIA-DDIM using StableDiffusion]

<a href="URL_REDIRECT" target="blank"><img align="center" src="https://github.com/guoqiang-zhang-x/BDIA/blob/main/image_examples/woman_editing_2nd.png" width="900" /></a>




