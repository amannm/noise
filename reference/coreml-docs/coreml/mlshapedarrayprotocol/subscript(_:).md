# subscript(_:)

**Instance Subscript**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArrayProtocol](../mlshapedarrayprotocol.md)

---

A slice of the shaped array for the selected leading axes.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
subscript<C>(indices: C) -> MLShapedArraySlice<Self.Scalar> where C : Collection, C.Element == Int { get set }
```

### Parameters

- **`indices`**
  The indices to slice the array.

## Overview

The slice has a rank of `self.rank - indices.count`. For example, given a shaped array `m` with the shape being `3 x 3`, `m[[1]]` returns a slice of shape `[3]` with the contents labeld as `x` below.

```None
 O  O  O
 x  x  x
 O  O  O
```

## See Also

### Accessing elements

- [subscript(scalarAt:)](subscript(scalarat:).md)
  Accesses an element and a multidimensional location.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
