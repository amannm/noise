# outputDescriptionsByName

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelDescription](../mlmodeldescription.md)

---

A dictionary of output feature descriptions, which the model keys by the output’s name.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var outputDescriptionsByName: [String : MLFeatureDescription] { get }
```

## See Also

### Accessing feature descriptions

- [stateDescriptionsByName](statedescriptionsbyname.md)
  Description of the state features.

- [inputDescriptionsByName](inputdescriptionsbyname.md)
  A dictionary of input feature descriptions, which the model keys by the input’s name.

- [MLFeatureDescription](../mlfeaturedescription.md)
  The name, type, and constraints of an input or output feature.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
