### An Implementation of the BDIA Technique from [Exact Diffusion Inversion via Bi-directional Integration Approximation](https://arxiv.org/abs/2307.10829) By Guoqiang Zhang, J. P. Lewis, and W. Bastiaan Kleijn

In summary, BDIA can be applied to both diffusion sampling and diffusion inversion. Suppose we would like to estimate the next diffusion state $`\boldsymbol{z}_{i-1}`$ by solving a probability ordinary differential equation (ODE) based on the recent information $`(\boldsymbol{z}_{i},t_i)`$ and $`(\boldsymbol{z}_{i+1},t_{i+1})`$.  The basic idea of BDIA is to compute $`\boldsymbol{z}_{i-1}`$ by performing both the forward integration approximation $`\Delta(t_i\rightarrow t_{i-1}|\boldsymbol{z}_i)`$ and the backbackward integration approximation $`\Delta(t_i\rightarrow t_{i+1}|\boldsymbol{z}_i)`$. As a result, $`\boldsymbol{z}_{i-1}`$ can be expressed as  
```math
\boldsymbol{z}_{i-1} = \boldsymbol{z}_{i+1} \underbrace{- \gamma (\boldsymbol{z}_{i+1}-\boldsymbol{z}_{i}) - (1-\gamma)\Delta(t_i\rightarrow t_{i+1}|\boldsymbol{z}_i)}_{asfd} + \underbrace{\Delta(t_i\rightarrow t_{i+1}|\boldsymbol{z}_i)}_{\approx \int_{t_i}^{t_{i-1}}\boldsymbol{d}(\boldsymbol{z},t)dt } 
```
