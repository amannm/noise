# load(contentsOf:configuration:completionHandler:)

**Type Method**

**Framework:** Core ML

**Availability:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModel](../mlmodel.md)

---

Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class func load(contentsOf url: URL, configuration: MLModelConfiguration = MLModelConfiguration(), completionHandler handler: @escaping (Result<MLModel, any Error>) -> Void)
```

### Parameters

- **`url`**
  The path to a compiled model file (*ModelName*`.mlmodelc`), typically with the `URL` that [compileModel(at:)](https://developer.apple.com/documentation/coreml/mlmodel/compilemodel(at:)-6442s) returns.

- **`configuration`**
  The runtime settings for the new model instance.

- **`handler`**
  A closure the method calls when it finishes loading the model.

## Overview

Use this method to load a model asynchronously. Core ML calls your completion handler after it successfully loads the model, or encounters an error attempting to load it.


In Swift, if the model loaded successfully, you can use the instance from the [Result.success(_:)](https://developer.apple.com/documentation/Swift/Result/success(_:)) associated value; otherwise, use the [Result.failure(_:)](https://developer.apple.com/documentation/Swift/Result/failure(_:)) associated value to address the error. In Objective-C, you can use the [MLModel](../mlmodel.md) instance in your completion hander; otherwise, use the [NSError](https://developer.apple.com/documentation/Foundation/NSError) instance to address the error.  See [MLModelError.Code](../mlmodelerror-swift.struct/code.md) for the list of error codes.

## See Also

### Loading a model

- [load(contentsOf:configuration:)](load(contentsof:configuration:).md)
  Construct a model asynchronously from a compiled model asset.

- [load(_:configuration:completionHandler:)](load(_:configuration:completionhandler:).md)
  Construct a model asynchronously from a compiled model asset.

- [init(contentsOf:)](init(contentsof:).md)
  Creates a Core ML model instance from a compiled model file.

- [init(contentsOf:configuration:)](init(contentsof:configuration:).md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.

- [init(contentsOfURL:)](init(contentsofurl:).md)

- [init(contentsOfURL:configuration:)](init(contentsofurl:configuration:).md)

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
