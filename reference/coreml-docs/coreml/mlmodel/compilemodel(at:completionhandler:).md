# compileModel(at:completionHandler:)

**Type Method**

**Framework:** Core ML

**Availability:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModel](../mlmodel.md)

---

Compile a model for a device.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS

```objc
class func compileModel(at url: URL, completionHandler handler: @escaping (Result<URL, any Error>) -> Void)
```

### Parameters

- **`url`**
  The URL to the model file.

- **`handler`**
  The completion handler the framework calls when the compilation completes.

## See Also

### Compiling a model

- [compileModel(at:)](compilemodel(at:).md)

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
