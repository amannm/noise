# init(array:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLArrayBatchProvider](../mlarraybatchprovider.md)

---

Creates the batch provider based on the array of feature providers.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(array: [any MLFeatureProvider])
```

### Parameters

- **`array`**
  The array of feature providers for the batch.

## See Also

### Creating a batch provider

- [init(dictionary:)](init(dictionary:).md)
  Creates a batch provider based on feature names and their associated arrays of data.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
