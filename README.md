### An Implementation of the BDIA Technique from [Exact Diffusion Inversion via Bi-directional Integration Approximation](https://arxiv.org/abs/2307.10829) By Guoqiang Zhang, J. P. Lewis, and W. Bastiaan Kleijn

In summary, BDIA can be applied to both diffusion sampling and diffusion inversion. Suppose we would like to estimate the next diffusion state $`z_{i-1}`$ based on the recent information $`(z_{i},t_i)`$ and $`(z_{i+1},t_{i+1})`$.  The basic idea of BDIA is to perform forward integration.
