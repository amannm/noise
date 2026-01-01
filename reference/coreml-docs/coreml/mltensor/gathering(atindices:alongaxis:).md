# gathering(atIndices:alongAxis:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns a tensor by gathering slices along the given axis at the specified indices.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func gathering(atIndices indices: MLTensor, alongAxis axis: Int) -> MLTensor
```

### Parameters

- **`indices`**
  A 32-bit integer tensor containing indices to gather at.

- **`axis`**
  The dimension to gather along. Must be in the range `[-rank, rank)`.

## Overview

The gathered tensor.

For example:

```swift
let x = MLTensor(shape: [3, 3], scalars: [
     0,  1,  2,
    10, 11, 12,
    20, 21, 22
], scalarType: Float.self)
let i = MLTensor([2, 1], scalarType: Int32.self)
let y0 = x.gathering(atIndices: i)
// [[20, 21, 22],
//  [10, 11, 12]]

let y1 = x.gathering(atIndices: i, alongAxis: 1)
// [[ 2,  1],
//  [12, 11],
//  [22, 21]]
```

## See Also

### Gathering slices

- [gathering(atIndices:)](gathering(atindices:).md)
  Returns a tensor by gathering slices at the specified indices.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
