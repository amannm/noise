# reshaped(to:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArraySlice](../mlshapedarrayslice.md)

---

Returns a new reshaped shaped array.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func reshaped(to newShape: [Int]) -> MLShapedArraySlice<Scalar>
```

### Parameters

- **`newShape`**
  The new shape after reshaping.

## Overview

The reshaped array gets scalars of the original array in first-major order. Therefore, the initializer is semantically equivalent to:

```swift
let reshaped = MLShapedArray(scalars: original.scalars, shape: newShape)
```

Usage example:

```swift
let original = MLShapedArraySlice<Int32>(scalars: 0..., shape: [4])
let reshaped = original.reshaped(to: [1, 2, 2])
```

A scalar can be reshaped to and from a shape where the product of dimensions is one.

The method raises a runtime error if the product of dimensions in the new shape is different from the current one.

## See Also

### Shaping the array slice

- [changingLayout(to:)](changinglayout(to:).md)
  Returns a copy with the specified buffer layout.

- [expandingShape(at:)](expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions

- [squeezingShape()](squeezingshape().md)
  Returns a new squeezed shaped array.

- [transposed()](transposed().md)
  Returns a new transposed shaped array

- [transposed(permutation:)](transposed(permutation:).md)
  Returns a new transposed shaped array using a custom permutation.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
