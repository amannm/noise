# withMultiArray(for:_:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLState](../mlstate.md)

---

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func withMultiArray<R>(for stateName: String, _ body: (MLMultiArray) throws -> R) rethrows -> R
```

## See Also

### Getting a state buffer

- [withMultiArray(_:)](withmultiarray(_:).md)

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
