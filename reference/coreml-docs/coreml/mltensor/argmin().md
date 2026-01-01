# argmin()

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns the index of the minimum value of the flattened scalars.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func argmin() -> MLTensor
```

## Overview

```swift
let x = MLTensor(shape: [3, 2], scalars: [2, 3, 4, 5, 6, 7], scalarType: Float.self)
let y = x.argmin()
y.shape // is []
y.scalarType // is Int32
await y.shapedArray(of: Int32.self) // is 0
```

## See Also

### Accessing the indicies

- [argmax()](argmax().md)
  Returns the index of the maximum value of the flattened scalars.

- [argmax(alongAxis:keepRank:)](argmax(alongaxis:keeprank:).md)
  Returns the indices of the maximum values along the specified axis.

- [argmin(alongAxis:keepRank:)](argmin(alongaxis:keeprank:).md)
  Returns the indices of the minimum values along the specified axis.

- [argsort(alongAxis:descendingOrder:)](argsort(alongaxis:descendingorder:).md)
  Returns the indices (or arguments) of a tensor that give its sorted order along the specified axis.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
