# weights

**Type Property**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLParameterKey](../mlparameterkey.md)

---

The key you use to access the weights of a layer in a neural network model.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class var weights: MLParameterKey { get }
```

## Overview

The value type for the [weights](weights.md) key is an [MLMultiArray](../mlmultiarray.md). You must scope this key with the name of the specific neural network layer whose weights you’d like to access. See [scoped(to:)](scoped(to:).md).

> **Note**
>  You can only override the weights of a model’s *updatable* layers. Model developers mark these layers as updatable with the [Core ML Tools](https://coremltools.readme.io/).

## See Also

### Accessing neural network layer parameters

- [biases](biases.md)
  The key you use to access the biases of a layer in a neural network model.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
