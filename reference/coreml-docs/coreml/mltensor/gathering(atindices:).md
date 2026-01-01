# gathering(atIndices:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns a tensor by gathering slices at the specified indices.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func gathering(atIndices indices: MLTensor) -> MLTensor
```

### Parameters

- **`indices`**
  A 32-bit integer tensor containing indices to gather at.

## Overview

The gathered tensor.

The `indices` tensor is interpreted as a `(rank-1)` dimensional set of one-dimensional lookup vectors, for example:

```swift
let x = MLTensor(shape: [2, 2], scalars: [
    0,  1,
    10, 11
], scalarType: Float.self)
let i = MLTensor(shape: [2, 2], scalars: [
    0, 0,
    1, 1
], scalarType: Int32.self)
let y = x.gathering(atIndices: i)
// [ 0, 11]
```

If the one-dimensional lookup vectors do not give a full set of indices, the remaining indices are treated as a slice, for example:

```swift
let x = MLTensor(shape: [3, 3], scalars: [
    0,  1,  2,
    10, 11, 12,
    20, 21, 22
], scalarType: Float.self)
let i = MLTensor(shape: [3, 1], scalars: [
    2,
    1
], scalarType: Int32.self)
let y = x.gathering(atIndices: i)
// [[20 21 22]
//  [10 11 12]]
```

## See Also

### Gathering slices

- [gathering(atIndices:alongAxis:)](gathering(atindices:alongaxis:).md)
  Returns a tensor by gathering slices along the given axis at the specified indices.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
