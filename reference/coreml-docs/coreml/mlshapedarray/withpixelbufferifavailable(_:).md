# withPixelBufferIfAvailable(_:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArray](../mlshapedarray.md)

---

Reads the underlying pixel buffer.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func withPixelBufferIfAvailable<R>(_ body: (CVPixelBuffer) throws -> R) rethrows -> R?
```

### Parameters

- **`body`**
  The closure to run with the pixel buffer.

## Overview

The value returned from body, unless the shaped array doesn’t use a pixel buffer backing, in which case the method ignores body and returns nil.

Use this method to read the contents of the underlying pixel buffer. The pixel buffer is read only. Do not write to it.

```swift
let array = MLShapedArray<Float16>(mutating: pixelBuffer, shape: [2, 3])
array.withPixelBuffer { backingPixelBuffer in
     // read backingPixelBuffer here.
}
```

## See Also

### Reading and writing the pixel buffer

- [withMutablePixelBufferIfAvailable(_:)](withmutablepixelbufferifavailable(_:).md)
  Writes to the underlying pixel buffer.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
