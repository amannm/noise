# bandPart(lowerBandCount:upperBandCount:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func bandPart(lowerBandCount: Int, upperBandCount: Int) -> MLTensor
```

### Parameters

- **`lowerBandCount`**
  The number of diagonals in the lower triangle to keep. If `-1`, keep the entire lower triangle.

- **`upperBandCount`**
  The number of diagonals in the upper triangle to keep. If `-1`, keep the entire upper triangle.

## Overview

The band part of the tensor.

The framework copies a diagonal band of values from the tensor to the result tensor of the same size. A coordinate `[..., i, j]` is considered in band if

```md
(lowerBandCount < 0 || (i-j) <= lowerBandCount) && (upperBandCount < 0 || (j-i) <= upperBandCount)
```

Values outside of the band are set to `0`.

For example:

```swift
let t = Tensor([
    [ 5,  1,  2, 3],
    [-1,  5,  1, 2],
    [-2, -1,  5, 1],
    [-3, -2, -1, 5]
], scalarType: Float.self)

t.bandPart(lowerBandCount: 0, upperBandCount: 0)
// [[ 5,  0,  0, 0]
//  [ 0,  5,  0, 0]
//  [ 0,  0,  5, 0]
//  [ 0,  0,  0, 5]]

t.bandPart(lowerBandCount: 0, upperBandCount: -1)
// [[ 5,  1,  2, 3]
//  [ 0,  5,  1, 2]
//  [ 0,  0,  5, 1]
//  [ 0,  0,  0, 5]]

t.bandPart(lowerBandCount: -1, upperBandCount: 0)
// [[ 5,  0,  0, 0]
//  [-1,  5,  0, 0]
//  [-2, -1,  5, 0]
//  [-3, -2, -1, 5]]
```

## See Also

### Accessing the extended tensor, sign and reciprocal

- [expandingShape(at:)](expandingshape(at:).md)
  Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.

- [tiled(multiples:)](tiled(multiples:).md)
  Returns a tensor by replicating its elements multiple times.

- [sign()](sign().md)
  Returns the sign of the tensor’s elements.

- [reciprocal()](reciprocal().md)
  Computes the reciprocal of the tensor’s elements.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
