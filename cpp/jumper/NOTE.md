# Rabbit jumper
To predict the probability of each ended node being jumped to. \
Actually we could compute the `n_parent` to know who's the root, however, we just skip that procedure here.

## Topic
### Graph
- construct adjencency list
- BFS
### Test
- assertion
- comparision between float: use `fabs`
- type assertion with template: use `static_assert`, `is_arithmetic`
### CMake
- use `add_definitions("-DXXX ")` to add flags for preprocessor

## Caution
- Use template to handle implicit double conversion
- Deallocate unused memory to prevent segmentation fault.

## Reference
[Graph implementation using C++ STL](https://www.techiedelight.com/graph-implementation-using-stl/)