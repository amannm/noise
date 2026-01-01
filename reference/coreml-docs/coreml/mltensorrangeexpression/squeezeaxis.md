# squeezeAxis

**Type Property**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensorRangeExpression](../mltensorrangeexpression.md)

---

Squeeze the tensor at the specified dimension.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
static var squeezeAxis: any MLTensorRangeExpression { get }
```

## Overview

For example:

```swift
let x = MLTensor(randomNormal: [1, 3, 28, 28], scalarType: Float.self)
let y = x[.squeezeAxis, ...]
y.shape // is [3, 28, 28]
```

## See Also

### Expanding and squeezing the tensor

- [newAxis](newaxis.md)
  Expand the tensor at the specified dimension.

- [fillAll](fillall.md)
  The same as the ellipsis literal `...` used to indicate unspecified dimensions of the tensor.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
