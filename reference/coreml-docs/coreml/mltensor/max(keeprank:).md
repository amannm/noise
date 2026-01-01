# max(keepRank:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns the maximum value in the array.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func max(keepRank: Bool = false) -> MLTensor
```

### Parameters

- **`keepRank`**
  A Boolean indicating whether to keep the reduced axes or not. The default value is `false`.

## Overview

The reduced tensor.

```swift
let x = MLTensor(shape: [3, 2], scalars: [2, 3, 4, 5, 6, 7], scalarType: Float.self)
let y = x.max()
y.shape // is []
await y.shapedArray(of: Float.self) // is [7.0]
```

## See Also

### Accessing the minimum, maximum and mean

- [min(alongAxes:keepRank:)](min(alongaxes:keeprank:).md)
  Returns the minimum values along the specified axes.

- [min(keepRank:)](min(keeprank:).md)
  Returns the minimum value in the array.

- [max(alongAxes:keepRank:)](max(alongaxes:keeprank:).md)
  Returns the maximum values along the specified axes.

- [mean(alongAxes:keepRank:)](mean(alongaxes:keeprank:).md)
  Returns the mean along the specified axes.

- [mean(keepRank:)](mean(keeprank:).md)
  Returns the mean along all axes.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
