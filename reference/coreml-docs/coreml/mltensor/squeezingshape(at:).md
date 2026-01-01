# squeezingShape(at:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Removes the specified dimensions of size 1 from the shape of the tensor.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func squeezingShape(at axes: Int...) -> MLTensor
```

### Parameters

- **`axes`**
  The axes to remove if the size is `1`.

## Overview

For example:

```swift
let x = MLTensor(shape: [1, 2, 1], scalars: [1, 2], scalarType: Float.self)
let y = x.squeezingShape(at: 0)
y.shape // is [2, 1]
```

## See Also

### Removing dimensions from the shape of the tensor

- [squeezingShape()](squeezingshape().md)
  Removes all dimensions of size 1 from the shape of the tensor.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
