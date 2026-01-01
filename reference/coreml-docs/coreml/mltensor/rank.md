# rank

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

The number of dimensions of the tensor.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var rank: Int { get }
```

## Overview

Rank is equal to the number of dimensions of the shape, i.e., `tensor.rank == tensor.shape.count`.

## See Also

### Accessing tensor properties

- [isScalar](isscalar.md)
  A Boolean value indicating whether the tensor is a scalar (when the `rank` is equal to `0`) or not.

- [scalarCount](scalarcount.md)
  The number of scalar elements in the tensor.

- [scalarType](scalartype.md)
  The type of scalars in the tensor.

- [shape](shape.md)
  The shape of the tensor.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
