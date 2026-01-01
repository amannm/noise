# specializationStrategy

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLOptimizationHints](../mloptimizationhints-swift.struct.md)

---

Optimization strategy for the model specialization.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var specializationStrategy: MLOptimizationHints.SpecializationStrategy
```

## Overview

Core ML segments the model’s compute graph and specializes each segment for the target compute device. This process can affect the model loading time and the prediction latency.

Use this option to tailor the specialization strategy for your model.

## See Also

### Getting the specialization strategy

- [MLOptimizationHints.SpecializationStrategy](specializationstrategy-swift.enum.md)
  The optimization strategy for the model specialization.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
