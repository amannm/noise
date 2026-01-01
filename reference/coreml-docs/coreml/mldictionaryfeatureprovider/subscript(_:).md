# subscript(_:)

**Instance Subscript**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLDictionaryFeatureProvider](../mldictionaryfeatureprovider.md)

---

Subscript interface for the feature provider to pass through to the dictionary.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
subscript(featureName: String) -> MLFeatureValue? { get }
```

## See Also

### Accessing the features

- [dictionary](dictionary.md)
  The backing dictionary.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
