# MLTensorRangeExpression

**Protocol**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A type that can be used to slice a dimension of a tensor. Don’t use this type directly.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
protocol MLTensorRangeExpression : Sendable
```

## Topics

### Expanding and squeezing the tensor

- [newAxis](mltensorrangeexpression/newaxis.md)
  Expand the tensor at the specified dimension.

- [squeezeAxis](mltensorrangeexpression/squeezeaxis.md)
  Squeeze the tensor at the specified dimension.

- [fillAll](mltensorrangeexpression/fillall.md)
  The same as the ellipsis literal `...` used to indicate unspecified dimensions of the tensor.

### Slicing the tensor

- [closedRange(_:stride:)](mltensorrangeexpression/closedrange(_:stride:).md)
  Slice the tensor at the specified dimension.

- [index(_:)](mltensorrangeexpression/index(_:).md)
  Slice the tensor at the specified dimension.

- [partialRangeFrom(_:stride:)](mltensorrangeexpression/partialrangefrom(_:stride:).md)
  Slice the tensor at the specified dimension.

- [partialRangeUpTo(_:stride:)](mltensorrangeexpression/partialrangeupto(_:stride:).md)
  Slice the tensor at the specified dimension.

- [range(_:stride:)](mltensorrangeexpression/range(_:stride:).md)
  Slice the tensor at the specified dimension.

## See Also

### Model tensor

- [MLTensor](mltensor.md)
  A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.

- [MLTensorScalar](mltensorscalar.md)
  A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.

- [pointwiseMin(_:_:)](pointwisemin(_:_:).md)
  Computes the element-wise minimum of two tensors.

- [pointwiseMax(_:_:)](pointwisemax(_:_:).md)
  Computes the element-wise minimum between two tensors.

- [withMLTensorComputePolicy(_:_:)](withmltensorcomputepolicy(_:_:).md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
