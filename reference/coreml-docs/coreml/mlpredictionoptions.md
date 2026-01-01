# MLPredictionOptions

**Class**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

The options available when making a prediction.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLPredictionOptions
```

## Topics

### Getting features

- [outputBackings](mlpredictionoptions/outputbackings.md)
  A dictionary of feature names and client-allocated buffers.

### Restricting computation to the CPU

- [usesCPUOnly](mlpredictionoptions/usescpuonly.md)
  A Boolean value that indicates whether a prediction is computed using only the CPU.

## See Also

### Making predictions

- [prediction(from:)](mlmodel/prediction(from:).md)

- [prediction(from:options:)](mlmodel/prediction(from:options:).md)

- [predictions(fromBatch:)](mlmodel/predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.

- [predictions(from:options:)](mlmodel/predictions(from:options:).md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.

- [prediction(from:using:)](mlmodel/prediction(from:using:).md)

- [prediction(from:using:options:)](mlmodel/prediction(from:using:options:).md)

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
