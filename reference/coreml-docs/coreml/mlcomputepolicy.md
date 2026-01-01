# MLComputePolicy

**Structure**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

The compute policy determining what compute device, or compute devices, to execute ML workloads on.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
struct MLComputePolicy
```

## Topics

### Compute policies

- [cpuAndGPU](mlcomputepolicy/cpuandgpu.md)
  Execute ML workloads using the GPU if available, otherwise falling back to the CPU.

- [cpuOnly](mlcomputepolicy/cpuonly.md)
  Execute ML workloads using the CPU.

### Creating a compute policy

- [init(_:)](mlcomputepolicy/init(_:).md)
  Creates a new compute policy using the given compute units.

### Default Implementations

- [CustomReflectable Implementations](mlcomputepolicy/customreflectable-implementations.md)

- [CustomStringConvertible Implementations](mlcomputepolicy/customstringconvertible-implementations.md)

## See Also

### Compute plan

- [MLComputePlan](mlcomputeplan-1w21n.md)
  A class representing the compute plan of a model.

- [MLModelStructure](mlmodelstructure-swift.enum.md)
  An enum representing the structure of a model.

- [withMLTensorComputePolicy(_:_:)](withmltensorcomputepolicy(_:_:)-8stx9.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

- [withMLTensorComputePolicy(_:_:)](withmltensorcomputepolicy(_:_:)-6z33x.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
