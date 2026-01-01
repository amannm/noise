# flattened()

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Reshape to a one-dimensional tensor.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func flattened() -> MLTensor
```

## Overview

> **Note**
> Flattening a zero-dimensional tensor will return a one-dimensional tensor.

For example:

```swift
let x = MLTensor(shape: [2, 2], scalars: [1, 2, 3, 4], scalarType: Float.self)
let y = x.flattened()
y.shape // is [4]
```

## See Also

### Reshaping the tensor

- [reshaped(to:)](reshaped(to:).md)
  Reshape to the specified shape.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
