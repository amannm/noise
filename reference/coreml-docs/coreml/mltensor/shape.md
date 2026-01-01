# shape

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

The shape of the tensor.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var shape: [Int] { get }
```

## Overview

For example, 2 x 3 matrix may be represented as a tensor with the shape of `[2, 3]`.

## See Also

### Accessing tensor properties

- [isScalar](isscalar.md)
  A Boolean value indicating whether the tensor is a scalar (when the `rank` is equal to `0`) or not.

- [rank](rank.md)
  The number of dimensions of the tensor.

- [scalarCount](scalarcount.md)
  The number of scalar elements in the tensor.

- [scalarType](scalartype.md)
  The type of scalars in the tensor.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
