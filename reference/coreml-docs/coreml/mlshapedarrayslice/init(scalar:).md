# init(scalar:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArraySlice](../mlshapedarrayslice.md)

---

Creates a shaped array slice with exactly one value and zero dimensions.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(scalar: Scalar)
```

### Parameters

- **`scalar`**
  A singular scalar value.

## See Also

### Creating a shaped array slice

- [init(scalars:shape:)](init(scalars:shape:).md)
  Initialize with a sequence and the shape.

- [init(mutating:shape:)](init(mutating:shape:).md)
  Creates a new `MLShapedArraySlice` using a pixel buffer as the backing storage.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
