# preferredMetalDevice

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelConfiguration](../mlmodelconfiguration.md)

---

The metal device you prefer this model use to make predictions (inference) and update the model.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var preferredMetalDevice: (any MTLDevice)? { get set }
```

## Overview

If [preferredMetalDevice](preferredmetaldevice.md) is `nil`, the default value, Core ML chooses a metal device for you.

## See Also

### Configuring GPU usage

- [allowLowPrecisionAccumulationOnGPU](allowlowprecisionaccumulationongpu.md)
  A Boolean value that determines whether to allow low-precision accumulation on a GPU.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
