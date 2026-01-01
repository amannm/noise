# init(parameters:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 11.2+, iPadOS 11.2+, Mac Catalyst 13.1+, macOS 10.13.2+, tvOS 11.2+, visionOS 1.0+, watchOS 4.2+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLCustomLayer](../mlcustomlayer.md)

---

Initializes the custom layer implementation.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(parameters: [String : Any]) throws
```

### Parameters

- **`parameters`**
  The contents of the parameter dictionary from the `.mlmodel` file.

## Overview

Implement this method to initialize your custom layer. It is called once, at load time. Use the parameters to configure the custom layer as needed.

If the layer cannot be initialized, your implementation should throw a [customLayer](../mlmodelerror-swift.struct/customlayer.md) error.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
