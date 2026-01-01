# load(contentsOf:)

**Type Method**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelStructure](../mlmodelstructure-swift.enum.md)

---

Load the model structure asynchronously given the location of its on-disk representation.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
static func load(contentsOf url: URL) async throws -> MLModelStructure
```

### Parameters

- **`url`**
  The location of its on-disk representation (.mlmodelc directory).

## See Also

### Loading a model structure

- [load(asset:)](load(asset:).md)
  Load the model structure asynchronously from the model asset.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
