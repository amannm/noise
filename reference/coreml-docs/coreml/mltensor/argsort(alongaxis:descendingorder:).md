# argsort(alongAxis:descendingOrder:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns the indices (or arguments) of a tensor that give its sorted order along the specified axis.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func argsort(alongAxis axis: Int = -1, descendingOrder: Bool = false) -> MLTensor
```

### Parameters

- **`axis`**
  The axis along which to sort. The default is `-1`, which sorts the last axis.

- **`descendingOrder`**
  A Boolean value that determines the sort order. The default is `false` which sorts from largest to least.

## Overview

A `Int32` tensor of sorted indices.

For example:

```swift
let x = MLTensor([1.0, 3.0, 2.0])
let y = x.argSort()
await y.shapedArray(of: Int32.self) // is [0, 2, 1]
```

## See Also

### Accessing the indicies

- [argmax()](argmax().md)
  Returns the index of the maximum value of the flattened scalars.

- [argmax(alongAxis:keepRank:)](argmax(alongaxis:keeprank:).md)
  Returns the indices of the maximum values along the specified axis.

- [argmin()](argmin().md)
  Returns the index of the minimum value of the flattened scalars.

- [argmin(alongAxis:keepRank:)](argmin(alongaxis:keeprank:).md)
  Returns the indices of the minimum values along the specified axis.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
