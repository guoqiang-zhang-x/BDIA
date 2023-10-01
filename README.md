### An Implementation of the BDIA Technique from [Exact Diffusion Inversion via Bi-directional Integration Approximation](https://arxiv.org/abs/2307.10829) By Guoqiang Zhang, J. P. Lewis, and W. Bastiaan Kleijn

In summary, BDIA can be applied to both diffusion sampling and diffusion inversion. Suppose we would like to estimate the next diffusion state $`z_{i-1}`$ based on the recent information $`(z_{i},t_i)`$ and $`(z_{i+1},t_{i+1})`$.  The basic idea of BDIA is to compute $`z_{i-1}`$ by performing both the forward integration approximation $`\Delta(t_i\rightarrow t_{i-1}|\boldsymbol{z}_i)`$ and the backbackward integration approximation $`\Delta(t_i\rightarrow t_{i+1}|\boldsymbol{z}_i)`$. As a result, $`z_{i-1}`$ can be expressed as  
```math
z_{i-1} = z_{i+1}+ \Delta(t_i\rightarrow t_{i+1}|\boldsymbol{z}_i)
```
