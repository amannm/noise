# MLOptimizationHints.ReshapeFrequency

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLOptimizationHints](../mloptimizationhints-swift.struct.md)

---

The anticipated frequency of changing input shapes.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum ReshapeFrequency
```

## Topics

### Enumeration Cases

- [MLOptimizationHints.ReshapeFrequency.frequent](reshapefrequency-swift.enum/frequent.md)
  The input shape is expected to change frequently on each prediction sent to this loaded model instance. Core ML will try to minimize the latency associated with shape changes and avoid expensive shape-specific optimizations prior to prediction computation. While prediction computation may be slower for each specific shape, switching between shapes should be faster.  This is the default.

- [MLOptimizationHints.ReshapeFrequency.infrequent](reshapefrequency-swift.enum/infrequent.md)
  The input shape is expected to be stable and many/all predictions sent to this loaded model instance would use the same input shapes repeatedly. On the shape change, Core ML re-optimizes the internal engine for the new shape if possible. The re-optimization takes some time, but the subsequent predictions for the shape should run faster.

## See Also

### Getting the reshape frequency

- [reshapeFrequency](reshapefrequency-swift.property.md)
  The anticipated reshape frequency

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
