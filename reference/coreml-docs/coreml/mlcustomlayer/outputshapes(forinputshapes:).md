# outputShapes(forInputShapes:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 11.2+, iPadOS 11.2+, Mac Catalyst 13.1+, macOS 10.13.2+, tvOS 11.2+, visionOS 1.0+, watchOS 4.2+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLCustomLayer](../mlcustomlayer.md)

---

Calculates the shapes of the output of this layer for the given input shapes.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func outputShapes(forInputShapes inputShapes: [[NSNumber]]) throws -> [[NSNumber]]
```

### Parameters

- **`inputShapes`**
  The shapes of the input for this layer.

## Overview

The shapes of the output for the given input shapes.

Implement this method to define the layer’s interface with the rest of the network. It will be called at least once at load time and any time the size of the inputs changes in a call to [prediction(from:)](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:)-9y2aa).

This method consumes and returns arrays of shapes, for inputs and outputs of the custom layer, respectively. See the [Core ML Neural Network specification](https://mlmodel.readme.io/reference/neuralnetwork) for more details about shapes and how layers use them.

## See Also

### Integrating a layer

- [setWeightData(_:)](setweightdata(_:).md)
  Assigns the weights for the connections within the layer.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
