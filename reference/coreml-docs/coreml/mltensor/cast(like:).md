# cast(like:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Casts the elements of the tensor to the scalar type of the given array.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func cast(like other: MLTensor) -> MLTensor
```

### Parameters

- **`other`**
  The other tensor whose scalar type is used for the cast.

## Overview

A new tensor with its contents cast to the scalar type of `other`.

For example:

```swift
let x = MLTensor([1, 2, 3], scalarType: Float.self)
let y = MLTensor([1, 2, 3], scalarType: Int32.self)
let z = y.cast(like: x)
z.scalarType // is Float
```

## See Also

### Casting the elements

- [cast(to:)](cast(to:).md)
  Casts the elements of the tensor to the given scalar type.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
