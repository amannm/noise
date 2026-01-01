# Encrypting a Model in Your App

**Article**

**Framework:** Core ML

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

Encrypt your app’s built-in model at compile time by adding a compiler flag.

## Overview

Tell Xcode to encrypt your model as it compiles your app by adding a compiler flag to your build target.


In Xcode, navigate to your project’s target and open its Build Phases tab. Expand the Compile Sources section and select the model you want Xcode to encrypt at compile time. Open the model’s compiler flags editor by double-clicking the model’s entry.

In the editor, add:

1. The encryption flag “`--encrypt`”
2. A space character
3. The absolute path to the model’s encryption key file you created (see [Generating a Model Encryption Key](generating-a-model-encryption-key.md)), between quotation marks

Press the Return key or click outside the editor to close it.

![Screenshot of an Xcode project’s Build Phases tab, showing a model’s compiler flags editor. The editor’s text reads: dash-dash-encrypt, space, and then the path to the model beginning with quotation mark dollar-sign S-R-C-root and then the path to the model file, ending in “dot M-L-model key”.](https://docs-assets.developer.apple.com/published/a61804fee42dfe738a6dde83652ecea8/media-3675192%402x.png)


At runtime, you load the encrypted model the same way you load any other built-in model by using its `load(completionHandler:completionHandler:)` type method. This method behaves similarly to the [MLModel](mlmodel.md) type method [loadContentsOfURL:configuration:completionHandler:](https://developer.apple.com/documentation/coreml/mlmodel/loadcontentsofurl:configuration:completionhandler:) and creates an instance of the model using the convenience class that Xcode generates.

## See Also

### Model encryption

- [Generating a Model Encryption Key](generating-a-model-encryption-key.md)
  Create a model encryption key to encrypt a compiled model or model archive.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
