# MLKey

**Class**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

An abstract base class for machine learning key types.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLKey
```

## Overview

You don’t create use this class directly. Instead, use a class that inherits from this one, such as [MLParameterKey](mlparameterkey.md) or [MLMetricKey](mlmetrickey.md).

## Topics

### Retrieving a key’s information

- [name](mlkey/name.md)
  The name of the machine learning key.

- [scope](mlkey/scope.md)
  The applicable scope of the machine learning key.

## See Also

### Supporting types

- [MLModelConfiguration](mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.

- [MLOptimizationHints](mloptimizationhints-swift.struct.md)

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
