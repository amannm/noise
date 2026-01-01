# reshaped(to:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Reshape to the specified shape.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func reshaped(to newShape: [Int]) -> MLTensor
```

### Parameters

- **`newShape`**
  The new shape of the array. The number of scalars matches the new shape.

## Overview

For example:

```swift
let x = MLTensor(shape: [2], scalars: [1, 2], scalarType: Float.self)
let y = x.reshaped(at: [1, 2, 1])
y.shape // is [1, 2, 1]
```

## See Also

### Reshaping the tensor

- [flattened()](flattened().md)
  Reshape to a one-dimensional tensor.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
