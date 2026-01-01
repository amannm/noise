# setWeightData(_:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 11.2+, iPadOS 11.2+, Mac Catalyst 13.1+, macOS 10.13.2+, tvOS 11.2+, visionOS 1.0+, watchOS 4.2+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLCustomLayer](../mlcustomlayer.md)

---

Assigns the weights for the connections within the layer.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func setWeightData(_ weights: [Data]) throws
```

### Parameters

- **`weights`**
  The data encoded in the `weights` field of the model specification.

## Overview

Implement this method to assign the weights for all the connections between nodes in your layer. This method is called once after the initialization call. Your implementation should validate the weights and throw an error if the weights do not have the expected shape or values.

The data encoded in the `weights` field of the `.mlmodel` file is loaded and passed into this method. If there are repeated weights in the `.mlmodel` file, they will be listed explicitly in the `weights` array. The weight values are provided in the order that they were defined during the custom layer conversion process. Keep a reference to the `weights` passed in because copying the `weights` array can significantly increase an app’s memory. Avoid modifying values of the weights.

## See Also

### Integrating a layer

- [outputShapes(forInputShapes:)](outputshapes(forinputshapes:).md)
  Calculates the shapes of the output of this layer for the given input shapes.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
