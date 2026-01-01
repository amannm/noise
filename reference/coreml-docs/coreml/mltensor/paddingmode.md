# MLTensor.PaddingMode

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

A mode that dictates how a tensor is padded.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum PaddingMode
```

## Topics

### Padding modes

- [MLTensor.PaddingMode.constant(_:)](paddingmode/constant(_:).md)
  Pads the input tensor boundaries with a constant value.

- [MLTensor.PaddingMode.reflection](paddingmode/reflection.md)
  Pads the input tensor using the reflection of the input boundary.

- [MLTensor.PaddingMode.symmetric](paddingmode/symmetric.md)
  Pads the input tensor using the reflection of the input, including the edge value.

## See Also

### Padding the tensor

- [padded(forSizes:mode:)](padded(forsizes:mode:).md)
  Returns a padded tensor according to the specified padding sizes and mode.

- [padded(forSizes:with:)](padded(forsizes:with:).md)
  Returns a tensor padded with the given constant according to the specified padding sizes.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
