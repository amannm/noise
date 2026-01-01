# init(scalars:shape:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArray](../mlshapedarray.md)

---

Initialize with a sequence and the shape.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init<S>(scalars: S, shape: [Int]) where Scalar == S.Element, S : Sequence
```

### Parameters

- **`scalars`**
  The initializing sequence.

- **`shape`**
  The shape

## Overview

The length of the sequence must not be less than the number of scalars in the shaped array.

## See Also

### Creating a shaped array

- [init(scalar:)](init(scalar:).md)
  Creates a shaped array with exactly one value and zero dimensions.

- [init(mutating:shape:)](init(mutating:shape:).md)
  Creates a new `MLShapedArray` using a pixel buffer as the backing storage.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
