# init(specification:blobMapping:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelAsset](../mlmodelasset.md)

---

Construct a model asset from an ML Program specification by replacing blob file references with corresponding in-memory blobs.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS

```objc
convenience init(specification specificationData: Data, blobMapping: [URL : Data]) throws
```

### Parameters

- **`blobMapping`**
  A dictionary with blob URL as the key and blob data as the value.

## Overview

An ML Program may use `BlobFileValue` syntax, which stores the blob data in external files and refers them by URL. This factory method enables in-memory workflow for such models by using the specified in-memory blob data in place of the external files.

The format of in-memory blobs must be the same as the external files. The dictionary must contain all the reference URLs used in the specification.

## See Also

### Creating a model asset

- [init(specification:)](init(specification:).md)
  Creates a model asset from an in-memory model specification.

- [init(url:)](init(url:).md)
  Constructs a ModelAsset from a compiled model URL.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
