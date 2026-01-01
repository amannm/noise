# init(_:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../../coreml.md) > [MLFeatureValue](../../mlfeaturevalue.md) > [MLFeatureValue.ImageOption](../imageoption.md)

---

Creates an image feature option key from a string.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(_ rawValue: String)
```

### Parameters

- **`rawValue`**
  A string that represents the name of the image feature option key.

## Overview

Don’t use this initializer directly. Create an image option key with [cropAndScale](cropandscale.md) or [cropRect](croprect.md) instead.

## See Also

### Image option key initializers

- [init(rawValue:)](init(rawvalue:).md)
  Creates an image feature option key from a raw value string.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
