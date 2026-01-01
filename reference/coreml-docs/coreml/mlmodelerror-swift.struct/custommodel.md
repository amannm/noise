# customModel

**Type Property**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelError](../mlmodelerror-swift.struct.md)

---

An error code for problems related to custom models.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
static var customModel: MLModelError.Code { get }
```

## Overview

Core ML typically throws this error when the custom model has a programming mistake. For example, a custom model’s prediction method fails with this error code if Core ML can’t find the custom model’s implementation.

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

- [modelDecryption](modeldecryption.md)
  An error code for problems related to decrypting models.

- [update](update.md)
  An error code for problems related to on-device model updates.

- [customLayer](customlayer.md)
  An error code for problems related to custom layers.

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
