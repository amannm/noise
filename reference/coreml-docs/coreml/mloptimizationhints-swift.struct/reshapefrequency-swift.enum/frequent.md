# MLOptimizationHints.ReshapeFrequency.frequent

**Case**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../../coreml.md) > [MLOptimizationHints](../../mloptimizationhints-swift.struct.md) > [MLOptimizationHints.ReshapeFrequency](../reshapefrequency-swift.enum.md)

---

The input shape is expected to change frequently on each prediction sent to this loaded model instance. Core ML will try to minimize the latency associated with shape changes and avoid expensive shape-specific optimizations prior to prediction computation. While prediction computation may be slower for each specific shape, switching between shapes should be faster.  This is the default.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
case frequent
```

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
