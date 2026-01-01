# transposed(permutation:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Permutes the dimensions of the tensor in the specified order.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func transposed(permutation: Int...) -> MLTensor
```

### Parameters

- **`permutation`**
  An array of integers defining the permutation, must be of length `rank` and define a valid permutation.

## Overview

A permuted tensor.

For example:

```swift
let x = MLTensor(shape: [1, 2, 3], scalars: [1, 2, 3, 4, 5, 6], scalarType: Float.self)
let y = x.transposed(1, 0, 2)
y.shape // is [2, 1, 3]
```

## See Also

### Transposing the tensor

- [transposed()](transposed().md)
  Permutes the tensor with dimensions permuted in reverse order.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
