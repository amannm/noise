# withUnsafeBytes(_:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 12.3+, tvOS 15.4+, visionOS 1.0+, watchOS 8.5+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

Calls a given closure with a raw pointer to the multiarray’s storage.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func withUnsafeBytes<R>(_ body: (UnsafeRawBufferPointer) throws -> R) rethrows -> R
```

### Parameters

- **`body`**
  A closure with an [UnsafeRawBufferPointer](https://developer.apple.com/documentation/Swift/UnsafeRawBufferPointer) parameter that points to the storage for the multiarray. This closure takes the following parameter:

  **`ptr`**
  The pointer to the buffer.


## See Also

### Providing buffer access

- [withUnsafeBufferPointer(ofType:_:)](withunsafebufferpointer(oftype:_:).md)
  Calls a given closure with a raw pointer to the multiarray’s storage.

- [withUnsafeMutableBufferPointer(ofType:_:)](withunsafemutablebufferpointer(oftype:_:).md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.

- [withUnsafeMutableBytes(_:)](withunsafemutablebytes(_:).md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
