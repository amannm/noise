# MLParameterKey

**Class**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

The keys for the parameter dictionary in a model configuration or a model update context.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLParameterKey
```

## Overview

Use an [MLParameterKey](mlparameterkey.md) to retrieve a model’s parameter value using:

- The model’s [parameterValue(for:)](mlmodel/parametervalue(for:).md) method
- The [parameters](mlmodelconfiguration/parameters.md) dictionary of an [MLModelConfiguration](mlmodelconfiguration.md)
- The [parameters](mlupdatecontext/parameters.md) dictionary of an [MLUpdateContext](mlupdatecontext.md)

> **Note**
>  To access the parameter of a specific model within a pipeline model, use the parameter key’s [scoped(to:)](mlparameterkey/scoped(to:).md) method with the model’s name.


To override a model’s default parameter values:

1. Create an [MLModelConfiguration](mlmodelconfiguration.md) instance.
2. Use an [MLParameterKey](mlparameterkey.md) for each parameter to set its value in the model configuration’s [parameters](mlmodelconfiguration/parameters.md) dictionary.
3. Create a new model instance using [init(contentsOf:configuration:)](mlmodel/init(contentsof:configuration:).md) with your custom model configuration.


To configure the update parameters for an [MLUpdateTask](mlupdatetask.md):

1. Create an [MLModelConfiguration](mlmodelconfiguration.md) instance.
2. Use an [MLParameterKey](mlparameterkey.md) for each parameter to set its value in the model configuration’s [parameters](mlmodelconfiguration/parameters.md) dictionary.
3. Create a new update task with your custom model configuration.

See [Personalizing a Model with On-Device Updates](personalizing-a-model-with-on-device-updates.md).

## Topics

### Scoping parameter keys

- [scoped(to:)](mlparameterkey/scoped(to:).md)
  Creates a copy of a parameter key and adds the scope to it.

### Accessing model parameters

- [numberOfNeighbors](mlparameterkey/numberofneighbors.md)
  The key you use to access the number of neighbors that adjusts the affinity of a k-nearest-neighbor model.

- [linkedModelFileName](mlparameterkey/linkedmodelfilename.md)
  The key you use to access the linked model’s filename.

- [linkedModelSearchPath](mlparameterkey/linkedmodelsearchpath.md)
  The key you use to access the linked model’s search path.

### Accessing neural network layer parameters

- [weights](mlparameterkey/weights.md)
  The key you use to access the weights of a layer in a neural network model.

- [biases](mlparameterkey/biases.md)
  The key you use to access the biases of a layer in a neural network model.

### Accessing model update parameters

- [learningRate](mlparameterkey/learningrate.md)
  The key you use to access the optimizer’s learning rate parameter.

- [momentum](mlparameterkey/momentum.md)
  The key you use to access the stochastic gradient descent (SGD) optimizer’s momentum parameter.

- [miniBatchSize](mlparameterkey/minibatchsize.md)
  The key you use to access the optimizer’s mini batch-size parameter.

- [beta1](mlparameterkey/beta1.md)
  The key you use to access the Adam optimizer’s first beta parameter.

- [beta2](mlparameterkey/beta2.md)
  The key you use to access the Adam optimizer’s second beta parameter.

- [eps](mlparameterkey/eps.md)
  The key you use to access the Adam optimizer’s epsilon parameter.

- [epochs](mlparameterkey/epochs.md)
  The key you use to access the optimizer’s epochs parameter.

- [shuffle](mlparameterkey/shuffle.md)
  The key you use to access the shuffle parameter, a Boolean value that determines whether the model randomizes the data between epochs.

- [seed](mlparameterkey/seed.md)
  The key you use to access the seed parameter that initializes the random number generator for the shuffle option.

## See Also

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

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
