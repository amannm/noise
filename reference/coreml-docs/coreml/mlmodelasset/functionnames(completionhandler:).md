# functionNames(completionHandler:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelAsset](../mlmodelasset.md)

---

The list of function names in the model asset.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func functionNames(completionHandler handler: @escaping ([String]?, (any Error)?) -> Void)
```

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var functionNames: [String] { get async throws }
```

## Overview

Some model types (e.g. ML Program) supports multiple functions. Use this method to query the function names.

The method vends the empty array when the model doesn’t use the multi-function configuration.

```swift
let modelAsset = try MLModelAsset(url: modelURL)
let functionNames = try await modelAsset.functionNames
print(functionNames) // For example, ["my_function1", "my_function2"];
```

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
