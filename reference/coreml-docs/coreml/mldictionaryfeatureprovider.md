# MLDictionaryFeatureProvider

**Class**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A convenience wrapper for the given dictionary of data.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLDictionaryFeatureProvider
```

## Overview

If your input data is stored in a dictionary, consider this type of [MLFeatureProvider](mlfeatureprovider.md) that is backed by a dictionary. It is a convenience interface, saving you the trouble of iterating through the dictionary to assign all of its values.

## Topics

### Creating the provider

- [init(dictionary:)](mldictionaryfeatureprovider/init(dictionary:).md)
  Creates the feature provider based on a dictionary.

### Accessing the features

- [subscript(_:)](mldictionaryfeatureprovider/subscript(_:).md)
  Subscript interface for the feature provider to pass through to the dictionary.

- [dictionary](mldictionaryfeatureprovider/dictionary.md)
  The backing dictionary.

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

- [MLBatchProvider](mlbatchprovider.md)
  An interface that represents a collection of feature providers.

- [MLArrayBatchProvider](mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.

- [MLModelAsset](mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
