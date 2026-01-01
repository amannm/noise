# predictions(from:options:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLCustomModel](../mlcustommodel.md)

---

Predicts output values from the given batch of input features.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
optional func predictions(from inputBatch: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider
```

### Parameters

- **`inputBatch`**
  The batch of feature values the model needs to make its predictions.

- **`options`**
  The options to be applied to the predictions.

## Overview

A batch provider that represents the model’s predictions for the batch of inputs.

## See Also

### Making predictions

- [prediction(from:options:)](prediction(from:options:).md)
  Predicts output values from the given input features.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
