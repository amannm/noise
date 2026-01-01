# MLModelError.Code

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelError](../mlmodelerror-swift.struct.md)

---

Information about a Core ML model error.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum Code
```

## Topics

### Error codes

- [MLModelError.Code.featureType](code/featuretype.md)
  An error code for problems related to model features.

- [MLModelError.Code.parameters](code/parameters.md)
  An error code for problems related to model parameters.

- [MLModelError.Code.modelCollection](code/modelcollection.md)
  An error code for problems related to retrieving a model collection from the deployment system.

- [MLModelError.Code.modelDecryptionKeyFetch](code/modeldecryptionkeyfetch.md)
  An error code for problems related to retrieving a model’s decryption key.

- [MLModelError.Code.modelDecryption](code/modeldecryption.md)
  An error code for problems related to decrypting models.

- [MLModelError.Code.update](code/update.md)
  An error code for problems related to on-device model updates.

- [MLModelError.Code.customLayer](code/customlayer.md)
  An error code for problems related to custom layers.

- [MLModelError.Code.customModel](code/custommodel.md)
  An error code for problems related to custom models.

- [MLModelError.Code.io](code/io.md)
  An error code for problems related to the system’s input or output.

- [MLModelError.Code.predictionCancelled](code/predictioncancelled.md)
  An error code for problems related to canceling the prediction before it completes.

- [MLModelError.Code.generic](code/generic.md)
  An error code for runtime issues that don’t apply to the other error codes.

### Error domain

- [MLModelErrorDomain](../mlmodelerrordomain.md)
  The domain for Core ML errors.

- [errorDomain](errordomain.md)

### Creating a model error

- [init(rawValue:)](code/init(rawvalue:).md)

## See Also

### Model errors

- [MLModelError](../mlmodelerror-swift.struct.md)
  Information about a Core ML model error.

- [MLModelErrorDomain](../mlmodelerrordomain.md)
  The domain for Core ML errors.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
