# Literature Review

This document records relevant and comparable points on each of the papers, listed below. No derivations or other *descriptions* can be found here (unless necessary for comparison). Please refer to the individual papers for the same.

**N.B.: ⚙ denotes work in progress.**

## List of packages/papers - (⚙)
Check `./Papers (Non-Annotated)` for the .PDFs.
* *NA* : [Fuerst et al (2004)](https://www.aanda.org/articles/aa/abs/2004/36/aa0814/aa0814.html)
* `HARM` : [Gammie et al (2003)](https://iopscience.iop.org/article/10.1086/374594/fulltext/)
* `geokerr` : [Dexter et al (2009)](https://iopscience.iop.org/article/10.1088/0004-637X/696/2/1616)
* `YNOGK` : [Yang et al (2013)](https://iopscience.iop.org/article/10.1088/0067-0049/207/1/6)
* `grtrans` : [Dexter et al (2016)](https://academic.oup.com/mnras/article/462/1/115/2589406) |  https://github.com/jadexter/grtrans
* `ODYSSEY` : [Pu et al (2016)](https://iopscience.iop.org/article/10.3847/0004-637X/820/2/105)
* `GRay` : [Chan et al (2013)](https://iopscience.iop.org/article/10.1088/0004-637X/777/1/13) | https://github.com/luxsrc/gray (Check `gray1` branch) 
* `GRay2` : [Chan et al (2018)](https://iopscience.iop.org/article/10.3847/1538-4357/aadfe5) | https://github.com/luxsrc/gray (Check branches)
* `RAPTOR` : [Bronzwaer et al (2018)](https://doi.org/10.1051/0004-6361/201732149)
* `ipole` : [Moscibrodzka et al (2017)](https://inspirehep.net/literature/1642211) | https://github.com/moscibrodzka/ipole/tree/ipole-dev
* `BHAC` : [Porth et al (2017)](https://comp-astrophys-cosmol.springeropen.com/articles/10.1186/s40668-017-0020-2)
* `ARTIST` : [Takahashi et al (2017)](https://academic.oup.com/mnras/article/464/4/4567/2562611)
* `projectkerr` (Not a published paper) : [Raquepas et al (2017)](http://www.math.mcgill.ca/gantumur/math599w17/project-kerr.pdf)
* `starless` (Not a published paper) : [Riccardo Antonelli](https://github.com/rantonels/starless)


## Summarized Comparison Table - (⚙)

*Some rows seem redundant now. To be removed.*

| Comparison Points ⬇ \ Papers ➡ | `geokerr` | `YNOGK` | `ODYSSEY` | `ARTIST` | `BHAC` | `RAPTOR` | `projectkerr` | `starless` | `grtrans` | `ipole` | `GRay` | `GRay2` | `HARM`
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Approach | Semi-Analytical | Semi-Analytical | ⚙ | ⚙ | ⚙ | Numerical | Semi-Analytical | Analytical | ⚙ |⚙ | ⚙ | Numerical | ⚙ |
| Performs RayTracing | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ✔ | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ✔ | ⚙ |
| Performs Radiative Transfer | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ✔ | ❌ | ❌ | ✔ | ✔ | ⚙ | ❌<sup>#4<sup> | ⚙ |
| Accuracy<sup>1</sup> | ⭐⭐⭐ | ⭐⭐⭐ | ⚙ | ⚙ | ⚙ | ⭐⭐⭐ | ⭐ | ⭐ | ⚙ |⚙ | ⚙ | ⭐⭐⭐ | ⚙ |
| Speed<sup>2</sup> | ⚡⚡⚡ | ⚡⚡⚡ | ⚙ | ⚙ | ⚙ | ⚡⚡ | ⚡ | ⚡ | ⚙ |⚙ | ⚙ | ⚡⚡⚡ | ⚙ |
| Extensible to GRMHD | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ✔ | ❌ | ❌ | ⚙ |⚙ | ⚙ | ⚠<sup>#5<sup> | ⚙ |
| Black Hole Shadow | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ✔ | ✔<sup>#1<sup> | ✔<sup>#1<sup> | ⚙ |⚙ | ⚙ | ✔ | ⚙ |
| Accretion Disk & Flow | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ✔ | ❌ | ✔<sup>#2<sup> | ⚙ |⚙ | ⚙ | ❌ | ⚙ |
| Redshift calculations | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ✔ | ❌ | ❌ | ⚙ |⚙ | ⚙ | ❌ | ⚙ |
| Lensing simuation | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ✔ | ❌ | ✔<sup>#3<sup> | ⚙ |⚙ | ⚙ | ❌ | ⚙ |
| Builds up on | ⚙ | `geokerr` | ⚙ | ⚙ | ⚙ | `geokerr`, `BHAC` | [Interstellar (Movie)](https://www.imdb.com/title/tt0816692/) | [Interstellar (Movie)'s BH](https://www.imdb.com/title/tt0816692/) | ⚙ |⚙ | ⚙ | `GRay` | ⚙ |
| Extras |  |  |  |   |  |Works for arbitrary spacetimes, Adaptive integration step size | Good introduction to the problem | Nice wallpapers and gifs | ⚙ | ⚙ | ⚙ | More efficient than `RAPTOR` apparently | ⚙ |

#### Notes:
* <sup>1</sup> Relative accuracy (based on papers' self-report)
  * highly accurate: ⭐⭐⭐
  * accurate: ⭐⭐
  * so-so: ⭐
* <sup>2</sup> Relative speed (based on papers' self-report) | Assuming `FORTRAN > C/C++ > Python ~ MATLAB`, if performance metrics are not mentioned in the paper
  * Very fast: ⚡⚡⚡
  * Fast: ⚡⚡
  * Slow: ⚡
* <sup>#1</sup> The shadow is not calculable. It's more of an initial condition.
* <sup>#2</sup> Artificially added.
* <sup>#3</sup> Nothing of analytic importance can be obtained from it.
* <sup>#4<sup> Can be extended to support Radiative Transfer. Paper itself does not present any work on it.
* <sup>#5</sup> Fast light paradigm. Complex accretion flow models not supported

### INITIAL IMPRESSIONS:
* For Ray Tracing: Prefer `geokerr`, `YNOGK`, `RAPTOR`, `GRay`, `GRay2`
* For Strong Gravity Simulations : Prefer `RAPTOR`, `BHAC`, `ARTIST`, `HARM`
* For Accretion Flow (GRMHD) : Prefer `ARTIST`, `BHAC`
* For wallpapers & gifs : Prefer `starless` 😉


## Verbose Comparison - (⚙)
**N.B.: ⚙ denotes work in progress.**

### <sup>##</sup>Use-cases of interest are:
* Black Hole Shadow
* Accretion Disk & Flow
* Redshift calculations
* Lensing simuation
* Overall extensibility to GRMHD simulations

### A. `projectkerr` - Raquepas et al (2017) - `G = c = 1`
* Written in `MATLAB`
* Solves in Boyer-Lindquist Coordinates
* Works in Kerr Spacetime
* Hamiltonian Approach -> Requires an initial position and momentum
* Makes use of the conserved quanitites -> *Angular Momentum, L* and *Energy, E*
* Uses RK4 integration scheme
* Integrates from observer to source
* Considers infinitesimally thin disk

* **Pros**:
  * Simple model -> Good introduction to the problem
  * Useful for visualizing null trajectories, but fails for complex ones
* **Cons**:
  * Simple model -> Does not consider radiative transfer
  * Useless for probing (getting physically relevant values out of) the integrated geodesics


### B. `starless` - Riccardo Antonelli (~2 years ago)
* Uses Schwarschild Metric
* More of a hobbyist project, capable of producing some nice lensing effects on images
* Does perform geodesic integration, but doesn't seem useful for probing physical quantities
* Kudos for multiprocessing, though


### C. `geokerr` - Dexter et al (2009) - `G = c = M = 1`
* Written in `FORTRAN77`
* Solves in Boyer-Lindquist Coordinates, provides transformations to Kerr-Schild Coordinates
* Works in Kerr Spacetime
* Hamiltonian Approach -> Requires an initial position and momentum
* Makes use of the conserved quanitites -> *Angular Momentum, L*, *Energy, E* and *Carter's Constant, Q*
* Uses Carlson's Elliptic Integrals to simplify algebraic manipulation -> Converts the integral computation into a root finding problem (or multiple root finding problems)
* Neglects plasma effects, scattering and absorption
* Integrates from observer to source
* Integration is piece-wise
* Considers thin disk accretion, based on an optically thin emission surface model
* Considers all cases of interest<sup>##</sup> (🆙)
* Is generalized to `grtrans` (2016), that can handle polarized radiative transfer


* **Pros**:
  * At a minimum, "~3 to 5 times faster than" a simplistic numerical geodesic computation algorithm. Increases massively (~300 to ~500 times) for more complicated cases (All in `FORTRAN`). Real world implications against Python not considered, in this review.
  * Rapid and accurate geodesic calculations
  * Extensible to GRMHD simulations
  * Generalized to Polarized Radiative Transfer in a 2016 paper (`grtrans`)
* **Cons**:
  * FORTRAN77 implementation is difficult to understand
  * Requires knowledge of turning points, in advance
  * No adaptive meshing near the strong gravity regions (close to the Black Hole)


### D .`YNOGK` - Yang et al (2013) - `G = c = M = 1`
* Written in `FORTRAN95`
* Builds on `geokerr` and Dexter et al's work
* Solves in Boyer-Lindquist Coordinates
* Works in Kerr Spacetime
* Hamiltonian Approach -> Requires an initial position and momentum
* Makes use of the conserved quanitites -> *Angular Momentum, L*, *Energy, E* and *Carter's Constant, Q*
* Parameterizes all coordinates and affine parameter with 'p'
* Uses Carlson's method to compute Weierstrass' and Jacobi's Elliptic Integrals (Cubic in order) - a bit simpler than Dexter et al's approach
* Handles turning points, unlike `geokerr`
* Handles arbitrary distance of the observer to the compact object
* Handles motion state of the observer, with respect to the compact object
* Converts many of the problems (BH Shadow imaging, connecting observer and emitter, line profile calculation) to root finding problems
* Allows tracking emission from a sophisticated surface, like a Rotationally-supported Torus, and not only a thin accretion disk (like in `geokerr`)
* Integrates from observer to source
* Integration is piece-wise (less so, than `geokerr`)
* Considers all cases of interest<sup>##</sup> (🆙)

* **Pros**:
  * Fast & Accurate (slightly slower than `geokerr`)
  * Information about turning points need not be specified in advance.
  * Object Oriented Code -> Extensible, if not for poor structure
  * Handles distance and relative motion between the emitter and observer
  * Allows for more complicated emission surface models (than `geokerr`)
  * Can be extended to computation of timelike geodesics without any changes
  * Extended to Kerr-Newman (Polarized case) (according to the paper)
* **Cons**:
  * Not too different from `geokerr`
    * Here too, certain cases (corresponding to the turning points) have been specifically handled - much less in number than `geokerr`. (Section 3.1 in paper)
    * `Nt1` & `Nt2` seem like a slightly complicated way to handle the problem of not knowing all turning points in advance. Commendations on finding a sequence though.
    * "the inner routines of our code" handle the turning points -> The code still has to manage the turning points, although the user does not need to specify them
  * No adaptive meshing, here as well


### E. `RAPTOR` - Bronzwaer et al (2018) - `G = c = 1`
* Written in `C`, with a plotting module in `Python`
* Numerical
* General to all spacetimes -> May be extensible to binary BH systems, neutron stars and **expanding FRW spacetime**
* Automatically takes into account all gravitational effects
* CPU & GPU agnostic -> Supports OpenMP (CPU Multiprocessing) and OpenACC (GPU Multiprocessing) (*Used as basis for ⚡⚡ speed rating*)
* Minimal physical assumptions -> Supports arbitrary spacetimes & Time-Dependent Radiative Transfer
* Hamiltonian Approach -> Requires an initial position and momentum
* Makes use of the conserved quanitites -> *Angular Momentum, L*, *Energy, E* and *Carter's Constant, Q*
* RK4 (more accurate) and Velocity Verlet, with adaptive step size (slightly less accurate, but faster)
* Integrates from observer to source
* Null geodesic integration and radiative transfer independent of choice of coordinate system or spacetime geometry
* Uses BL Coordinates, Modified BL, Kerr-Schild (KS) and Modified KS
* Radiative transfer ignores plasma refraction effects, scattering and polarization
* Accounts for changes in plasma structure
* Simultaneously integrates null geodesic and specific intensity, allowing for:
  * Cutting off integration at a threshold (based on optical depth)
  * No need to store geodesic
  * Choosing proper integration step size for both calculations (Syncs step size with spacetime mesh)
* Geodesic integration and Line Profile -> Shows excellent correspondence with `geokerr` (*Used as basis for ⭐⭐⭐ accuracy rating*)
* Accretion flow -> Shoes excellent correspondence with `BHAC` (*Used as basis for ⭐⭐⭐ accuracy rating*)
* Considers fast and slow light accretion flow
* Considers all cases of interest<sup>##</sup> (🆙)

* **Pros**:
  * Generalizable to other spacetimes
  * Adaptive step size helps with accuracy and stability
  * Synced step size for radiative transfer calculations
  * Consideration of plasma effects and relatively complicated accretion disk models
  * Multiprocessing support
  * Correspondence with `BHAC` and `geokerr`
* **Cons**:
  * Slower than `geokerr` and other semi-analytical approaches


### E. `GRay2` - Chan et al (2018) - `G = c = 1`
* Written in `C`
* Numerical
* Implementation is specific to Kerr (More on this in the *Differences* section below)
* Minimal physical assumptions on the integrator
* Hamiltonian Approach
* Does not make use of the conserved quanitites. Most quantities are unconstrained.
* RK4
* Integrates from observer to source
* Uses Cartesian form of KS Coordinates
* Stable for pathological orbits
* Considers fast light accretion flow -> Does not account for changes in plasma structure
* OpenCL support -> "Massively parallel"
* Supports timelike geodesics
* Supports redering trajectories from acrretion flow models, created in GRMHD software

* **Pros**:
  * Mathematical manipulations
    * Avoids singularities
    * Efficieny and stability boost
  * Almost as fast as semi-analytical approaches
  * Stability
  * Extensible to Radiative Transfer applications, but major additions required
  * Support for timelike geodesics
  * OpenCL support
* **Cons**:
  * Not general to other spacetimes 
  * Does not consider plasma effects
  * Is not extensible to GRMHD directly, but allows for using accretion flow models created in existing GRMHD software
  * No adaptive meshing
  * Does not consider all cases of interest<sup>##</sup> (🆙)
  * OpenCL support is through `lux` - not well known

#### Differences between `GRay2` and other geodesic integrators:
1. `GRay2` uses KS coordinates and makes some mathematical manipulations, that allow it to speed-up computation and make it more stable. Some of them are:
   1. Expanding the Christoffel Symbols and ignoring the symmetrization of $g_{\mu\nu}$ in the geodesic equation.
   2. Deals in non-tensorial quantities (metric comma derivatives).
   3. Exploits the symmetries in equations, written in KS coordinates
2. The cartesian form of KS coordinates does not have singularities at the event horizon (*horizon-penetrating*) or the poles (unlike BL). This makes `GRay2` more hands-off and more stable.
3. To increase the accuracy of the fast light approximation (ever so slightly) and decrease the overall bandwidth requirement, `GRay2` uses coordinate time integration, instead of using the affine parameter. It should be noted, that using KS automatically means more space requirement due to more quantities, which would otherwise be 0, in BL.
4. `GRay2` does not make use of the conserved quanitites. Most quantities are unconstrained. However, for convergence tests, certain lorentz scalars have been used.


## Comparison between Numerical Integration & Analytical Approaches (Elliptical Functions) - (⚙)

*I am ignoring the Transfer Function Method. It's outdated now, with not much work going on.*


| Numerical Integration | Analytical Method (Elliptical Functions) |
|:---:|:---:|
| Handles 3D accretion flow well | Analytical formula for 3D seems complex and computationally intensive to implement (can be partly overcome, though - `YNOGK`) |
| Simpler and faster for higher dimensions | Faster in most other computations |
| Slower, as each point on the geodesic has to be evaluated | Faster, as arbitrary sections of the geodesic can be computed |
| Can be massively sped up by using parallel programming | Here, since calculations are implementation (Math) - specific, speed improvements are negligible, but these methods are already very fast |
| Mostly general to all spacetimes | Specific to particular spacetimes, where metric and connection are known |
| Less accurate | Spatial accuracy independent of integration step size |


## Resources:

1. `HARM`, `ipole` and other relevant projects: https://github.com/AFD-Illinois