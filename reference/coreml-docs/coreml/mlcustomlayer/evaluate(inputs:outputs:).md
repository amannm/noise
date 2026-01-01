# evaluate(inputs:outputs:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 11.2+, iPadOS 11.2+, Mac Catalyst 13.1+, macOS 10.13.2+, tvOS 11.2+, visionOS 1.0+, watchOS 4.2+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLCustomLayer](../mlcustomlayer.md)

---

Evaluates the custom layer with the given inputs.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func evaluate(inputs: [MLMultiArray], outputs: [MLMultiArray]) throws
```

### Parameters

- **`inputs`**
  The array of inputs to be evaluated.

- **`outputs`**
  The array of outputs to be populated by evaluating the given inputs.

## Overview

Implement this method to evaluate the inputs using your layer’s custom behavior and to populate the output arrays. It will be called for each evaluation of your model performed on the CPU.

The memory for both input and output arrays is preallocated; don’t copy or move it. The inputs and outputs will have the shapes of the most recent call to [outputShapes(forInputShapes:)](outputshapes(forinputshapes:).md). Don’t modify the input values.

Investigate [vecLib](https://developer.apple.com/documentation/Accelerate/veclib) for methods that could optimize your implementation significantly.

## See Also

### Evaluating a layer

- [encode(commandBuffer:inputs:outputs:)](encode(commandbuffer:inputs:outputs:).md)
  Encodes GPU commands to evaluate the custom layer.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
