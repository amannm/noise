# init(specification:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelAsset](../mlmodelasset.md)

---

Creates a model asset from an in-memory model specification.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS

```objc
convenience init(specification specificationData: Data) throws
```

### Parameters

- **`specificationData`**
  The contents of a `.mlmodel` as a data blob.

## See Also

### Creating a model asset

- [init(specification:blobMapping:)](init(specification:blobmapping:).md)
  Construct a model asset from an ML Program specification by replacing blob file references with corresponding in-memory blobs.

- [init(url:)](init(url:).md)
  Constructs a ModelAsset from a compiled model URL.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
