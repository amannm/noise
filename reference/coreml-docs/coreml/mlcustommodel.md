# MLCustomModel

**Protocol**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

An interface that defines the behavior of a custom model.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
protocol MLCustomModel
```

## Overview

To integrate your custom model with Core ML, adopt the [MLCustomModel](mlcustommodel.md) protocol in the implementation of your custom model. If you use a Swift class for your custom implementation, make it accessible to Core ML by using the `@objc(`*name*`)` attribute.

```swift
@objc(MyCustomModel)
class MyCustomModel: NSObject, MLCustomModel {
  ...
}
```

This defines the Objective-C name for the class, which Core ML needs to access your custom class’s implementation.

## Topics

### Creating the model

- [init(modelDescription:parameters:)](mlcustommodel/init(modeldescription:parameters:).md)
  Creates a custom model with the given description and parameters.

### Making predictions

- [prediction(from:options:)](mlcustommodel/prediction(from:options:).md)
  Predicts output values from the given input features.

- [predictions(from:options:)](mlcustommodel/predictions(from:options:).md)
  Predicts output values from the given batch of input features.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
