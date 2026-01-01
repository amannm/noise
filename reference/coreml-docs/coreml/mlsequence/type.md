# type

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLSequence](../mlsequence.md)

---

The underlying type of the sequence’s elements.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var type: MLFeatureType { get }
```

## Overview

The sequence’s underlying element type can only be either [MLFeatureType.string](../mlfeaturetype/string.md) or [MLFeatureType.int64](../mlfeaturetype/int64.md). Use this value to determine whether to access [stringValues](stringvalues.md) or [int64Values](int64values.md) at runtime.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
