# transposed()

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Permutes the tensor with dimensions permuted in reverse order.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func transposed() -> MLTensor
```

## Overview

A permuted tensor.

For example:

```swift
let x = MLTensor(shape: [1, 2, 3], scalars: [1, 2, 3, 4, 5, 6], scalarType: Float.self)
let y = x.transposed()
y.shape // is [3, 2, 1]
```

## See Also

### Transposing the tensor

- [transposed(permutation:)](transposed(permutation:).md)
  Permutes the dimensions of the tensor in the specified order.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
