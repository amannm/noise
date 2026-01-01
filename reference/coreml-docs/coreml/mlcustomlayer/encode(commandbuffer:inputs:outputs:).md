# encode(commandBuffer:inputs:outputs:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 11.2+, iPadOS 11.2+, Mac Catalyst 13.1+, macOS 10.13.2+, tvOS 11.2+, visionOS 1.0+, watchOS 4.2+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLCustomLayer](../mlcustomlayer.md)

---

Encodes GPU commands to evaluate the custom layer.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
optional func encode(commandBuffer: any MTLCommandBuffer, inputs: [any MTLTexture], outputs: [any MTLTexture]) throws
```

### Parameters

- **`commandBuffer`**
  A command buffer that defines the work the layer performs on the GPU.

- **`inputs`**
  A texture array that represents the layer’s inputs.

- **`outputs`**
  A texture array that represents the layer’s outputs.

## Overview

Implement this method to use the GPU to evaluate your layer. Fill `commandBuffer` with the GPU commands that evaluate the layer. Don’t commit the command buffer in this method; Core ML executes the command buffer after this method returns.

Improve your layer’s performance by caching the [MTLComputePipelineState](https://developer.apple.com/documentation/Metal/MTLComputePipelineState) instances you create and intend to reuse in subsequent calls.

Implementing this method doesn’t guarantee that Core ML evaluates this layer on the GPU. For example, Core ML may evaluate the layer on the CPU if the system doesn’t have enough GPU’s resources to run the custom layer.

> **Important**
>  The GPU works with 16-bit floats, not 32-bit floats. Verify that lower precision values don’t impact your network’s behavior.

If you don’t implement this method, Core ML instead uses [evaluate(inputs:outputs:)](evaluate(inputs:outputs:).md).

For more information about using the GPU for general purpose programming, see `Compute Processing`.

## See Also

### Evaluating a layer

- [evaluate(inputs:outputs:)](evaluate(inputs:outputs:).md)
  Evaluates the custom layer with the given inputs.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
