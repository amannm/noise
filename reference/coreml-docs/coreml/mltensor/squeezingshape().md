# squeezingShape()

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Removes all dimensions of size 1 from the shape of the tensor.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func squeezingShape() -> MLTensor
```

## Overview

For example:

```swift
let x = MLTensor(shape: [1, 2, 1], scalars: [1, 2], scalarType: Float.self)
let y = x.squeezingShape()
y.shape // is [2]
```

## See Also

### Removing dimensions from the shape of the tensor

- [squeezingShape(at:)](squeezingshape(at:).md)
  Removes the specified dimensions of size 1 from the shape of the tensor.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
