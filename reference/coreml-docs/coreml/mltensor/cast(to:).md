# cast(to:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Casts the elements of the tensor to the given scalar type.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func cast<Scalar>(to scalarType: Scalar.Type) -> MLTensor where Scalar : MLTensorScalar
```

### Parameters

- **`scalarType`**
  The destination scalar type.

## Overview

A new tensor with its contents cast to the given scalar type.

For example:

```swift
let x = MLTensor([1, 2, 3], scalarType: Int32.self)
let y = x.cast(to: Float.self)
y.scalarType // is Float
```

## See Also

### Casting the elements

- [cast(like:)](cast(like:).md)
  Casts the elements of the tensor to the scalar type of the given array.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
