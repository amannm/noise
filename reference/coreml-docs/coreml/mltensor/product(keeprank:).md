# product(keepRank:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns the product along all axes.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func product(keepRank: Bool = false) -> MLTensor
```

### Parameters

- **`keepRank`**
  A Boolean indicating whether to keep the reduced axes or not. The default value is `false`.

## Overview

The reduced tensor.

```swift
let x = MLTensor(shape: [3, 2], scalars: [2, 3, 4, 5, 6, 7], scalarType: Float.self)
let y = x.product()
y.shape // is []
await y.shapedArray(of: Float.self) // is [5040.0]
```

## See Also

### Accessing the product along an axes

- [product(alongAxes:keepRank:)](product(alongaxes:keeprank:).md)
  Returns the product along the specified axes.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
