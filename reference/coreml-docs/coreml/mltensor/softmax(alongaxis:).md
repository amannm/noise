# softmax(alongAxis:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Computes the softmax of the specified tensor along the specified axis.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func softmax(alongAxis axis: Int = -1) -> MLTensor
```

### Parameters

- **`axis`**
  The axis along which softmax will be computed.

## Overview

A new tensor with the same shape and scalar type.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
