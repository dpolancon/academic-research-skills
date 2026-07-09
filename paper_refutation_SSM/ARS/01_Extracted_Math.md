# Mathematical Foundations of the Sraffian Supermultiplier with Unbalanced Capacity Transformation

We reformulate the Sraffian Supermultiplier (SSM) model from first principles to address the reviewer's concerns, using $\theta$ as the central parameter representing the relation between labor productivity growth and mechanization growth.

## 1. Technological and Accounting Foundations

Let $K$ denote the aggregate capital stock, $Y$ denote actual output, $Y^p$ denote potential (capacity) output, and $L$ denote labor employment. 

* **Capital-Capacity Ratio**: The capital-capacity ratio $v$ is defined as:
  $$ v \equiv \frac{K}{Y^p} $$
* **Labor Productivity and Mechanization**: Let $A^p \equiv Y^p/L$ denote labor productivity at capacity, and $Q \equiv K/L$ denote the capital-labor ratio (mechanization). We can express the capital-capacity ratio as:
  $$ v = \frac{K/L}{Y^p/L} = \frac{Q}{A^p} $$
* **Growth rate of $v$**: Taking the natural logarithm and differentiating with respect to time yields:
  $$ \hat{v} = \hat{Q} - \hat{A}^p = q - a^p $$
  where $q \equiv \hat{Q}$ is the rate of mechanization and $a^p \equiv \hat{A}^p$ is the growth rate of capacity labor productivity.

## 2. Technical Change and the Elasticity Parameter $\theta$

We introduce the parameter $\theta > 0$ as the technical progress parameter representing the elasticity of capacity labor productivity growth with respect to mechanization growth:
$$ a^p = \theta q $$
This relation represents the joint evolution of the rate of change of labor productivity and mechanization. Substituting this technical relation into the growth rate of the capital-capacity ratio yields:
$$ \hat{v} = q - \theta q = (1 - \theta)q $$

* **Balanced Growth**: When $\theta = 1$, we have $a^p = q$, and the capital-capacity ratio is constant ($\hat{v} = 0$).
* **Unbalanced Growth**: When $\theta \neq 1$, labor productivity growth does not track mechanization growth, leading to a time-varying capital-capacity ratio ($\hat{v} \neq 0$).

## 3. Okishio-Harrod Accelerator and Mechanization Growth

Induced investment is governed by the Okishio-Harrod accelerator function, where capital accumulation responds to the utilization gap. Normalizing the normal capacity utilization rate to unity ($\mu_n = 1$), the growth rate of capital stock $g_K$ is:
$$ g_K \equiv \hat{K} = \gamma(\mu - 1) $$
where $\gamma > 0$ represents the adjustment sensitivity.
Assuming that the rate of mechanization is driven by capital accumulation (normalizing labor growth to zero for simplicity), we have $q = g_K = \gamma(\mu - 1)$. This gives the rate of change of the capital-capacity ratio as:
$$ \hat{v} = (1 - \theta)\gamma(\mu - 1) $$

## 4. Derivation of the Investment Share Dynamics

The investment share is defined as $\phi \equiv I/Y$. Since net investment is $I = \dot{K}$, we have:
$$ \phi = \frac{\dot{K}}{Y} = \frac{\dot{K}}{K} \frac{K}{Y} = g_K \frac{v}{\mu} $$
where $\mu \equiv Y/Y^p = \frac{v Y}{K}$ is the capacity utilization rate.

To derive the growth rate of the investment share $\hat{\phi}$, we take the natural logarithm of both sides and differentiate with respect to time:
$$ \ln \phi = \ln g_K + \ln v - \ln \mu \implies \hat{\phi} = \hat{g}_K + \hat{v} - \hat{\mu} $$

To determine $\hat{g}_K$, we differentiate the accelerator function $g_K = \gamma(\mu - 1)$ with respect to time:
$$ \dot{g}_K = \gamma \dot{\mu} $$
The growth rate of $g_K$ is:
$$ \hat{g}_K = \frac{\dot{g}_K}{g_K} = \frac{\gamma \dot{\mu}}{\gamma(\mu - 1)} = \frac{\dot{\mu}}{\mu - 1} $$
Since $\dot{\mu} = \mu \hat{\mu}$, we substitute this to get:
$$ \hat{g}_K = \frac{\mu}{\mu - 1}\hat{\mu} $$

Substituting $\hat{g}_K$ and $\hat{v} = (1 - \theta)\gamma(\mu - 1)$ into the expression for $\hat{\phi}$ yields:
$$ \hat{\phi} = \frac{\mu}{\mu - 1}\hat{\mu} + (1 - \theta)\gamma(\mu - 1) - \hat{\mu} $$
$$ \hat{\phi} = \left( \frac{\mu}{\mu - 1} - 1 \right)\hat{\mu} + (1 - \theta)\gamma(\mu - 1) $$
$$ \hat{\phi} = \frac{1}{\mu - 1}\hat{\mu} + (1 - \theta)\gamma(\mu - 1) $$
This provides a rigorous derivation of the investment share dynamic equation from first principles.

## 5. Capacity Utilization Growth Dynamics

The growth rate of capacity utilization is derived from the definition $\mu = \frac{v Y}{K}$:
$$ \hat{\mu} = \hat{v} + \hat{Y} - \hat{K} $$

In the Sraffian Supermultiplier framework, output is demand-determined:
$$ Y = \frac{Z}{s + m - \phi} $$
where $Z$ is autonomous demand (growing at rate $g_z > 0$), $s$ is the marginal saving propensity, and $m$ is the marginal import propensity. Taking logs and differentiating gives output growth:
$$ \hat{Y} = g_z + \frac{\phi}{s + m - \phi}\hat{\phi} $$

Substituting $\hat{v} = (1 - \theta)\gamma(\mu - 1)$, $\hat{Y}$, and $\hat{K} = \gamma(\mu - 1)$ into the capacity utilization growth equation yields:
$$ \hat{\mu} = (1 - \theta)\gamma(\mu - 1) + g_z + \frac{\phi}{s + m - \phi}\hat{\phi} - \gamma(\mu - 1) $$
$$ \hat{\mu} = g_z + \frac{\phi}{s + m - \phi}\hat{\phi} - \theta\gamma(\mu - 1) $$
This completes the specification of the 2D dynamic system in $(\mu, \phi)$.