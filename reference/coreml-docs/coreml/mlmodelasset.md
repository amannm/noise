# MLModelAsset

**Class**

**Framework:** Core ML

**Availability:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

An abstraction of a compiled Core ML model asset.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLModelAsset
```

## Overview

[MLModelAsset](mlmodelasset.md) provides a unified interface by abstracting the compiled model representations for `.mlmodelc` files and in-memory representations.

To use an in-memory model, create an [MLModelAsset](mlmodelasset.md) with an in-memory model specification, then call [load(_:configuration:completionHandler:)](mlmodel/load(_:configuration:completionhandler:).md).

## Topics

### Creating a model asset

- [init(specification:)](mlmodelasset/init(specification:).md)
  Creates a model asset from an in-memory model specification.

- [init(specification:blobMapping:)](mlmodelasset/init(specification:blobmapping:).md)
  Construct a model asset from an ML Program specification by replacing blob file references with corresponding in-memory blobs.

- [init(url:)](mlmodelasset/init(url:).md)
  Constructs a ModelAsset from a compiled model URL.

### Getting function names

- [functionNames(completionHandler:)](mlmodelasset/functionnames(completionhandler:).md)
  The list of function names in the model asset.

### Getting the model description

- [modelDescription(completionHandler:)](mlmodelasset/modeldescription(completionhandler:).md)
  The default model descripton.

- [modelDescription(ofFunctionNamed:completionHandler:)](mlmodelasset/modeldescription(offunctionnamed:completionhandler:).md)
  The model descripton for a specified function.

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

- [MLArrayBatchProvider](mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
