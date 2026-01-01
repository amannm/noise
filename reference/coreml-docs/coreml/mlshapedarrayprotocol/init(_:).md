# init(_:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArrayProtocol](../mlshapedarrayprotocol.md)

---

Creates a shaped array type from a multiarray.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(_ multiArray: MLMultiArray)
```

### Parameters

- **`multiArray`**
  An [MLMultiArray](../mlmultiarray.md) with the same underlying type as the shaped array type.

## See Also

### Creating a shaped array type from another type

- [init(converting:)](init(converting:).md)
  Initialize by converting a MLMultiArray of different scalar type.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
