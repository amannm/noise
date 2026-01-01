# withUnsafeBufferPointer(ofType:_:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 12.3+, tvOS 15.4+, visionOS 1.0+, watchOS 8.5+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

Calls a given closure with a raw pointer to the multiarray’s storage.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func withUnsafeBufferPointer<S, R>(ofType type: S.Type, _ body: (UnsafeBufferPointer<S>) throws -> R) rethrows -> R where S : MLShapedArrayScalar
```

### Parameters

- **`type`**
  The element type of the buffer passed in the body. This must be a Swift primitive type equivalent to `dataType`. This closure takes the following parameter:

  **`ptr`**
  The pointer to the buffer.


- **`body`**
  A closure with an [UnsafeBufferPointer](https://developer.apple.com/documentation/Swift/UnsafeBufferPointer) parameter that points to the storage for the multiarray.

## Overview

The buffer contains a collection of `int32`, `float16`, `float32`, or `float64` values, depending on the multiarray’s data type. It may not store these scalar values contiguously; use [strides](strides.md) to get the buffer layout.

## See Also

### Providing buffer access

- [withUnsafeBytes(_:)](withunsafebytes(_:).md)
  Calls a given closure with a raw pointer to the multiarray’s storage.

- [withUnsafeMutableBufferPointer(ofType:_:)](withunsafemutablebufferpointer(oftype:_:).md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.

- [withUnsafeMutableBytes(_:)](withunsafemutablebytes(_:).md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
