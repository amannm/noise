# configuration

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModel](../mlmodel.md)

---

The configuration of the model set during initialization.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var configuration: MLModelConfiguration { get }
```

## See Also

### Inspecting a model

- [availableComputeDevices](availablecomputedevices-6klyt.md)
  The list of available compute devices that the model’s prediction methods use.

- [modelDescription](modeldescription.md)
  Model information you use at runtime during development, which Xcode also displays in its Core ML model editor view.

- [MLModelDescription](../mlmodeldescription.md)
  Information about a model, primarily the input and output format for each feature the model expects, and optional metadata.

- [parameterValue(for:)](parametervalue(for:).md)
  Returns a model parameter value for a key.

- [MLParameterKey](../mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
