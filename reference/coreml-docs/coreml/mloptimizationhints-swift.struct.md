# MLOptimizationHints

**Structure**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
struct MLOptimizationHints
```

## Topics

### Creating optimization hints

- [init()](mloptimizationhints-swift.struct/init().md)
  Construct an MLOptimizationHints

### Getting the reshape frequency

- [reshapeFrequency](mloptimizationhints-swift.struct/reshapefrequency-swift.property.md)
  The anticipated reshape frequency

- [MLOptimizationHints.ReshapeFrequency](mloptimizationhints-swift.struct/reshapefrequency-swift.enum.md)
  The anticipated frequency of changing input shapes.

### Getting the specialization strategy

- [specializationStrategy](mloptimizationhints-swift.struct/specializationstrategy-swift.property.md)
  Optimization strategy for the model specialization.

- [MLOptimizationHints.SpecializationStrategy](mloptimizationhints-swift.struct/specializationstrategy-swift.enum.md)
  The optimization strategy for the model specialization.

## See Also

### Supporting types

- [MLModelConfiguration](mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.

- [MLKey](mlkey.md)
  An abstract base class for machine learning key types.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
