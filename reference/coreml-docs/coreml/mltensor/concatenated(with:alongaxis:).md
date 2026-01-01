# concatenated(with:alongAxis:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Returns a concatenated tensor along the specified axis.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func concatenated(with other: MLTensor, alongAxis axis: Int = 0) -> MLTensor
```

### Parameters

- **`other`**
  The tensor to concatenate. The tensors must have the same dimensions, except for the specified axis.

- **`axis`**
  The axis along which to concatenate. Negative values wrap around but must be in the range `[-rank, rank)`.

## See Also

### Clamping and concatenating

- [clamped(to:)](clamped(to:).md)
  Clamps all elements to the given lower and upper bounds, inclusively.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
