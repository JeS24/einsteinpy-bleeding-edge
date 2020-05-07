# Repository to store my research into implementing Null Geodesics in einsteinpy

The Literature Review can be found in `review.md`. Corresponding .PDFs of the papers can be found in `./Papers (Non-Annotated)`. Code implemenatations (if any) are present in `./Code Implementations`. *Please bring any mistakes to my attention. Thanks.*

## Plan:
1. Read the papers and make a comparison table. (Check `review.md` for this)
2. Explore the software/code (if any). (Look into `./Code Implementations` for this)
3. Check the math in the most suitable papers.
4. Assess conversion (from paper) to code viability (in terms of math complexity et al)

## Important issues, that will determine the development of the module:

| Issue | Notes |
|:---:|:---:|
| Numerical Integration vs (Semi-)Analytical Approach | [Check `review.md` for a comparison]() |
| General Geodesic Integrator or Specific to certain spacetimes, like Kerr or Schwarzschild | Related to the aforementioned point |
| Wrappers vs Pure Python implementation | Wrappers are more efficient. OpenCL or CUDA may alleviate this issue somewhat. |
| CPU vs GPU | Related to the aforementioned point. Pushing hard with GPU support will render the module sluggish on most machines, at best. In Computational GR community, this may not be a major issue. |
| Fast vs Slow Light Paradigm | Discussed under Time Dependent Radiative Transfer. "Slow light" implies many more calculations per timestep. Much higher memory and processing overhead. But "slow light" leads to much more realistic results too. |
| GRMHD pluggability vs Self-Contained Package | We can make EPY support exported plasma models from pre-existing GRMHD softwares, like `HARM`, `BHAC` et cetera, or we can implement their functionality ourselves. |