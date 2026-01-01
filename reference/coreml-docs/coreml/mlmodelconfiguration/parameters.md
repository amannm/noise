# parameters

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelConfiguration](../mlmodelconfiguration.md)

---

A dictionary of configuration settings your app can override when loading a model.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var parameters: [MLParameterKey : Any]? { get set }
```

## See Also

### Configuring model parameters

- [functionName](functionname.md)
  Function name that `MLModel` will use.

- [modelDisplayName](modeldisplayname.md)
  A human readable name of a model for display purposes.

- [MLParameterKey](../mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
