# metadata

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelDescription](../mlmodeldescription.md)

---

A dictionary of the model’s creation information, such as its description, author, version, and license.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var metadata: [MLModelMetadataKey : Any] { get }
```

## Overview

Use the keys defined by [MLModelMetadataKey](../mlmodelmetadatakey.md) to retrieve the dictionary’s entries.

## See Also

### Accessing metadata

- [classLabels](classlabels.md)
  An array of labels, which can be either strings or a numbers, for classifier models.

- [MLModelMetadataKey](../mlmodelmetadatakey.md)
  The set of keys the model uses to store values in its metadata dictionary.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
