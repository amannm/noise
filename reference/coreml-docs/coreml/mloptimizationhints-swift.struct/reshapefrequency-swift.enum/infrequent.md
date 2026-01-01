# MLOptimizationHints.ReshapeFrequency.infrequent

**Case**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../../coreml.md) > [MLOptimizationHints](../../mloptimizationhints-swift.struct.md) > [MLOptimizationHints.ReshapeFrequency](../reshapefrequency-swift.enum.md)

---

The input shape is expected to be stable and many/all predictions sent to this loaded model instance would use the same input shapes repeatedly. On the shape change, Core ML re-optimizes the internal engine for the new shape if possible. The re-optimization takes some time, but the subsequent predictions for the shape should run faster.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
case infrequent
```

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
