# functionName

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelConfiguration](../mlmodelconfiguration.md)

---

Function name that `MLModel` will use.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var functionName: String? { get set }
```

## Overview

Some model types (e.g. ML Program) supports multiple functions in a model asset, where each `MLModel` instance is associated with a particular function.

Use `MLModelAsset` to get the list of available functions. Use `nil` to use a default function.

```swift
let configuration = MLModelConfiguration()
configuration.functionName = "my_function"
```

## See Also

### Configuring model parameters

- [modelDisplayName](modeldisplayname.md)
  A human readable name of a model for display purposes.

- [parameters](parameters.md)
  A dictionary of configuration settings your app can override when loading a model.

- [MLParameterKey](../mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
