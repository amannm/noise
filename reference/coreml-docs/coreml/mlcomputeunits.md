# MLComputeUnits

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

The set of processing-unit configurations the model can use to make predictions.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum MLComputeUnits
```

## Overview

Use this enumeration to set or inspect the processing units you allow a model to use when it makes a prediction.

Use `all` to allow the OS to select the best processing unit to use (including the neural engine, if available).

Use [MLComputeUnits.cpuOnly](mlcomputeunits/cpuonly.md) to restrict the model to the CPU, if your app might run in the background or runs other GPU intensive tasks.

## Topics

### Processing Unit Configurations

- [MLComputeUnits.all](mlcomputeunits/all.md)
  The option you choose to allow the model to use all compute units available, including the neural engine.

- [MLComputeUnits.cpuOnly](mlcomputeunits/cpuonly.md)
  The option you choose to limit the model to only use the CPU.

- [MLComputeUnits.cpuAndGPU](mlcomputeunits/cpuandgpu.md)
  The option you choose to allow the model to use both the CPU and GPU, but not the neural engine.

- [MLComputeUnits.cpuAndNeuralEngine](mlcomputeunits/cpuandneuralengine.md)
  The option you choose to allow the model to use both the CPU and neural engine, but not the GPU.

### Creating compute units

- [init(rawValue:)](mlcomputeunits/init(rawvalue:).md)

## See Also

### Allowing access to processing units

- [computeUnits](mlmodelconfiguration/computeunits.md)
  The processing unit or units the model uses to make predictions.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
