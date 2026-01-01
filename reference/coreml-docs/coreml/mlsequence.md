# MLSequence

**Class**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A machine learning collection type that stores a series of strings or integers.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLSequence
```

## Overview

A sequence stores a series of integers or strings of any length as the underlying type of an `MLFeatureValue`. Some classifier models — typically natural language models, such as an [NLTagger](https://developer.apple.com/documentation/NaturalLanguage/NLTagger) — produce an [MLSequence](mlsequence.md) feature value from their output features.

## Topics

### Creating a sequence

- [init(strings:)](mlsequence/init(strings:).md)
  Creates a sequence of strings from a string array.

- [init(int64s:)](mlsequence/init(int64s:).md)
  Creates a sequence of integers from an array of numbers.

- [init(empty:)](mlsequence/init(empty:).md)
  Creates an empty sequence of strings or integers.

### Identifying the sequence’s element type

- [type](mlsequence/type.md)
  The underlying type of the sequence’s elements.

### Retrieving the Sequence’s Values

- [stringValues](mlsequence/stringvalues.md)
  An array of strings in the sequence.

- [int64Values](mlsequence/int64values.md)
  An array of 64-bit integers in the sequence.

## See Also

### Supporting types

- [MLFeatureType](mlfeaturetype.md)
  The possible types for feature values, input features, and output features.

- [MLShapedArray](mlshapedarray.md)
  A machine learning collection type that stores scalar values in a multidimensional array.

- [MLShapedArrayProtocol](mlshapedarrayprotocol.md)
  An interface that defines a shaped array type.

- [MLMultiArray](mlmultiarray.md)
  A machine learning collection type that stores numeric values in an array with multiple dimensions.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
