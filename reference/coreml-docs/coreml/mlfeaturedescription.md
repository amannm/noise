# MLFeatureDescription

**Class**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

The name, type, and constraints of an input or output feature.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLFeatureDescription
```

## Overview

In Core ML, a *feature* is a single input or output of a model. A model can have any number of *input features* or *output features*. Each feature has a name and a value type, which are defined in the feature’s `MLFeatureDescription`. Model authors use feature descriptions to help developers integrate their model properly. Each `MLFeatureDescription` instance has read-only properties that indicate the feature’s name, its type, and whether it’s optional.

For examples of features, see [Integrating a Core ML Model into Your App](integrating-a-core-ml-model-into-your-app.md). Note the three input features named `solarPanels`, `greenhouses`, and `size`, and the output feature is named `price`. All four features are of type `Double`.

An `MLFeatureDescription` may also include constraints, which specify the limitations of the model’s input and output features. For each input feature, the constraints describe what values the model expects from your app. For each output feature, the constraints describe what values your app should expect from the model. You can also write code to inspect these descriptions before using the model in your app.

## Topics

### Inspecting a feature

- [name](mlfeaturedescription/name.md)
  The name of this feature.

- [type](mlfeaturedescription/type.md)
  The type of this feature.

- [MLFeatureType](mlfeaturetype.md)
  The possible types for feature values, input features, and output features.

- [isOptional](mlfeaturedescription/isoptional.md)
  A Boolean value that indicates whether this feature is optional.

### Checking for validity

- [isAllowedValue(_:)](mlfeaturedescription/isallowedvalue(_:).md)
  Checks whether the model will accept an input feature value.

### Accessing feature constraints

- [stateConstraint](mlfeaturedescription/stateconstraint.md)
  The state feature value constraint.

- [imageConstraint](mlfeaturedescription/imageconstraint.md)
  The size and format constraints for an image feature.

- [MLImageConstraint](mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.

- [dictionaryConstraint](mlfeaturedescription/dictionaryconstraint.md)
  The constraint for a dictionary feature.

- [MLDictionaryConstraint](mldictionaryconstraint.md)
  The constraint on the keys for a dictionary feature.

- [multiArrayConstraint](mlfeaturedescription/multiarrayconstraint.md)
  The constraints on a multidimensional array feature.

- [MLMultiArrayConstraint](mlmultiarrayconstraint.md)
  The shape and data type constraints for a multidimensional array feature.

- [sequenceConstraint](mlfeaturedescription/sequenceconstraint.md)
  The constraints for a sequence feature.

- [MLSequenceConstraint](mlsequenceconstraint.md)
  The constraints for a sequence feature.

## See Also

### Accessing feature descriptions

- [stateDescriptionsByName](mlmodeldescription/statedescriptionsbyname.md)
  Description of the state features.

- [inputDescriptionsByName](mlmodeldescription/inputdescriptionsbyname.md)
  A dictionary of input feature descriptions, which the model keys by the input’s name.

- [outputDescriptionsByName](mlmodeldescription/outputdescriptionsbyname.md)
  A dictionary of output feature descriptions, which the model keys by the output’s name.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
