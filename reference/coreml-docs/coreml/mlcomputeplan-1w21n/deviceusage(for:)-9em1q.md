# deviceUsage(for:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLComputePlan](../mlcomputeplan-1w21n.md)

---

Returns the anticipated compute devices that would be used for executing a NeuralNetwork layer.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func deviceUsage(for layer: MLModelStructure.NeuralNetwork.Layer) -> MLComputePlan.DeviceUsage?
```

### Parameters

- **`layer`**
  A NeuralNetwork layer

## Overview

The anticipated compute devices that would be used for evaluating the layer or `nil` if the usage couldn’t be determined.

## See Also

### Getting the device usage

- [deviceUsage(for:)](deviceusage(for:).md)
  Returns the anticipated compute devices that would be used for executing a NeuralNetwork layer.

- [deviceUsage(for:)](deviceusage(for:)-7cdlm.md)
  Returns the anticipated compute devices that would be used for executing a MLProgram operation.

- [MLComputePlan.DeviceUsage](deviceusage.md)
  The anticipated compute devices that would be used for executing a layer/operation.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
