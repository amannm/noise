# init(imageAtURL:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLFeatureValue](../mlfeaturevalue.md)

---

Creates a feature value that contains an image defined by an image URL and the image’s orientation, size, and pixel format.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(imageAtURL url: URL, orientation: CGImagePropertyOrientation, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]? = nil) throws
```

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(imageAt url: URL, orientation: CGImagePropertyOrientation, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]? = nil) throws
```

### Parameters

- **`url`**
  A [URL](https://developer.apple.com/documentation/Foundation/URL) (Swift) or [NSURL](https://developer.apple.com/documentation/Foundation/NSURL) (Objective-C) to an image.

- **`orientation`**
  A [CGImagePropertyOrientation](https://developer.apple.com/documentation/ImageIO/CGImagePropertyOrientation) instance.

- **`pixelsWide`**
  The image’s width in pixels.

- **`pixelsHigh`**
  The image’s height in pixels.

- **`pixelFormatType`**
  The image’s pixel format (see [Pixel Format Identifiers](https://developer.apple.com/documentation/CoreVideo/pixel-format-identifiers)).

- **`options`**
  A dictionary of [VNImageCropAndScaleOption](https://developer.apple.com/documentation/Vision/VNImageCropAndScaleOption) values, each keyed by [MLFeatureValue.ImageOption](imageoption.md).

## See Also

### Creating image feature values

- [init(pixelBuffer:)](init(pixelbuffer:).md)
  Creates a feature value that contains an image from a pixel buffer.

- [init(CGImage:pixelsWide:pixelsHigh:pixelFormatType:options:)](init(cgimage:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and its size and pixel format.

- [init(CGImage:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:)](init(cgimage:orientation:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and its orientation, size, and pixel format.

- [init(CGImage:constraint:options:)](init(cgimage:constraint:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and a constraint.

- [init(CGImage:orientation:constraint:options:)](init(cgimage:orientation:constraint:options:).md)
  Creates a feature value that contains an image defined by a core graphics image, an orientation, and a constraint.

- [init(imageAtURL:pixelsWide:pixelsHigh:pixelFormatType:options:)](init(imageaturl:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by an image URL and the image’s size and pixel format.

- [init(imageAtURL:constraint:options:)](init(imageaturl:constraint:options:).md)
  Creates a feature value that contains an image defined by an image URL and a constraint.

- [init(imageAtURL:orientation:constraint:options:)](init(imageaturl:orientation:constraint:options:).md)
  Creates a feature value that contains an image defined by an image URL, an orientation, and a constraint.

- [MLImageConstraint](../mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.

- [MLFeatureValue.ImageOption](imageoption.md)
  The initializer options you use to crop and scale an image when creating an image feature value.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
