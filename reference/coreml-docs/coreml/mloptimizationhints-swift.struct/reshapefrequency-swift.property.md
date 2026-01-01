# reshapeFrequency

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLOptimizationHints](../mloptimizationhints-swift.struct.md)

---

The anticipated reshape frequency

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var reshapeFrequency: MLOptimizationHints.ReshapeFrequency
```

## Overview

CoreML framework needs to reshape the model with new shapes for models with flexible input. Specify the anticipated reshape frequency (frequent or infrequent), so that the framework can optimize for fast shape switching or fast prediction on seen shapes.

The default value is frequent, which means CoreML tries to switch to new shapes as fast as possible

## See Also

### Getting the reshape frequency

- [MLOptimizationHints.ReshapeFrequency](reshapefrequency-swift.enum.md)
  The anticipated frequency of changing input shapes.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
