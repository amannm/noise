# transposed()

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArraySlice](../mlshapedarrayslice.md)

---

Returns a new transposed shaped array

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func transposed() -> MLShapedArraySlice<Scalar>
```

## Overview

This is equivalent to `transposed(permutation:)` where `permutation:` parameter is `[shape.count-1, shape.count-2, ..., 0]`, which reverses the shape.

```swift
let original = MLShapedArraySlice<Int32>(scalars: 0..., shape: [1, 2, 3])
let transposed = original.transposed()
transposed.shape // [3, 2, 1]
```

## See Also

### Shaping the array slice

- [changingLayout(to:)](changinglayout(to:).md)
  Returns a copy with the specified buffer layout.

- [expandingShape(at:)](expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions

- [reshaped(to:)](reshaped(to:).md)
  Returns a new reshaped shaped array.

- [squeezingShape()](squeezingshape().md)
  Returns a new squeezed shaped array.

- [transposed(permutation:)](transposed(permutation:).md)
  Returns a new transposed shaped array using a custom permutation.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
