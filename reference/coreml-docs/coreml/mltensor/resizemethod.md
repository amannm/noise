# MLTensor.ResizeMethod

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

A resize algorithm.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum ResizeMethod
```

## Topics

### Resize methods

- [MLTensor.ResizeMethod.bilinear(alignCorners:)](resizemethod/bilinear(aligncorners:).md)
  The bilinear interpolation mode where values are computed using bilinear interpolation of 4 neighboring pixels.

- [MLTensor.ResizeMethod.nearestNeighbor](resizemethod/nearestneighbor.md)
  The nearest interpolation mode where values are interpolated using the closest neighbor pixel.

## See Also

### Resizing the tensor

- [resized(to:method:)](resized(to:method:).md)
  Resize the tensor’s spatial dimensions to size using the specified method.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
