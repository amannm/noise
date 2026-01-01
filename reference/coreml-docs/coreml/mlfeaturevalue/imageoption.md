# MLFeatureValue.ImageOption

**Structure**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLFeatureValue](../mlfeaturevalue.md)

---

The initializer options you use to crop and scale an image when creating an image feature value.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
struct ImageOption
```

## Topics

### Image options keys

- [cropRect](imageoption/croprect.md)
  The option you use to crop an image when creating an image feature value.

- [cropAndScale](imageoption/cropandscale.md)
  The option you use to crop and scale an image when creating an image feature value.

### Image option key initializers

- [init(_:)](imageoption/init(_:).md)
  Creates an image feature option key from a string.

- [init(rawValue:)](imageoption/init(rawvalue:).md)
  Creates an image feature option key from a raw value string.

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

- [init(imageAtURL:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:)](init(imageaturl:orientation:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by an image URL and the image’s orientation, size, and pixel format.

- [init(imageAtURL:constraint:options:)](init(imageaturl:constraint:options:).md)
  Creates a feature value that contains an image defined by an image URL and a constraint.

- [init(imageAtURL:orientation:constraint:options:)](init(imageaturl:orientation:constraint:options:).md)
  Creates a feature value that contains an image defined by an image URL, an orientation, and a constraint.

- [MLImageConstraint](../mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
