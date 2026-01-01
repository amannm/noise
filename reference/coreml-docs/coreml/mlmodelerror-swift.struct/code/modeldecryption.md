# MLModelError.Code.modelDecryption

**Case**

**Framework:** Core ML

**Availability:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../../coreml.md) > [MLModelError](../../mlmodelerror-swift.struct.md) > [MLModelError.Code](../code.md)

---

An error code for problems related to decrypting models.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
case modelDecryption
```

## Overview

Core ML typically throws (Swift) or returns (Objective-C) this error when the framework can’t decrypt a model.

The framework can’t decrypt encrypted models in macOS if System Integrity Protection (SIP) is disabled.

## See Also

### Error codes

- [MLModelError.Code.featureType](featuretype.md)
  An error code for problems related to model features.

- [MLModelError.Code.parameters](parameters.md)
  An error code for problems related to model parameters.

- [MLModelError.Code.modelCollection](modelcollection.md)
  An error code for problems related to retrieving a model collection from the deployment system.

- [MLModelError.Code.modelDecryptionKeyFetch](modeldecryptionkeyfetch.md)
  An error code for problems related to retrieving a model’s decryption key.

- [MLModelError.Code.update](update.md)
  An error code for problems related to on-device model updates.

- [MLModelError.Code.customLayer](customlayer.md)
  An error code for problems related to custom layers.

- [MLModelError.Code.customModel](custommodel.md)
  An error code for problems related to custom models.

- [MLModelError.Code.io](io.md)
  An error code for problems related to the system’s input or output.

- [MLModelError.Code.predictionCancelled](predictioncancelled.md)
  An error code for problems related to canceling the prediction before it completes.

- [MLModelError.Code.generic](generic.md)
  An error code for runtime issues that don’t apply to the other error codes.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
