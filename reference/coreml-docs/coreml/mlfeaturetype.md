# MLFeatureType

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

The possible types for feature values, input features, and output features.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum MLFeatureType
```

## Topics

### Feature types

- [MLFeatureType.int64](mlfeaturetype/int64.md)
  The type for integer features and feature values.

- [MLFeatureType.double](mlfeaturetype/double.md)
  The type for double features and feature values.

- [MLFeatureType.image](mlfeaturetype/image.md)
  The type for image features and feature values.

- [MLFeatureType.multiArray](mlfeaturetype/multiarray.md)
  The type for multidimensional array features and feature values.

- [MLFeatureType.string](mlfeaturetype/string.md)
  The type for string features and feature values.

- [MLFeatureType.dictionary](mlfeaturetype/dictionary.md)
  The type for dictionary features and feature values.

- [MLFeatureType.sequence](mlfeaturetype/sequence.md)
  The type for sequence features and feature values.

- [MLFeatureType.state](mlfeaturetype/state.md)
  MLState. Represents a model state that may be updated in each inference.

- [MLFeatureType.invalid](mlfeaturetype/invalid.md)
  The type for invalid feature values.

### Creating a feature type

- [init(rawValue:)](mlfeaturetype/init(rawvalue:).md)

## See Also

### Supporting types

- [MLShapedArray](mlshapedarray.md)
  A machine learning collection type that stores scalar values in a multidimensional array.

- [MLShapedArrayProtocol](mlshapedarrayprotocol.md)
  An interface that defines a shaped array type.

- [MLMultiArray](mlmultiarray.md)
  A machine learning collection type that stores numeric values in an array with multiple dimensions.

- [MLSequence](mlsequence.md)
  A machine learning collection type that stores a series of strings or integers.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
