# featureValue(for:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLFeatureProvider](../mlfeatureprovider.md)

---

Accesses the feature value given the feature’s name.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func featureValue(for featureName: String) -> MLFeatureValue?
```

### Parameters

- **`featureName`**
  The name of the feature of the desired value.

## Overview

The value of the feature, or nil if no value exists for that name.

## See Also

### Accessing values

- [featureNames](featurenames.md)
  The set of valid feature names.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
