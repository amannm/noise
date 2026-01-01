# MLOptimizationHints.SpecializationStrategy

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLOptimizationHints](../mloptimizationhints-swift.struct.md)

---

The optimization strategy for the model specialization.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum SpecializationStrategy
```

## Topics

### Specialization strategies

- [MLOptimizationHints.SpecializationStrategy.default](specializationstrategy-swift.enum/default.md)
  The strategy that should work well for most applications.

- [MLOptimizationHints.SpecializationStrategy.fastPrediction](specializationstrategy-swift.enum/fastprediction.md)
  Prefer the prediction latency at the potential cost of specialization time, memory footprint, and the disk space usage of specialized artifacts.

## See Also

### Getting the specialization strategy

- [specializationStrategy](specializationstrategy-swift.property.md)
  Optimization strategy for the model specialization.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
