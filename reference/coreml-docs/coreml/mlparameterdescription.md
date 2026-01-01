# MLParameterDescription

**Class**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A description of a model parameter that includes a default value and a constraint, if applicable.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLParameterDescription
```

## Topics

### Describing the model parameter

- [defaultValue](mlparameterdescription/defaultvalue.md)
  The default value for the parameter.

- [key](mlparameterdescription/key.md)
  The key for this parameter description value.

### Constraining numeric values

- [numericConstraint](mlparameterdescription/numericconstraint.md)
  The constraints of this paramter description value, if and only if the value is numerical.

- [MLNumericConstraint](mlnumericconstraint.md)
  The value limitations of a number.

## See Also

### Accessing update descriptions

- [isUpdatable](mlmodeldescription/isupdatable.md)
  A Boolean value that indicates whether you can update the model with additional training.

- [trainingInputDescriptionsByName](mlmodeldescription/traininginputdescriptionsbyname.md)
  A dictionary of the training input feature descriptions, which the model keys by the input’s name.

- [parameterDescriptionsByKey](mlmodeldescription/parameterdescriptionsbykey.md)
  A dictionary of the descriptions for the model’s parameters.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
