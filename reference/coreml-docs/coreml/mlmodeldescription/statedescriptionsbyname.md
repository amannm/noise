# stateDescriptionsByName

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelDescription](../mlmodeldescription.md)

---

Description of the state features.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var stateDescriptionsByName: [String : MLFeatureDescription] { get }
```

## See Also

### Accessing feature descriptions

- [inputDescriptionsByName](inputdescriptionsbyname.md)
  A dictionary of input feature descriptions, which the model keys by the input’s name.

- [outputDescriptionsByName](outputdescriptionsbyname.md)
  A dictionary of output feature descriptions, which the model keys by the output’s name.

- [MLFeatureDescription](../mlfeaturedescription.md)
  The name, type, and constraints of an input or output feature.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
