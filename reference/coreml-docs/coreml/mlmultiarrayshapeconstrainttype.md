# MLMultiArrayShapeConstraintType

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

The possible types of shape constraints.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum MLMultiArrayShapeConstraintType
```

## Topics

### Constraint types

- [MLMultiArrayShapeConstraintType.enumerated](mlmultiarrayshapeconstrainttype/enumerated.md)
  The constraint is an array of allowed shapes.

- [MLMultiArrayShapeConstraintType.range](mlmultiarrayshapeconstrainttype/range.md)
  The constraint is a set of ranges allowed for the array shape.

- [MLMultiArrayShapeConstraintType.unspecified](mlmultiarrayshapeconstrainttype/unspecified.md)
  The constraint type is undefined.

### Creating a constraint type

- [init(rawValue:)](mlmultiarrayshapeconstrainttype/init(rawvalue:).md)

## See Also

### Accessing the Constraints

- [enumeratedShapes](mlmultiarrayshapeconstraint/enumeratedshapes.md)
  Array of allowed shapes for a multiarray feature.

- [sizeRangeForDimension](mlmultiarrayshapeconstraint/sizerangefordimension.md)
  The allowable range for a dimention of the multiarray.

- [type](mlmultiarrayshapeconstraint/type.md)
  The type of the shape constraint.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
