# cumulativeSum(alongAxis:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Computes the cumulative sum along the specified axis.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func cumulativeSum(alongAxis axis: Int = 0) -> MLTensor
```

### Parameters

- **`axis`**
  The axis along which to perform the cumulative sum. The default value is `0`. Must be in the range `[-rank, rank)` and have a rank greater than zero.

## Overview

The result of the cumulative sum operation.

The scalar type of the tensor must be numeric.

For example:

```swift
MLTensor([1, 2, 3]).cumulativeSum() = [1, 1 + 2, 1 + 2 + 3]
```

## See Also

### Computing the cumulative value

- [cumulativeProduct(alongAxis:)](cumulativeproduct(alongaxis:).md)
  Computes the cumulative product along the specified axis.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
