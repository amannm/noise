# reversed(alongAxes:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns a new tensor with the specified dimensions reversed.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func reversed(alongAxes axes: Int...) -> MLTensor
```

### Parameters

- **`axes`**
  The indices of the dimensions to reverse. Must be in the range `[-rank, rank)`.

## Overview

A new tensor with the same shape and scalar type with the specified dimensions reversed.

For example:

```swift
let x = MLTensor(shape: [4], scalars: [0,  1,  2,  3], scalarType: Float.self)
let y = x.reversed(alongAxes: 0)
// [3, 2, 1, 0]
```

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
