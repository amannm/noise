# withUnsafeMutableBufferPointer(ofType:_:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 12.3+, tvOS 15.4+, visionOS 1.0+, watchOS 8.5+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

Calls a given closure with a raw pointer to the multiarray’s mutable storage.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func withUnsafeMutableBufferPointer<S, R>(ofType type: S.Type, _ body: (UnsafeMutableBufferPointer<S>, [Int]) throws -> R) rethrows -> R where S : MLShapedArrayScalar
```

### Parameters

- **`type`**
  The element type of the buffer passed in the body. This must be a Swift primitive type equivalent to `dataType`.

- **`body`**
  A closure with an [UnsafeMutableBufferPointer](https://developer.apple.com/documentation/Swift/UnsafeMutableBufferPointer) parameter that points to the storage for the multiarray and its strides. This closure takes the following parameters:

  **`ptr`**
  The pointer to the buffer.

  **`strides`**
  The strides of the buffer in scalars. Note that this may be different from `strides`’s value prior to this method invocation.


## Overview

The buffer contains a collection of `int32`, `float16`, `float32`, or `float64` values, depending on the multiarray’s data type. It may not store these scalar values contiguously; use `strides` to get the buffer layout.

## See Also

### Providing buffer access

- [withUnsafeBufferPointer(ofType:_:)](withunsafebufferpointer(oftype:_:).md)
  Calls a given closure with a raw pointer to the multiarray’s storage.

- [withUnsafeBytes(_:)](withunsafebytes(_:).md)
  Calls a given closure with a raw pointer to the multiarray’s storage.

- [withUnsafeMutableBytes(_:)](withunsafemutablebytes(_:).md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
