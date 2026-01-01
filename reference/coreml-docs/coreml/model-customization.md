# Model Customization

**API Collection**

**Framework:** Core ML

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

Expand and modify your model with new layers.

## Overview

Customize your Core ML model to make it work better for your specific app. For instance, create one or more custom layers to improve accuracy by increasing the model’s capacity to capture information. You can also reduce the model’s size to optimize the contents of your app bundle.

## Topics

### Model file size

- [Reducing the Size of Your Core ML App](reducing-the-size-of-your-core-ml-app.md)
  Reduce the storage used by the Core ML model inside your app bundle.

### Custom model layers

- [Creating and Integrating a Model with Custom Layers](creating-and-integrating-a-model-with-custom-layers.md)
  Add models with custom neural-network layers to your app.

- [MLCustomLayer](mlcustomlayer.md)
  An interface that defines the behavior of a custom layer in your neural network model.

### Custom models

- [MLCustomModel](mlcustommodel.md)
  An interface that defines the behavior of a custom model.

## See Also

### Core ML models

- [Getting a Core ML Model](getting-a-core-ml-model.md)
  Obtain a Core ML model to use in your app.

- [Updating a Model File to a Model Package](updating-a-model-file-to-a-model-package.md)
  Convert a Core ML model file into a model package in Xcode.

- [Integrating a Core ML Model into Your App](integrating-a-core-ml-model-into-your-app.md)
  Add a simple model to an app, pass input data to the model, and process the model’s predictions.

- [MLModel](mlmodel.md)
  An encapsulation of all the details of your machine learning model.

- [Model Personalization](model-personalization.md)
  Update your model to adapt to new data.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
