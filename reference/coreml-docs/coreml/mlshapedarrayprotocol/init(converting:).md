# init(converting:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArrayProtocol](../mlshapedarrayprotocol.md)

---

Initialize by converting a MLMultiArray of different scalar type.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(converting multiArray: MLMultiArray)
```

### Parameters

- **`multiArray`**
  MLMultiArray object

## Overview

Converting a floating number to an integer uses rounding-towards-zero method.

When necessary, the source values are truncated to fit the destination type, but the behavior is undefined if the source value is too large, too small, or otherwise not representable in the destination type.

## See Also

### Creating a shaped array type from another type

- [init(_:)](init(_:).md)
  Creates a shaped array type from a multiarray.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
