# MLBatchProvider

**Protocol**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

An interface that represents a collection of feature providers.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
protocol MLBatchProvider
```

## Overview

Similar to the [MLFeatureProvider](mlfeatureprovider.md), this interface allows you to define your own batch provider. If you collect your data asynchronously or it is memory intensive, implement this protocol on your data structure to optimize performance with batch processing.

## Topics

### Accessing values

- [features(at:)](mlbatchprovider/features(at:).md)
  Returns the feature provider at the given index.

- [count](mlbatchprovider/count.md)
  The number of feature providers in this batch.

## See Also

### Model inputs and outputs

- [Making Predictions with a Sequence of Inputs](making-predictions-with-a-sequence-of-inputs.md)
  Integrate a recurrent neural network model to process sequences of inputs.

- [MLFeatureValue](mlfeaturevalue.md)
  A generic wrapper around an underlying value and the value’s type.

- [MLSendableFeatureValue](mlsendablefeaturevalue.md)
  A sendable feature value.

- [MLFeatureProvider](mlfeatureprovider.md)
  An interface that represents a collection of values for either a model’s input or its output.

- [MLDictionaryFeatureProvider](mldictionaryfeatureprovider.md)
  A convenience wrapper for the given dictionary of data.

- [MLArrayBatchProvider](mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.

- [MLModelAsset](mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
