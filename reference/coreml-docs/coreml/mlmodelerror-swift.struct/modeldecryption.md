# modelDecryption

**Type Property**

**Framework:** Core ML

**Availability:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelError](../mlmodelerror-swift.struct.md)

---

An error code for problems related to decrypting models.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
static var modelDecryption: MLModelError.Code { get }
```

## Overview

Core ML typically throws this error when the framework can’t decrypt a model.

The framework can’t decrypt encrypted models in macOS if System Integrity Protection (SIP) is disabled.

## See Also

### Error Codes

- [featureType](featuretype.md)
  An error code for problems related to model features.

- [parameters](parameters.md)
  An error code for problems related to model parameters.

- [modelCollection](modelcollection.md)
  An error code for problems related to retrieving a model collection from the deployment system.

- [modelDecryptionKeyFetch](modeldecryptionkeyfetch.md)
  An error code for problems related to retrieving a model’s decryption key.

- [update](update.md)
  An error code for problems related to on-device model updates.

- [customLayer](customlayer.md)
  An error code for problems related to custom layers.

- [customModel](custommodel.md)
  An error code for problems related to custom models.

- [io](io.md)
  An error code for problems related to the system’s input or output.

- [predictionCancelled](predictioncancelled.md)
  An error code for problems related to cancelling the prediction before it completes.

- [generic](generic.md)
  An error code for runtime issues that don’t apply to the other error codes.

- [MLModelError.Code](code.md)
  Information about a Core ML model error.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
