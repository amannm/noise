# init(url:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelAsset](../mlmodelasset.md)

---

Constructs a ModelAsset from a compiled model URL.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(url compiledModelURL: URL) throws
```

### Parameters

- **`compiledModelURL`**
  Location on the disk where the model asset is present.

## Overview

A model asset or nil if there is an error.

## See Also

### Creating a model asset

- [init(specification:)](init(specification:).md)
  Creates a model asset from an in-memory model specification.

- [init(specification:blobMapping:)](init(specification:blobmapping:).md)
  Construct a model asset from an ML Program specification by replacing blob file references with corresponding in-memory blobs.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
