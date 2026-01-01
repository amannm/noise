# modelDescription(completionHandler:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelAsset](../mlmodelasset.md)

---

The default model descripton.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func modelDescription(completionHandler handler: @escaping (MLModelDescription?, (any Error)?) -> Void)
```

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var modelDescription: MLModelDescription { get async throws }
```

## Overview

Use this method to get the description of the model such as the feature descriptions, the model author, and other metadata.

For the multi-function model asset, this method vends the description for the default function. Use `modelDescription(for:)` to get the model description of other functions.

```swift
let modelAsset = try MLModelAsset(url: modelURL)
let modelDescription = try await modelAsset.modelDescription()
print(modelDescription)
```

## See Also

### Getting the model description

- [modelDescription(ofFunctionNamed:completionHandler:)](modeldescription(offunctionnamed:completionhandler:).md)
  The model descripton for a specified function.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
