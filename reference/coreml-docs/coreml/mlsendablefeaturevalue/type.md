# type

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLSendableFeatureValue](../mlsendablefeaturevalue.md)

---

The type of value.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var type: MLFeatureType { get }
```

## See Also

### Accessing the values

- [doubleValue](doublevalue.md)
  The double-precision floating-point value, if the contained value is a double.

- [float16Value](float16value.md)
  The 16-bit floating-point value, if the contained value is a 16-bit float.

- [floatValue](floatvalue.md)
  The single-precision floating-point value, if the contained value is a float.

- [integerDictionaryValue](integerdictionaryvalue.md)
  The integer dictionary value, if the contained value is a dictionary of integers to numbers.

- [integerValue](integervalue.md)
  The integer value, if the contained value is an integer.

- [isScalar](isscalar.md)
  A Boolean value indicating whether the value is a single number.

- [isShapedArray](isshapedarray.md)
  A Boolean value indicating whether the value is a shaped array.

- [isUndefined](isundefined.md)
  A Boolean value indicating whether the value is missing or undefined.

- [stringArrayValue](stringarrayvalue.md)
  The string array value, if the contained value is an array of string.

- [stringDictionaryValue](stringdictionaryvalue.md)
  The string dictionary value, if the contained value is a dictionary of strings to numbers.

- [stringValue](stringvalue.md)
  The string value, if the contained value is a string.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
