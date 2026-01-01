# MLModel

**Class**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

An encapsulation of all the details of your machine learning model.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLModel
```

## Overview

[MLModel](mlmodel.md) encapsulates a model’s prediction methods, configuration, and model description.

In most cases, you can use Core ML without accessing the [MLModel](mlmodel.md) class directly. Instead, use the programmer-friendly wrapper class that Xcode automatically generates when you add a model (see [Integrating a Core ML Model into Your App](integrating-a-core-ml-model-into-your-app.md)). If your app needs the [MLModel](mlmodel.md) interface, use the wrapper class’s `model` property.

With the [MLModel](mlmodel.md) interface, you can:

- Make a prediction with your app’s custom [MLFeatureProvider](mlfeatureprovider.md) by calling [prediction(from:)](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:)-9y2aa) or [prediction(from:options:)](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:options:)-81mr6).
- Make multiple predictions with your app’s custom [MLBatchProvider](mlbatchprovider.md) by calling [predictions(fromBatch:)](mlmodel/predictions(frombatch:).md) or [predictions(from:options:)](mlmodel/predictions(from:options:).md).
- Inspect your model’s [metadata](mlmodeldescription/metadata.md) and [MLFeatureDescription](mlfeaturedescription.md) instances through [modelDescription](mlmodel/modeldescription.md).

If your app downloads and compiles a model on the user’s device, you must use the [MLModel](mlmodel.md) class directly to make predictions. See [Downloading and Compiling a Model on the User’s Device](downloading-and-compiling-a-model-on-the-user-s-device.md).

> **Important**
>  Use an [MLModel](mlmodel.md) instance on one thread or one dispatch queue at a time. Do this by either serializing method calls to the model, or by creating a separate model instance for each thread and dispatch queue.

## Topics

### Loading a model

- [load(contentsOf:configuration:)](mlmodel/load(contentsof:configuration:).md)
  Construct a model asynchronously from a compiled model asset.

- [load(_:configuration:completionHandler:)](mlmodel/load(_:configuration:completionhandler:).md)
  Construct a model asynchronously from a compiled model asset.

- [load(contentsOf:configuration:completionHandler:)](mlmodel/load(contentsof:configuration:completionhandler:).md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.

- [init(contentsOf:)](mlmodel/init(contentsof:).md)
  Creates a Core ML model instance from a compiled model file.

- [init(contentsOf:configuration:)](mlmodel/init(contentsof:configuration:).md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.

- [init(contentsOfURL:)](mlmodel/init(contentsofurl:).md)

- [init(contentsOfURL:configuration:)](mlmodel/init(contentsofurl:configuration:).md)

### Compiling a model

- [compileModel(at:)](mlmodel/compilemodel(at:).md)

- [compileModel(at:completionHandler:)](mlmodel/compilemodel(at:completionhandler:).md)
  Compile a model for a device.

### Making predictions

- [prediction(from:)](mlmodel/prediction(from:).md)

- [prediction(from:options:)](mlmodel/prediction(from:options:).md)

- [predictions(fromBatch:)](mlmodel/predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.

- [predictions(from:options:)](mlmodel/predictions(from:options:).md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.

- [prediction(from:using:)](mlmodel/prediction(from:using:).md)

- [prediction(from:using:options:)](mlmodel/prediction(from:using:options:).md)

- [MLPredictionOptions](mlpredictionoptions.md)
  The options available when making a prediction.

### Making state

- [makeState()](mlmodel/makestate().md)
  Creates a new state object.

### Inspecting a model

- [availableComputeDevices](mlmodel/availablecomputedevices-6klyt.md)
  The list of available compute devices that the model’s prediction methods use.

- [configuration](mlmodel/configuration.md)
  The configuration of the model set during initialization.

- [modelDescription](mlmodel/modeldescription.md)
  Model information you use at runtime during development, which Xcode also displays in its Core ML model editor view.

- [MLModelDescription](mlmodeldescription.md)
  Information about a model, primarily the input and output format for each feature the model expects, and optional metadata.

- [parameterValue(for:)](mlmodel/parametervalue(for:).md)
  Returns a model parameter value for a key.

- [MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.

### Supporting types

- [MLModelConfiguration](mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.

- [MLOptimizationHints](mloptimizationhints-swift.struct.md)

- [MLKey](mlkey.md)
  An abstract base class for machine learning key types.

## See Also

### Core ML models

- [Getting a Core ML Model](getting-a-core-ml-model.md)
  Obtain a Core ML model to use in your app.

- [Updating a Model File to a Model Package](updating-a-model-file-to-a-model-package.md)
  Convert a Core ML model file into a model package in Xcode.

- [Integrating a Core ML Model into Your App](integrating-a-core-ml-model-into-your-app.md)
  Add a simple model to an app, pass input data to the model, and process the model’s predictions.

- [Model Customization](model-customization.md)
  Expand and modify your model with new layers.

- [Model Personalization](model-personalization.md)
  Update your model to adapt to new data.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
