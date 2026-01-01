# features(at:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLBatchProvider](../mlbatchprovider.md)

---

Returns the feature provider at the given index.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func features(at index: Int) -> any MLFeatureProvider
```

### Parameters

- **`index`**
  The index of the desired feature provider.

## Overview

The feature provider at the given index.

## See Also

### Accessing values

- [count](count.md)
  The number of feature providers in this batch.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
