# expandingShape(at:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func expandingShape(at axes: Int...) -> MLTensor
```

### Parameters

- **`axes`**
  The axes at which to expand the shape.

## Overview

For example:

```swift
let x = MLTensor(shape: [2], scalars: [1, 2], scalarType: Float.self)
let y = x.expandingShape(at: 0)
y.shape // is [1, 2]
```

## See Also

### Accessing the extended tensor, sign and reciprocal

- [bandPart(lowerBandCount:upperBandCount:)](bandpart(lowerbandcount:upperbandcount:).md)
  Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.

- [tiled(multiples:)](tiled(multiples:).md)
  Returns a tensor by replicating its elements multiple times.

- [sign()](sign().md)
  Returns the sign of the tensor’s elements.

- [reciprocal()](reciprocal().md)
  Computes the reciprocal of the tensor’s elements.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
