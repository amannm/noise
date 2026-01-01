# MLCustomLayer

**Protocol**

**Framework:** Core ML

**Availability:** iOS 11.2+, iPadOS 11.2+, Mac Catalyst 13.1+, macOS 10.13.2+, tvOS 11.2+, visionOS 1.0+, watchOS 4.2+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

An interface that defines the behavior of a custom layer in your neural network model.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
protocol MLCustomLayer
```

## Overview

You use the [MLCustomLayer](mlcustomlayer.md) protocol to define the behavior of your own neural network layers in Core ML models. You can deploy novel or proprietary models on your own release schedule. Custom layers also provide a mechanism for pre- or post-processing during model evaluation.

## Topics

### Creating a layer

- [init(parameters:)](mlcustomlayer/init(parameters:).md)
  Initializes the custom layer implementation.

### Integrating a layer

- [setWeightData(_:)](mlcustomlayer/setweightdata(_:).md)
  Assigns the weights for the connections within the layer.

- [outputShapes(forInputShapes:)](mlcustomlayer/outputshapes(forinputshapes:).md)
  Calculates the shapes of the output of this layer for the given input shapes.

### Evaluating a layer

- [evaluate(inputs:outputs:)](mlcustomlayer/evaluate(inputs:outputs:).md)
  Evaluates the custom layer with the given inputs.

- [encode(commandBuffer:inputs:outputs:)](mlcustomlayer/encode(commandbuffer:inputs:outputs:).md)
  Encodes GPU commands to evaluate the custom layer.

## See Also

### Custom model layers

- [Creating and Integrating a Model with Custom Layers](creating-and-integrating-a-model-with-custom-layers.md)
  Add models with custom neural-network layers to your app.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
