# squeezingShape()

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArray](../mlshapedarray.md)

---

Returns a new squeezed shaped array.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func squeezingShape() -> MLShapedArray<Scalar>
```

## Overview

The new shape removes 1s in the original shape.

```swift
let original = MLShapedArray<Int32>(scalars: 0..., shape: [1, 2, 1, 2])
let squeezed = original.squeezingShape()
squeezed.shape // [2, 2]
```

When all the dimensions of the original shape is one, the resultant shaped array is a scalar.

```swift
let original = MLShapedArray<Int32>(scalars: 42, shape: [1, 1])
let squeezed = original.squeezingShape()
squeezed.scalar // 42
```

## See Also

### Shaping the array

- [changingLayout(to:)](changinglayout(to:).md)
  Returns a copy with the specified buffer layout.

- [expandingShape(at:)](expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions.

- [reshaped(to:)](reshaped(to:).md)
  Returns a new reshaped shaped array.

- [transposed()](transposed().md)
  Returns a new transposed shaped array.

- [transposed(permutation:)](transposed(permutation:).md)
  Returns a transposed shaped array using a custom permutation.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
