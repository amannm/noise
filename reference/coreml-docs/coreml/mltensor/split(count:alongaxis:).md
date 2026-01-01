# split(count:alongAxis:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Splits a tensor into multiple tensors. The tensor is split along dimension `axis` into `count` smaller tensors.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func split(count: Int, alongAxis axis: Int = 0) -> [MLTensor]
```

### Parameters

- **`count`**
  The number of splits to create, must divide the size of dimension `axis` evenly.

- **`axis`**
  The dimension along which to split this tensor. The `axis` must be in the range `[-rank, rank)`.

## Overview

An array containing the tensor parts.

For example:

```None
// 'value' is a tensor with shape [5, 30]
// Split 'value' into 3 tensors along dimension 1:
let parts = value.split(count: 3, alongAxis: 1)
parts[0] // has shape [5, 10]
parts[1] // has shape [5, 10]
parts[2] // has shape [5, 10]
```

## See Also

### Splitting the tensor

- [split(sizes:alongAxis:)](split(sizes:alongaxis:).md)
  Splits a tensor into multiple tensors. The tensor is split  into `sizes.shape[0]` parts.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
