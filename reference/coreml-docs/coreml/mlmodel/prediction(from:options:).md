# prediction(from:options:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModel](../mlmodel.md)

---

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func prediction(from input: any MLFeatureProvider, options: MLPredictionOptions) throws -> any MLFeatureProvider
```

## See Also

### Making predictions

- [prediction(from:)](prediction(from:).md)

- [predictions(fromBatch:)](predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.

- [predictions(from:options:)](predictions(from:options:).md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.

- [prediction(from:using:)](prediction(from:using:).md)

- [prediction(from:using:options:)](prediction(from:using:options:).md)

- [MLPredictionOptions](../mlpredictionoptions.md)
  The options available when making a prediction.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
