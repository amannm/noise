# stateConstraint

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLFeatureDescription](../mlfeaturedescription.md)

---

The state feature value constraint.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var stateConstraint: MLStateConstraint? { get }
```

## Overview

The property has a value when `.type == MLFeatureTypeState`.

## See Also

### Accessing feature constraints

- [imageConstraint](imageconstraint.md)
  The size and format constraints for an image feature.

- [MLImageConstraint](../mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.

- [dictionaryConstraint](dictionaryconstraint.md)
  The constraint for a dictionary feature.

- [MLDictionaryConstraint](../mldictionaryconstraint.md)
  The constraint on the keys for a dictionary feature.

- [multiArrayConstraint](multiarrayconstraint.md)
  The constraints on a multidimensional array feature.

- [MLMultiArrayConstraint](../mlmultiarrayconstraint.md)
  The shape and data type constraints for a multidimensional array feature.

- [sequenceConstraint](sequenceconstraint.md)
  The constraints for a sequence feature.

- [MLSequenceConstraint](../mlsequenceconstraint.md)
  The constraints for a sequence feature.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
