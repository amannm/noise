# int64Values

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLSequence](../mlsequence.md)

---

An array of 64-bit integers in the sequence.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var int64Values: [NSNumber] { get }
```

## Overview

Only use this property when the sequence’s [type](type.md) is [MLFeatureType.int64](../mlfeaturetype/int64.md).

## See Also

### Retrieving the Sequence’s Values

- [stringValues](stringvalues.md)
  An array of strings in the sequence.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
