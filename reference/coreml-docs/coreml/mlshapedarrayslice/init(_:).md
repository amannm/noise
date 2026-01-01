# init(_:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArraySlice](../mlshapedarrayslice.md)

---

Creates a new MLShapedArraySlice using a `MLMultiArray` as a backing storage.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(_ multiArray: MLMultiArray)
```

### Parameters

- **`multiArray`**
  The `MLMultiArray` object.

## Overview

Use this initializer to access `MLMultiArray` through `MLShapedArray` interface.

Mutating operations trigger copy-on-write. Non-mutating operations access the `MLMultiArray`’s backing storage including the pixel buffer.

## See Also

### Creating a shaped array slice from another type

- [init(concatenating:alongAxis:)](init(concatenating:alongaxis:).md)
  Merges a sequence of shaped arrays into one shaped array along an axis.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
