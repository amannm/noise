# MLComputePlan.DeviceUsage

**Structure**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLComputePlan](../mlcomputeplan-1w21n.md)

---

The anticipated compute devices that would be used for executing a layer/operation.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
struct DeviceUsage
```

## Topics

### Getting the device usage

- [preferred](deviceusage/preferred.md)
  The compute device that the framework prefers to execute the layer/operation.

- [supported](deviceusage/supported.md)
  The compute devices that can execute the layer/operation.

## See Also

### Getting the device usage

- [deviceUsage(for:)](deviceusage(for:).md)
  Returns the anticipated compute devices that would be used for executing a NeuralNetwork layer.

- [deviceUsage(for:)](deviceusage(for:)-9em1q.md)
  Returns the anticipated compute devices that would be used for executing a NeuralNetwork layer.

- [deviceUsage(for:)](deviceusage(for:)-7cdlm.md)
  Returns the anticipated compute devices that would be used for executing a MLProgram operation.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
