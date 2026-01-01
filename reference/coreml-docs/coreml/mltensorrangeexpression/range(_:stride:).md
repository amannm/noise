# range(_:stride:)

**Type Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensorRangeExpression](../mltensorrangeexpression.md)

---

Slice the tensor at the specified dimension.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
static func range(_ range: Range<Int>, stride: Int = 1) -> any MLTensorRangeExpression
```

## Overview

```swift
let x = MLTensor(randomNormal: [1, 3, 28, 28], scalarType: Float.self)
let y = x[..., 0..<2] // or x[..., .range(0..<2, stride: 1)]
y.shape // is [1, 3, 28, 2]
```

## See Also

### Slicing the tensor

- [closedRange(_:stride:)](closedrange(_:stride:).md)
  Slice the tensor at the specified dimension.

- [index(_:)](index(_:).md)
  Slice the tensor at the specified dimension.

- [partialRangeFrom(_:stride:)](partialrangefrom(_:stride:).md)
  Slice the tensor at the specified dimension.

- [partialRangeUpTo(_:stride:)](partialrangeupto(_:stride:).md)
  Slice the tensor at the specified dimension.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
