# cpuOnly

**Type Property**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLComputePolicy](../mlcomputepolicy.md)

---

Execute ML workloads using the CPU.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
static var cpuOnly: MLComputePolicy { get }
```

## See Also

### Compute policies

- [cpuAndGPU](cpuandgpu.md)
  Execute ML workloads using the GPU if available, otherwise falling back to the CPU.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
