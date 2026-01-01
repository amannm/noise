# sum(keepRank:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns the sum along all axes.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func sum(keepRank: Bool = false) -> MLTensor
```

### Parameters

- **`keepRank`**
  A Boolean indicating whether to keep the reduced axes or not. The default value is `false`.

## Overview

The reduced tensor.

For example:

```swift
let x = MLTensor(shape: [3, 2], scalars: [2, 3, 4, 5, 6, 7], scalarType: Float.self)
let y = x.sum()
y.shape // is []
await y.shapedArray(of: Float.self) // is [27]
```

## See Also

### Getting the sum

- [sum(alongAxes:keepRank:)](sum(alongaxes:keeprank:).md)
  Returns the sum along the specified axes.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
