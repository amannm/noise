# subscript(scalarAt:)

**Instance Subscript**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArrayProtocol](../mlshapedarrayprotocol.md)

---

Accesses an element and a multidimensional location.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
subscript<C>(scalarAt indices: C) -> Self.Scalar where C : Collection, C.Element == Int { get set }
```

### Parameters

- **`indices`**
  An integer collection that represents a position in the shaped array in which each integer is an index in the corresponding dimension.

## See Also

### Accessing elements

- [subscript(_:)](subscript(_:).md)
  A slice of the shaped array for the selected leading axes.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
