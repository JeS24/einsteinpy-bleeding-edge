# Repository to store my research into implementing Null Geodesics in einsteinpy

The Literature Review can be found in [`review.md`](https://github.com/JeS24/einsteinpy-bleeding-edge/blob/master/review.md). Corresponding .PDFs of the papers can be found in [`./Papers (Non-Annotated)`](https://github.com/JeS24/einsteinpy-bleeding-edge/tree/master/Papers%20(Non-Annotated)). Code implemenatations (if any) are present in [`./Code Implementations`](https://github.com/JeS24/einsteinpy-bleeding-edge/tree/master/Code%20Implementations). *Please bring any mistakes to my attention. Thanks.*

## Plan
1. Read the papers and make a comparison table. (Check [`review.md`](https://github.com/JeS24/einsteinpy-bleeding-edge/blob/master/review.md) for this)
2. Explore the software/code (if any). (Look into [`./Code Implementations`](https://github.com/JeS24/einsteinpy-bleeding-edge/tree/master/Code%20Implementations) for this)
3. Check the math in the most suitable papers.
4. Assess conversion (from paper) to code viability (in terms of math complexity et al)

### Detailed plan (after including the considerations below)

1. Implement a Numerical Geodesic Integrator (1 photon)
   1. Will use one of: `RAPTOR`, `GRay2`, `EHT`/`Odyssey`
   2. Unit interconversion module, if needed
2. Find out a way to parallelize it on CPU for a photon sheet
   1. Make use of `numba`
3. Look for GRMHD packages, that allow model exports of the environment around a black hole for accretion flow simulations
   1. `HARM`, `BHAC`, `ARTIST`
   2. Based on `GRay2`'s implementation
4. Implement bridging modules (from/to those packages)
5. Implement:
   1. Photon Red-shift
   2. BH Shadow
   3. Keplerian Disk
   4. Lensing

## Important issues, that will determine the development of the module:

| Issue | Notes | Resolution | 
|:---:|:---:|:---:|
| SI vs Geom Units or a separate unit conversion module | Geom is a necessity due to precision constraints | Use `astropy.units` for tracking units. We can have an interconversion module, but all calculations will be done in Geometric units. |
| Numerical Integration vs (Semi-)Analytical Approach | [Check `review.md` for a comparison](https://github.com/JeS24/einsteinpy-bleeding-edge/blob/master/review.md#comparison-between-numerical-integration--analytical-approaches-elliptical-functions---) | For future extensibility (to other spacetimes), it's better to go the Numerical Route à la `RAPTOR`. |
| General Geodesic Integrator or Specific to certain spacetimes, like Kerr or Schwarzschild | Related to the aforementioned point | See above. |
| Wrappers vs Pure Python implementation | Wrappers are more efficient. OpenCL or CUDA may alleviate this issue somewhat. | Pure python + `Numba`. `cuPy`, if needed. See [below](https://github.com/JeS24/einsteinpy-bleeding-edge/blob/master/README.md#parallel-computing).
| CPU vs GPU | Related to the aforementioned point. Pushing hard with GPU support will render the module sluggish on most machines, at best. In Computational GR community, this may not be a major issue. | Agnostic, as far as possible. See above. |
| Fast vs Slow Light Paradigm | Discussed under Time Dependent Radiative Transfer. "Slow light" implies many more calculations per timestep. Much higher memory and processing overhead. But "slow light" leads to much more realistic results too. | Prefer model exports from existing GRMHD packages, like `GRay2`, or can put slow-light as a feature request for future. |
| GRMHD pluggability vs Self-Contained Package | We can make EPY support exported plasma models from pre-existing GRMHD softwares, like `HARM`, `BHAC` et cetera, or we can implement their functionality ourselves. | See above. |


#### Parallel Computing
Check [here (Python Wiki)](https://wiki.python.org/moin/ParallelProcessing) and [here (SE)](https://scicomp.stackexchange.com/questions/19586/parallelizing-a-for-loop-in-python?rq=1).

We'll go with `numba`. `cuPy` can be used later on, if `numba` optimizations are insufficient.

Based on the following factors (in decreasing orders of importance):
1. Relevance to our usecase
2. Installation/maintenance overheads
3. Code complexity
4. Machine-specificity/Code portability
```
Numba > dask > joblib > threading == multiprocessing

cupy > pyOpenCL == pyCUDA 
```