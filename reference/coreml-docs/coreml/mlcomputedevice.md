# MLComputeDevice

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

Compute devices for framework operations.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum MLComputeDevice
```

## Topics

### Device types

- [MLComputeDevice.cpu(_:)](mlcomputedevice/cpu(_:).md)
  A device that represents a CPU compute device.

- [MLComputeDevice.gpu(_:)](mlcomputedevice/gpu(_:).md)
  A device that represents a GPU compute device.

- [MLComputeDevice.neuralEngine(_:)](mlcomputedevice/neuralengine(_:).md)
  A device that represents a Neural Engine compute device.

### Getting all devices

- [allComputeDevices](mlcomputedevice/allcomputedevices.md)
  Returns an array that contains all of the compute devices that are accessible.

## See Also

### Compute devices

- [MLCPUComputeDevice](mlcpucomputedevice.md)
  An object that represents a CPU compute device.

- [MLGPUComputeDevice](mlgpucomputedevice.md)
  An object that represents a GPU compute device.

- [MLNeuralEngineComputeDevice](mlneuralenginecomputedevice.md)
  An object that represents a Neural Engine compute device.

- [MLComputeDeviceProtocol](mlcomputedeviceprotocol.md)
  An interface that represents a compute device type.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
