# MLArrayBatchProvider

**Class**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A convenience wrapper for batches of feature providers.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLArrayBatchProvider
```

## Overview

This batch provider supports an array of feature providers or a dictionary of arrays of feature values.

## Topics

### Creating a batch provider

- [init(array:)](mlarraybatchprovider/init(array:).md)
  Creates the batch provider based on the array of feature providers.

- [init(dictionary:)](mlarraybatchprovider/init(dictionary:).md)
  Creates a batch provider based on feature names and their associated arrays of data.

### Accessing the feature providers

- [array](mlarraybatchprovider/array.md)
  The array of feature providers.

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

- [MLBatchProvider](mlbatchprovider.md)
  An interface that represents a collection of feature providers.

- [MLModelAsset](mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
