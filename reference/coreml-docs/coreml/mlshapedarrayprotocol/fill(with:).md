# fill(with:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArrayProtocol](../mlshapedarrayprotocol.md)

---

Fills the array with a value.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
mutating func fill(with value: Self.Scalar)
```

### Parameters

- **`value`**
  The filling value

## See Also

### Modifying a shaped array type

- [withUnsafeMutableShapedBufferPointer(_:)](withunsafemutableshapedbufferpointer(_:).md)
  Provides read-write access of the shaped array’s underlying memory to a closure.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
