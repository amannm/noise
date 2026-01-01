# load(_:configuration:completionHandler:)

**Type Method**

**Framework:** Core ML

**Availability:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModel](../mlmodel.md)

---

Construct a model asynchronously from a compiled model asset.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class func load(_ asset: MLModelAsset, configuration: MLModelConfiguration, completionHandler handler: @escaping (MLModel?, (any Error)?) -> Void)
```

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class func load(asset: MLModelAsset, configuration: MLModelConfiguration) async throws -> MLModel
```

### Parameters

- **`asset`**
  The compiled model asset derived from in-memory or on-disk Core ML model.

- **`configuration`**
  The model configuration that holds options for loading the model.

- **`handler`**
  The completion handler invoked when the load completes. A valid [MLModel](../mlmodel.md) returns on success, or an error if failure.

## See Also

### Loading a model

- [load(contentsOf:configuration:)](load(contentsof:configuration:).md)
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
