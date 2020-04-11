# Literature Review

## Comparison of various Papers on Raytracing and Radiative Transfer

This document records points about each of the papers, that are important to compare these papers. No derivations or other *descriptions* can be found here (unless necessary for the comparison). Please refer to the individual papers for the same.

### List of codes/papers (Evolving):
  * NA : [Fuerst et al](https://www.aanda.org/articles/aa/abs/2004/36/aa0814/aa0814.html)
  * `geokerr` : [Dexter et al (2009)](https://iopscience.iop.org/article/10.1088/0004-637X/696/2/1616)
    * `YNOGK` : [Yang et al (2013)](https://iopscience.iop.org/article/10.1088/0067-0049/207/1/6)
  * `ODYSSEY` : [Pu et al (2016)](https://iopscience.iop.org/article/10.3847/0004-637X/820/2/105)
  * `ARTIST` : [Takahashi et al (2017)](https://academic.oup.com/mnras/article/464/4/4567/2562611)
  * `BHAC` : [Porth et al (2017)](https://comp-astrophys-cosmol.springeropen.com/articles/10.1186/s40668-017-0020-2)
  * `projectkerr` (Not a published paper) : [Raquepas et al (2017)](http://www.math.mcgill.ca/gantumur/math599w17/project-kerr.pdf)
  * `RAPTOR` : [Bronzwaer et al (2018)](https://doi.org/10.1051/0004-6361/201732149)
  * `starless` (Not a published paper) : [Riccardo Antonelli](https://github.com/rantonels/starless)
  * `grtrans` : LINK TO BE ADDED


## Summarized Comparison Table

**N.B.: ⚙ denotes work in progress.**

| Comparison Points ⬇ \ Papers ➡ | `geokerr` | `YNOGK` | `ODYSSEY` | `ARTIST` | `BHAC` | `RAPTOR` | `projectkerr` | `starless` | `grtrans` |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Performs RayTracing | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ⚙ | ✔ | ✔ | ⚙ |
| Performs Radiative Transfer | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ⚙ | ❌ | ❌ | ✔ |
| Accuracy<sup>1</sup> | ⭐⭐⭐ | ⭐⭐⭐ | ⚙ | ⚙ | ⚙ | ⚙ | ⭐ | ⭐ | ⚙ |
| Speed<sup>2</sup> | ⚡⚡⚡ | ⚡⚡⚡ | ⚙ | ⚙ | ⚙ | ⚙ | ⚡ | ⚡ | ⚙ |
| Extensible to GRMHD | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ⚙ | ❌ | ❌ | ⚙ |
| Black Hole Shadow | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ⚙ | ✔<sup>#1<sup> | ✔<sup>#1<sup> | ⚙ |
| Accretion Disk & Flow | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ⚙ | ❌ | ✔<sup>#2<sup> | ⚙ |
| Redshift calculations | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ⚙ | ❌ | ❌ | ⚙ |
| Lensing simuation | ✔ | ✔ | ⚙ | ⚙ | ⚙ | ⚙ | ❌ | ✔<sup>#3<sup> | ⚙ |
| Approach | Semi-Analytical | Semi-Analytical |  |  |  | Numerical | Semi-Analytical | Analytical | ⚙ |
| Builds up on |  | `geokerr` |  |  |  | `geokerr` and other works here | [Interstellar (Movie)](https://www.imdb.com/title/tt0816692/) | [Interstellar (Movie)](https://www.imdb.com/title/tt0816692/) | ⚙ |
| Extra benefits |  |  |  |   |  | Recent, Works for arbitrary spacetimes, Adaptive integration step size | Good introduction to the problem | Nice wallpapers and gifs | ⚙ |

* <sup>1</sup> Relative accuracy (based on papers' own report)
  * highly accurate: ⭐⭐⭐
  * accurate: ⭐⭐
  * so-so: ⭐
* <sup>2</sup> Relative speed (based on papers' own report) | `FORTRAN > C/C++ > Python ~ MATLAB`, if no mention of speed in the paper
  * Very fast: ⚡⚡⚡
  * Fast: ⚡⚡
  * Slow: ⚡
* <sup>#1</sup> The shadow is not calculable. It's more of an initial condition.
* <sup>#2</sup> Artificially added.
* <sup>#3</sup> Not a simulation.



### (INITIAL) OUTLOOK:
* For Ray Tracing: Prefer `geokerr`, `YNOGK`, `RAPTOR`
* For Strong Gravity Simulations : Prefer `RAPTOR`, `BHAC`, `ARTIST`
* For Accretion Flow (GRMHD) : Prefer `ARTIST`
* For wallpapers & gifs : Prefer `starless` 😉

## Verbose Comparison

### Cases of interest are:
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
  * Useful for visualizing null trajectories
* **Cons**:
  * Simple model -> Does not consider radiative transfer
  * Useless for probing (getting physically relevant values out of) the integrated geodesics


### B. `geokerr` - Dexter et al (2009) - `G = c = M = 1`
* Written in `FORTRAN77` (yikes)
* Solves in Boyer-Lindquist Coordinates, provides transformations to Kerr-Schild Coordinates
* Works in Kerr Spacetime
* Hamiltonian Approach -> Requires an initial position and momentum
* Makes use of the conserved quanitites -> *Angular Momentum, L*, *Energy, E* and *Carter's Constant, Q*
* Uses Carlson's Elliptic Integrals to simplify algebraic manipulation -> Converts the integral computation into a root finding problem (or multiple root finding problems)
* Neglects plasma effects, scattering and absorption
* Integrates from observer to source
* Integration is piece-wise
* Considers thin disk accretion, based on an optically thin emission surface model
* Considers all cases of interest<sup>##</sup>
* Is generalized to `grtrans` (2016), that can handle polarized radiative transfer


* **Pros**:
  * At a minimum, "~3 to 5 times faster than" a simplistic numerical geodesic computation algorithm. Increases massively (~300 to ~500 times) for more complicated cases (All in `FORTRAN`). Real world implications against Python not considered, in this review.
  * Rapid and accurate geodesic calculations
  * Extensible to GRMHD simulations
  * Generalized to Polarized Radiative Transfer in a 2016 paper
* **Cons**:
  * FORTRAN77 implementation is difficult to understand
  * Requires knowledge of turning points, in advance
  * No adaptive meshing near the strong gravity regions (close to the Black Hole)


### C .`YNOGK` - Yang et al (2013) - `G = c = M = 1`
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
* Considers all cases of interest<sup>##</sup>

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


### D. `ODYSSEY` - Pu et al (2016)
* Written in `FORTRAN77` (yikes)
* 

* **Pros**:
  * 
* **Cons**:
  * 


### E. `ARTIST` - Takahashi et al (2017)
* Written in `FORTRAN77` (yikes)
* 

* **Pros**:
  * 
* **Cons**:
  * 


### F. `BHAC` - Porth et al (2017)
* Written in `FORTRAN77` (yikes)
* 

* **Pros**:
  * 
* **Cons**:
  * 


### G. `RAPTOR` - Bronzwaer et al (2018) - `G = c = 1`
* Written in `FORTRAN77` (yikes)
* Completely numerical
* General to all spacetimes -> May be extensible to binary BH systems, neutron stars and **expanding FRW spacetime**
* Automatically takes into account all gravitational effects
* CPU & GPU agnostic - GOOD GPU
* Minimal physical assumptions -> Supports arbitrary spacetimes & Time-Dependent Radiative Transfer 

* Presents implementation in RK4 (more accurate) and Velocity Verlet, with adaptive step size (slightly less accurate, but faster).
* Hamiltonian Approach -> Requires an initial position and momentum
* Makes use of the conserved quanitites -> *Angular Momentum, L*, *Energy, E* and *Carter's Constant, Q*
  
* Uses BL Coordinates, transforms to Kerr-Schild (KS) and Modified KS, when needed
* Supports OpenMP (CPU Multiprocessing) and OpenACC (GPU Multiprocessing)

* **Pros**:
  * Generalizable to other spacetimes
  * Adaptive step size helps with accuracy
  * Multiprocessing support
  * 
* **Cons**:


### H. `starless` - Riccardo Antonelli (~2 years ago)
* Uses Schwarschild Metric
* More of a hobbyist project, capable of producing some nice lensing effects on images
* Does perform geodesic integration, but doesn't seem useful for probing physical quantities
* Kudos for multiprocessing, though


### I. `grtrans` - Dexter et al (2016)
* 
* **Pros**:
  * 
* **Cons**:

## Comparison between Direct Numerical Integration & Analytical Elliptical Function approaches (EVOLVING)

**ONLY PROS MENTIONED**

| Direct Numerical Integration | Analytical Elliptical Function |
|:---:|:---:|
| Handles 3D accretion flow well | Analytical formula for 3D seems complex and computationally intensive to implement (can be partly overcome, though - `YNOGK`) |
| Simpler and faster for higher dimensions | Faster in most other computations |
| Slower, as each point on the geodesic has to be evaluated | Faster, as arbitrary sections of the geodesic can be computed |
| Mostly general to all spacetimes | Specific to particular spacetimes, where metric and connection are known |
| Less accurate | Spatial accuracy independent of integration step size |