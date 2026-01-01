# clamped(to:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Clamps all elements to the given lower and upper bounds, inclusively.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func clamped(to bounds: ClosedRange<Float>) -> MLTensor
```

## Overview

For example:

```swift
let x = MLTensor([-1.0, 1.0, 2.0])
let y = x.clamped(to: 0...1)
await y.shapedArray(of: Float.self) // is [0.0, 1.0, 1.0]
```

## See Also

### Clamping and concatenating

- [concatenated(with:alongAxis:)](concatenated(with:alongaxis:).md)
  Returns a concatenated tensor along the specified axis.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
