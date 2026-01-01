# sign()

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns the sign of the tensor’s elements.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func sign() -> MLTensor
```

## Overview

This operation returns `1.0` if the correspnding element is greater than `0`, `-1.0` if it is less than `0`, `-0.0` if it is equal to `-0.0`, and `+0.0` if it is equal to `+0.0`.

## See Also

### Accessing the extended tensor, sign and reciprocal

- [expandingShape(at:)](expandingshape(at:).md)
  Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.

- [bandPart(lowerBandCount:upperBandCount:)](bandpart(lowerbandcount:upperbandcount:).md)
  Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.

- [tiled(multiples:)](tiled(multiples:).md)
  Returns a tensor by replicating its elements multiple times.

- [reciprocal()](reciprocal().md)
  Computes the reciprocal of the tensor’s elements.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
