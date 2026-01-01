# init(shapedArray:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLFeatureValue](../mlfeaturevalue.md)

---

Creates a feature value that contains a shaped array.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init<Scalar>(shapedArray: MLShapedArray<Scalar>) where Scalar : MLShapedArrayScalar
```

### Parameters

- **`shapedArray`**
  An [MLShapedArray](../mlshapedarray.md) instance.

## See Also

### Creating multidimensional feature values

- [init(multiArray:)](init(multiarray:).md)
  Creates a feature value that contains a multidimensional array.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
