# withUnsafeMutableShapedBufferPointer(_:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArrayProtocol](../mlshapedarrayprotocol.md)

---

Provides read-write access of the shaped array’s underlying memory to a closure.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
mutating func withUnsafeMutableShapedBufferPointer<R>(_ body: (inout UnsafeMutableBufferPointer<Self.Scalar>, [Int], [Int]) throws -> R) rethrows -> R
```

### Parameters

- **`body`**
  A closure that accesses a shaped array’s underlying memory.

## Overview

The method returns the value your closure returns, if applicable.

## See Also

### Modifying a shaped array type

- [fill(with:)](fill(with:).md)
  Fills the array with a value.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
