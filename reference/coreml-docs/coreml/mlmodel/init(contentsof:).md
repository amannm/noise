# init(contentsOf:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModel](../mlmodel.md)

---

Creates a Core ML model instance from a compiled model file.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(contentsOf url: URL) throws
```

### Parameters

- **`url`**
  The path to a compiled model file (*ModelName*`.mlmodelc`), typically with the `URL` that [compileModel(at:)](https://developer.apple.com/documentation/coreml/mlmodel/compilemodel(at:)-6442s) returns.

## Overview

In most cases, your app won’t need to create a model object directly. Consider the programmer-friendly wrapper class that Xcode automatically generates when you add a model to your project (see [Integrating a Core ML Model into Your App](../integrating-a-core-ml-model-into-your-app.md)).

If the wrapper class doesn’t meet your app’s needs or you need to customize the model’s configuration, use this initializer to create a model object from any compiled model file you can access. Typically, you use this initializer after your app has downloaded and compiled a model, which is one technique for saving space in your app (see [Downloading and Compiling a Model on the User’s Device](../downloading-and-compiling-a-model-on-the-user-s-device.md)).

## See Also

### Loading a model

- [load(contentsOf:configuration:)](load(contentsof:configuration:).md)
  Construct a model asynchronously from a compiled model asset.

- [load(_:configuration:completionHandler:)](load(_:configuration:completionhandler:).md)
  Construct a model asynchronously from a compiled model asset.

- [load(contentsOf:configuration:completionHandler:)](load(contentsof:configuration:completionhandler:).md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.

- [init(contentsOf:configuration:)](init(contentsof:configuration:).md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.

- [init(contentsOfURL:)](init(contentsofurl:).md)

- [init(contentsOfURL:configuration:)](init(contentsofurl:configuration:).md)

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
