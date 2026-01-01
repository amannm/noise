# init(dictionary:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLArrayBatchProvider](../mlarraybatchprovider.md)

---

Creates a batch provider based on feature names and their associated arrays of data.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(dictionary: [String : [Any]]) throws
```

### Parameters

- **`dictionary`**
  A dictionary which maps feature names to an array of values. The error case occurs when all the arrays do not have the same length or the values in an aray are not expressible as an [MLFeatureValue](../mlfeaturevalue.md).

## Overview

This initializer is convenient when the data are available as individual arrays.

```swift
let batch = try  MLArrayBatchProvider(dictionary: ["age": [30, 35, 29],
                                                   "weightLbs": [120.0, 170.4, 213.6]])
```

## See Also

### Creating a batch provider

- [init(array:)](init(array:).md)
  Creates the batch provider based on the array of feature providers.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
