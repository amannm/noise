# changingLayout(to:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArray](../mlshapedarray.md)

---

Returns a copy with the specified buffer layout.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func changingLayout(to bufferLayout: MLShapedArrayBufferLayout) -> MLShapedArray<Scalar>
```

### Parameters

- **`bufferLayout`**
  The desired buffer layout.

## Overview

The returned shaped array will have `.strides` property according to the requested layout.

The function may return a heap-memory backed shaped array even if `self` is backed by a pixel buffer.

```swift
let source = MLShapedArray<Int32>(scalars: 0..., shape: [2, 2])

// Returns a new MLShapedArray with the specified strides.
_ = source.changingLayout(to: .custom(strides: [4, 1]))

// Returns a new MLShapedArray with the first-major contiguous layout.
_ = source.changingLayout(to: .firstMajorContiguous)

// Returns a new MLShapedArray with the last-major contiguous layout.
_ = source.changingLayout(to: .lastMajorContiguous)
```

The `withUnsafeShapedBufferPointer` function provides read-only access to the underlying buffer of the layout.

The `withUnsafeMutableShapedBufferPointer(body:)` function may provide a buffer of different layout due to copy-on-write. Use `withUnsafeMutableShapedBufferPointer(bufferLayout:body:)` if you need a specific buffer layout.

It raises a precondition error if the custom strides and the shape have different ranks.

## See Also

### Shaping the array

- [expandingShape(at:)](expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions.

- [reshaped(to:)](reshaped(to:).md)
  Returns a new reshaped shaped array.

- [squeezingShape()](squeezingshape().md)
  Returns a new squeezed shaped array.

- [transposed()](transposed().md)
  Returns a new transposed shaped array.

- [transposed(permutation:)](transposed(permutation:).md)
  Returns a transposed shaped array using a custom permutation.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
