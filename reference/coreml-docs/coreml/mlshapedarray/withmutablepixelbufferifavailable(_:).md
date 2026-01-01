# withMutablePixelBufferIfAvailable(_:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArray](../mlshapedarray.md)

---

Writes to the underlying pixel buffer.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
mutating func withMutablePixelBufferIfAvailable<R>(_ body: (CVPixelBuffer) throws -> R) rethrows -> R?
```

### Parameters

- **`body`**
  The closure to run with the pixel buffer.

## Overview

Use this method to writes the contents of the underlying pixel buffer.

```swift
let array = MLShapedArray<Float16>(mutating: pixelBuffer, shape: [2, 3])
array.withMutablePixelBuffer { backingPixelBuffer in
     // write backingPixelBuffer here.
}
```

## See Also

### Reading and writing the pixel buffer

- [withPixelBufferIfAvailable(_:)](withpixelbufferifavailable(_:).md)
  Reads the underlying pixel buffer.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
