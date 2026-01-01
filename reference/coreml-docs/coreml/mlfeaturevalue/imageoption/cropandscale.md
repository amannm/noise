# cropAndScale

**Type Property**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../../coreml.md) > [MLFeatureValue](../../mlfeaturevalue.md) > [MLFeatureValue.ImageOption](../imageoption.md)

---

The option you use to crop and scale an image when creating an image feature value.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
static let cropAndScale: MLFeatureValue.ImageOption
```

## Overview

Use this value as a dictionary key for the `options` argument of an image-based `MLFeatureValue` initializer. Pair this key with a [VNImageCropAndScaleOption](https://developer.apple.com/documentation/Vision/VNImageCropAndScaleOption) value in the initializer’s `options` dictionary. For example, see [init(CGImage:pixelsWide:pixelsHigh:pixelFormatType:options:)](../init(cgimage:pixelswide:pixelshigh:pixelformattype:options:).md).

## See Also

### Image options keys

- [cropRect](croprect.md)
  The option you use to crop an image when creating an image feature value.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
