# load(contentsOf:configuration:)

**Type Method**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModel](../mlmodel.md)

---

Construct a model asynchronously from a compiled model asset.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class func load(contentsOf url: URL, configuration: MLModelConfiguration = MLModelConfiguration()) async throws -> MLModel
```

### Parameters

- **`url`**
  The URL of the compiled model asset derived from in-memory or on-disk Core ML model.

- **`configuration`**
  The model configuration that hold options for loading the model.

## Overview

The loaded model, if successful; otherwise, `nil`.

## See Also

### Loading a model

- [load(_:configuration:completionHandler:)](load(_:configuration:completionhandler:).md)
  Construct a model asynchronously from a compiled model asset.

- [load(contentsOf:configuration:completionHandler:)](load(contentsof:configuration:completionhandler:).md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.

- [init(contentsOf:)](init(contentsof:).md)
  Creates a Core ML model instance from a compiled model file.

- [init(contentsOf:configuration:)](init(contentsof:configuration:).md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.

- [init(contentsOfURL:)](init(contentsofurl:).md)

- [init(contentsOfURL:configuration:)](init(contentsofurl:configuration:).md)

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
