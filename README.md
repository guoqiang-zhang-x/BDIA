### An Implementation of the BDIA Technique from "[Exact Diffusion Inversion via Bi-directional Integration Approximation](https://arxiv.org/abs/2307.10829)" By Guoqiang Zhang, J. P. Lewis, and W. Bastiaan Kleijn

##### In summary, BDIA can be applied to both diffusion sampling and diffusion inversion. Suppose we would like to estimate the next diffusion state $$z_{i-1}$$ at current timestep $$t_i$$.  The basic idea of BDIA is to perform forward integration.  ```math SE = \frac{\sigma}{\sqrt{n}} ```
