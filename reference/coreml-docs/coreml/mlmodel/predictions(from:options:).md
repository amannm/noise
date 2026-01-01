# predictions(from:options:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModel](../mlmodel.md)

---

Generates a prediction for each input feature provider within the batch provider using the prediction options.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func predictions(from inputBatch: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider
```

### Parameters

- **`inputBatch`**
  A batch provider that contains multiple input feature providers. The model makes a prediction for each feature provider.

- **`options`**
  The runtime settings the model uses as it makes a prediction.

## Overview

A batch provider that contains an output feature provider for each prediction.

Use this method to make more than one prediction at one time.

## See Also

### Making predictions

- [prediction(from:)](prediction(from:).md)

- [prediction(from:options:)](prediction(from:options:).md)

- [predictions(fromBatch:)](predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.

- [prediction(from:using:)](prediction(from:using:).md)

- [prediction(from:using:options:)](prediction(from:using:options:).md)

- [MLPredictionOptions](../mlpredictionoptions.md)
  The options available when making a prediction.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
