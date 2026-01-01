# prediction(from:options:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLCustomModel](../mlcustommodel.md)

---

Predicts output values from the given input features.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func prediction(from input: any MLFeatureProvider, options: MLPredictionOptions) throws -> any MLFeatureProvider
```

### Parameters

- **`input`**
  The feature values the models needs to make its prediction.

- **`options`**
  The options to be applied to the prediction.

## Overview

A feature provider that represents the model’s prediction.

## See Also

### Making predictions

- [predictions(from:options:)](predictions(from:options:).md)
  Predicts output values from the given batch of input features.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
