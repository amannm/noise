# momentum

**Type Property**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLParameterKey](../mlparameterkey.md)

---

The key you use to access the stochastic gradient descent (SGD) optimizer’s momentum parameter.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class var momentum: MLParameterKey { get }
```

## Overview

The value type for the [momentum](momentum.md) key is a [Double](https://developer.apple.com/documentation/Swift/Double).

## See Also

### Accessing model update parameters

- [learningRate](learningrate.md)
  The key you use to access the optimizer’s learning rate parameter.

- [miniBatchSize](minibatchsize.md)
  The key you use to access the optimizer’s mini batch-size parameter.

- [beta1](beta1.md)
  The key you use to access the Adam optimizer’s first beta parameter.

- [beta2](beta2.md)
  The key you use to access the Adam optimizer’s second beta parameter.

- [eps](eps.md)
  The key you use to access the Adam optimizer’s epsilon parameter.

- [epochs](epochs.md)
  The key you use to access the optimizer’s epochs parameter.

- [shuffle](shuffle.md)
  The key you use to access the shuffle parameter, a Boolean value that determines whether the model randomizes the data between epochs.

- [seed](seed.md)
  The key you use to access the seed parameter that initializes the random number generator for the shuffle option.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
