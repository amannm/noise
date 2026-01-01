# init(from:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArray](../mlshapedarray.md)

---

Creates a shaped array from a decoder.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(from decoder: any Decoder) throws
```

### Parameters

- **`decoder`**
  The decoder to read data from.

## Overview

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## See Also

### Encoding and decoding

- [encode(to:)](encode(to:).md)
  Encode a shaped array.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
