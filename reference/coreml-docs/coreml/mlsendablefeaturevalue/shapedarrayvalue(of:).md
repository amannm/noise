# shapedArrayValue(of:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLSendableFeatureValue](../mlsendablefeaturevalue.md)

---

Returns the shaped array value, if the contained value is a shaped array of the specified type.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func shapedArrayValue<Scalar>(of type: Scalar.Type) -> MLShapedArray<Scalar>? where Scalar : MLShapedArrayScalar
```

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
