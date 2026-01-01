# load(asset:configuration:)

**Type Method**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLComputePlan](../mlcomputeplan-1w21n.md)

---

Construct the compute plan of a model asynchronously given the model asset.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
static func load(asset: MLModelAsset, configuration: MLModelConfiguration) async throws -> MLComputePlan
```

### Parameters

- **`asset`**
  The model asset.

- **`configuration`**
  The model configuration.

## See Also

### Loading a compute plan

- [load(contentsOf:configuration:)](load(contentsof:configuration:).md)
  Construct the compute plan of a model asynchronously given the location of its on-disk representation.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
