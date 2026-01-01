# isOptional

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLFeatureDescription](../mlfeaturedescription.md)

---

A Boolean value that indicates whether this feature is optional.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var isOptional: Bool { get }
```

## Overview

Optional values can be `nil`, for models that have inputs related to features being present or not.

## See Also

### Inspecting a feature

- [name](name.md)
  The name of this feature.

- [type](type.md)
  The type of this feature.

- [MLFeatureType](../mlfeaturetype.md)
  The possible types for feature values, input features, and output features.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
