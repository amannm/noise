# all(alongAxes:keepRank:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Computes logical AND on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func all(alongAxes axes: Int..., keepRank: Bool = false) -> MLTensor
```

### Parameters

- **`axes`**
  The axes to reduce.

- **`keepRank`**
  A Boolean indicating whether to keep the reduced axes or not. The default value is `false`.

## Overview

The reduced Boolean tensor.

## See Also

### Performing a logical AND operation

- [all(keepRank:)](all(keeprank:).md)
  Computes logical AND on elements across all axes of a tensor where the scalar type of the tensor is expected to be Boolean.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
