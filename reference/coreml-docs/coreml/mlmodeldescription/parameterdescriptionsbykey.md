# parameterDescriptionsByKey

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelDescription](../mlmodeldescription.md)

---

A dictionary of the descriptions for the model’s parameters.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var parameterDescriptionsByKey: [MLParameterKey : MLParameterDescription] { get }
```

## See Also

### Accessing update descriptions

- [isUpdatable](isupdatable.md)
  A Boolean value that indicates whether you can update the model with additional training.

- [trainingInputDescriptionsByName](traininginputdescriptionsbyname.md)
  A dictionary of the training input feature descriptions, which the model keys by the input’s name.

- [MLParameterDescription](../mlparameterdescription.md)
  A description of a model parameter that includes a default value and a constraint, if applicable.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
