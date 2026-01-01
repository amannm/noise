# isAllowedValue(_:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLFeatureDescription](../mlfeaturedescription.md)

---

Checks whether the model will accept an input feature value.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func isAllowedValue(_ value: MLFeatureValue) -> Bool
```

### Parameters

- **`value`**
  Given the `MLFeatureValue`, is it compatible with the `MLFeatureType` of this `MLFeatureDescription`.

## Overview

`True` if the given `MLFeatureValue` is acceptable to the model’s input feature, `false` otherwise.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
