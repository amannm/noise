# isScalar

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

A Boolean value indicating whether the tensor is a scalar (when the `rank` is equal to `0`) or not.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var isScalar: Bool { get }
```

## See Also

### Accessing tensor properties

- [rank](rank.md)
  The number of dimensions of the tensor.

- [scalarCount](scalarcount.md)
  The number of scalar elements in the tensor.

- [scalarType](scalartype.md)
  The type of scalars in the tensor.

- [shape](shape.md)
  The shape of the tensor.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
