# shapedArray(of:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns a materialized representation of the tensor.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func shapedArray<Scalar>(of scalarType: Scalar.Type) async -> MLShapedArray<Scalar> where Scalar : MLShapedArrayScalar, Scalar : MLTensorScalar
```

## Overview

A `MLShapedArray` with the contents of the tensor.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
