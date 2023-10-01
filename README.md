### An Implementation of the BDIA Technique from [Exact Diffusion Inversion via Bi-directional Integration Approximation](https://arxiv.org/abs/2307.10829) By Guoqiang Zhang, J. P. Lewis, and W. Bastiaan Kleijn

In summary, BDIA can be applied to both diffusion sampling and diffusion inversion. Suppose we would like to estimate the next diffusion state $`\boldsymbol{z}_{i-1}`$ by solving a probability ordinary differential equation (ODE) 
```math
d\boldsymbol{z} = \boldsymbol{d}(\boldsymbol{z},t)dt
```
based on the recent information $`(\boldsymbol{z}_{i},t_i)`$ and $`(\boldsymbol{z}_{i+1},t_{i+1})`$.  The basic idea of BDIA is to compute $`\boldsymbol{z}_{i-1}`$ by performing both the forward integration approximation $`\Delta(t_i\rightarrow t_{i-1}|\boldsymbol{z}_i)`$ and the backbackward integration approximation $`\Delta(t_i\rightarrow t_{i+1}|\boldsymbol{z}_i)`$. As a result, $`\boldsymbol{z}_{i-1}`$ can be expressed as  
```math
\boldsymbol{z}_{i-1} = \boldsymbol{z}_{i+1} \underbrace{- \gamma (\boldsymbol{z}_{i+1}-\boldsymbol{z}_{i}) - (1-\gamma)\Delta(t_i\rightarrow t_{i+1}|\boldsymbol{z}_i)}_{\approx \int_{t_{i+1}}^{t_{i}}\boldsymbol{d}(\boldsymbol{z},t)dt } + \underbrace{\Delta(t_i\rightarrow t_{i+1}|\boldsymbol{z}_i)}_{ \approx \int_{t_i}^{t_{i-1}}\boldsymbol{d}(\boldsymbol{z},t)dt } 
```
where $\gamma=[0,1]$. Once nice property of the above update expression is that it is invertiable. That is, $\boldsymbol{z}_{i+1}$ can be represented as an expression of $`\boldsymbol{z}_{i-1}`$ and $`\boldsymbol{z}_{i+1}`$, thus enabling exact diffusion inversion. 

The BDIA technique can be applied directly to DDIM. In this case, the forward integration approximatio $`\Delta(t_i\rightarrow t_{i-1}|\boldsymbol{z}_i)`$ becomes the DDIM updates, which is given by 
```math
\Delta(t_i\rightarrow t_{i-1}|\boldsymbol{z}_i) =  \alpha_{i-1} \left(\frac{\boldsymbol{z}_{i} \hspace{-0.3mm}-\hspace{-0.3mm} \sigma_{i}\hat{\boldsymbol{\epsilon}}_{\boldsymbol{\theta}}(\boldsymbol{z}_{i}, i) }{\alpha_{i}}\right)+\hspace{0.5mm}\sigma_{i-1}\hat{\boldsymbol{\epsilon}}_{\boldsymbol{\theta}}(\boldsymbol{z}_{i}, i)   - \boldsymbol{z}_i
```
