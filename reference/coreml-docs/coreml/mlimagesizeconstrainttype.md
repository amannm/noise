# MLImageSizeConstraintType

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

The modes that determine how the model defines a feature’s image size constraint.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum MLImageSizeConstraintType
```

## Topics

### Constraint types

- [MLImageSizeConstraintType.range](mlimagesizeconstrainttype/range.md)
  The image feature accepts image sizes defined by a range of widths and a range of heights.

- [MLImageSizeConstraintType.enumerated](mlimagesizeconstrainttype/enumerated.md)
  The image feature accepts image sizes listed in an array.

- [MLImageSizeConstraintType.unspecified](mlimagesizeconstrainttype/unspecified.md)
  The image size constraint is not configured and should be ignored.

### Creating a constraint type

- [init(rawValue:)](mlimagesizeconstrainttype/init(rawvalue:).md)

## See Also

### Determining relevant constraints

- [type](mlimagesizeconstraint/type.md)
  Indicator of which properties to inspect for this image size constraint.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
