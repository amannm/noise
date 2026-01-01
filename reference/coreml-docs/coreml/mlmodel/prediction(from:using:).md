# prediction(from:using:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModel](../mlmodel.md)

---

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func prediction(from inputFeatures: any MLFeatureProvider, using state: MLState) throws -> any MLFeatureProvider
```

## See Also

### Making predictions

- [prediction(from:)](prediction(from:).md)

- [prediction(from:options:)](prediction(from:options:).md)

- [predictions(fromBatch:)](predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.

- [predictions(from:options:)](predictions(from:options:).md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.

- [prediction(from:using:options:)](prediction(from:using:options:).md)

- [MLPredictionOptions](../mlpredictionoptions.md)
  The options available when making a prediction.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
